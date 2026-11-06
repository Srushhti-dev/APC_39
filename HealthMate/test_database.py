"""Focused tests for database persistence and reminder scheduling."""

import hashlib
import sqlite3
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path

from database import (
    HealthMateDatabase,
    password_validation_error,
    username_validation_error,
)
from reminder_service import ReminderService


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.database = HealthMateDatabase(Path(self.temp_dir.name) / "test.db")

    def tearDown(self):
        self.database.close()
        self.temp_dir.cleanup()

    def test_password_validation_message_is_only_for_invalid_passwords(self):
        self.assertEqual(
            password_validation_error("short"),
            "Password must be at least 8 characters.",
        )
        self.assertEqual(
            password_validation_error("        "),
            "Password cannot contain only spaces.",
        )
        self.assertIsNone(password_validation_error("valid-pass"))

    def test_username_validation_message_is_only_for_invalid_usernames(self):
        self.assertEqual(username_validation_error(""), "Username cannot be empty.")
        self.assertEqual(
            username_validation_error("ab"),
            "Use 3–30 letters, numbers, dots, underscores, or hyphens; "
            "start with a letter or number.",
        )
        self.assertIsNotNone(username_validation_error("bad username"))
        self.assertIsNone(username_validation_error("health.user_1"))

    def test_local_account_registers_and_authenticates_with_hashed_password(self):
        self.assertFalse(self.database.account_exists())
        self.database.register_user("health.user", "secure-pass-123")
        self.assertTrue(self.database.account_exists())
        self.assertEqual(
            self.database.authenticate_user("HEALTH.USER", "secure-pass-123"),
            "health.user",
        )
        self.assertIsNone(
            self.database.authenticate_user("health.user", "incorrect-password")
        )
        self.assertIsNone(self.database.authenticate_user("unknown", "secure-pass-123"))
        row = self.database.connection.execute(
            "SELECT password_salt, password_hash FROM local_account WHERE id = 1"
        ).fetchone()
        self.assertNotEqual(row["password_hash"], b"secure-pass-123")
        self.assertEqual(len(row["password_salt"]), 16)

    def test_local_account_validates_username_and_password(self):
        for username in ("ab", "bad username", "   "):
            with self.subTest(username=username), self.assertRaises(ValueError):
                self.database.register_user(username, "secure-pass-123")
        for password in ("short", "        "):
            with self.subTest(password=password), self.assertRaises(ValueError):
                self.database.register_user("health.user", password)

    def test_multiple_local_accounts_can_be_created(self):
        self.database.register_user("health.user", "secure-pass-123")
        self.database.register_user("another.user", "another-pass-123")
        self.assertEqual(
            self.database.authenticate_user("another.user", "another-pass-123"),
            "another.user",
        )
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.database.register_user("HEALTH.USER", "different-password")

    def test_health_data_is_isolated_between_local_accounts(self):
        self.database.register_user("health.user", "secure-pass-123")
        self.database.update_profile("First User", 8)
        self.database.add_reminder("Morning walk", "Walking", "", "08:00")

        self.database.register_user("another.user", "another-pass-123")
        self.database.activate_user("another.user")
        self.assertEqual(self.database.get_profile()["display_name"], "HealthMate")
        self.assertEqual(self.database.get_reminders(), [])
        self.database.add_reminder("Drink water", "Water", "", "09:00")

        self.database.activate_user("health.user")
        self.assertEqual(self.database.get_profile()["display_name"], "First User")
        self.assertEqual(
            [item["title"] for item in self.database.get_reminders()],
            ["Morning walk"],
        )
        self.database.activate_user("another.user")
        self.assertEqual(
            [item["title"] for item in self.database.get_reminders()],
            ["Drink water"],
        )

    def test_legacy_single_account_database_migrates_for_multiple_users(self):
        legacy_path = Path(self.temp_dir.name) / "legacy.db"
        salt = b"0123456789abcdef"
        password_hash = hashlib.pbkdf2_hmac(
            "sha256", b"secure-pass-123", salt, 310_000
        )
        connection = sqlite3.connect(str(legacy_path))
        connection.execute(
            """
            CREATE TABLE local_account (
                id INTEGER PRIMARY KEY CHECK(id = 1),
                username TEXT NOT NULL COLLATE NOCASE UNIQUE,
                password_salt BLOB NOT NULL,
                password_hash BLOB NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        connection.execute(
            "INSERT INTO local_account VALUES (1, ?, ?, ?, ?)",
            ("legacy.user", salt, password_hash, "2026-01-01T00:00:00"),
        )
        connection.commit()
        connection.close()

        migrated_database = HealthMateDatabase(legacy_path)
        try:
            self.assertEqual(
                migrated_database.authenticate_user(
                    "legacy.user", "secure-pass-123"
                ),
                "legacy.user",
            )
            migrated_database.register_user("new.user", "another-pass-123")
            self.assertTrue(migrated_database.account_exists())
        finally:
            migrated_database.close()

    def test_duplicate_check_is_case_insensitive_and_can_exclude_edit(self):
        reminder_id = self.database.add_reminder(
            "Drink water", "Water", "", "09:30", ""
        )
        self.assertTrue(
            self.database.has_duplicate("drink water", "Water", "", "09:30")
        )
        self.assertFalse(
            self.database.has_duplicate(
                "Drink water", "Water", "", "09:30", exclude_id=reminder_id
            )
        )

    def test_daily_reminder_notifies_once_and_snoozes_for_five_minutes(self):
        self.database.add_reminder("Morning walk", "Exercise", "", "08:00", "")
        service = ReminderService(self.database)
        now = datetime(2026, 11, 1, 8, 0)
        self.assertEqual(len(service.check_due(now)), 1)
        self.assertEqual(service.check_due(now), [])

        self.database.snooze_reminder(1, now)
        self.assertEqual(service.check_due(now + timedelta(minutes=4, seconds=59)), [])
        self.assertEqual(
            len(service.check_due(now + timedelta(minutes=5))), 1
        )
        self.database.complete_reminder(1, now + timedelta(minutes=5))
        self.assertEqual(service.check_due(now + timedelta(minutes=6)), [])
        with self.assertRaisesRegex(ValueError, "completed today"):
            self.database.complete_reminder(1, now + timedelta(minutes=6))
        self.assertEqual(
            [row["status"] for row in self.database.history()],
            ["Done", "Snoozed", "Notified"],
        )

    def test_one_time_reminder_becomes_completed(self):
        self.database.add_reminder(
            "One time activity", "Other", "02-11-2026", "10:00", ""
        )
        self.database.complete_reminder(1, datetime(2026, 11, 2, 10, 0))
        self.assertEqual(self.database.get_reminder(1)["status"], "Completed")
        with self.assertRaisesRegex(ValueError, "already completed"):
            self.database.complete_reminder(1, datetime(2026, 11, 2, 10, 1))


if __name__ == "__main__":
    unittest.main()
