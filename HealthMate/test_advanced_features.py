"""Tests for HealthMate profile, hydration, achievements, and report features."""

import csv
import sqlite3
import tempfile
import unittest
from datetime import date, datetime, timedelta
from pathlib import Path

from database import HealthMateDatabase
from reports import export_activity_report
from reminder_service import ReminderService
from validation import (
    validate_optional_water_goal,
    validate_profile_name,
    validate_water_goal,
)


class AdvancedFeatureTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.database = HealthMateDatabase(Path(self.temp_dir.name) / "healthmate.db")

    def tearDown(self):
        self.database.close()
        self.temp_dir.cleanup()

    def test_profile_and_water_goal_validation(self):
        self.assertEqual(validate_profile_name("  Alex  "), "Alex")
        for value in ("", "  ", "x" * 61):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_profile_name(value)
        self.assertEqual(validate_water_goal("8"), 8)
        for value in ("0", "-1", "2.5", "31", ""):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_water_goal(value)
        self.assertEqual(validate_optional_water_goal(""), 0)
        self.assertEqual(validate_optional_water_goal("4"), 4)

    def test_profile_and_water_intake_persist_by_day(self):
        first_day = date(2026, 4, 1)
        next_day = first_day + timedelta(days=1)
        self.database.update_profile("Alex", 3)
        self.assertEqual(self.database.get_profile()["display_name"], "Alex")
        self.assertEqual(self.database.add_water_glasses(on_date=first_day), 1)
        self.assertEqual(self.database.add_water_glasses(2, first_day), 3)
        self.assertEqual(self.database.water_glasses(first_day), 3)
        self.assertEqual(self.database.water_glasses(next_day), 0)
        for amount in (0, -1, 21, 1.5, True):
            with self.subTest(amount=amount), self.assertRaises(ValueError):
                self.database.add_water_glasses(amount, first_day)

    def test_water_glass_can_be_removed_without_going_negative(self):
        on_day = date(2026, 4, 1)
        with self.assertRaisesRegex(ValueError, "no water glass"):
            self.database.remove_water_glass(on_day)
        self.database.add_water_glasses(2, on_day)
        self.assertEqual(self.database.remove_water_glass(on_day), 1)
        self.assertEqual(self.database.remove_water_glass(on_day), 0)
        self.assertEqual(self.database.water_glasses(on_day), 0)

    def test_duplicate_active_reminders_are_rejected(self):
        self.database.add_reminder("Morning walk", "Exercise", "", "08:00")
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.database.add_reminder("morning walk", "Exercise", "", "08:00")
        self.assertEqual(len(self.database.get_reminders()), 1)

    def test_snooze_interval_retriggers_after_selected_minutes(self):
        reminder_id = self.database.add_reminder(
            "Stretch break", "Break", "", "08:00"
        )
        service = ReminderService(self.database)
        started = datetime(2026, 4, 1, 8, 0)
        self.assertEqual(len(service.check_due(started)), 1)
        self.database.snooze_reminder(reminder_id, started, minutes=10)
        self.assertEqual(service.check_due(started + timedelta(minutes=9)), [])
        self.assertEqual(
            len(service.check_due(started + timedelta(minutes=10))), 1
        )
        with self.assertRaises(ValueError):
            self.database.snooze_reminder(reminder_id, started, minutes=7)

    def test_missed_reminder_is_identified_but_snoozed_alert_is_not(self):
        reminder_id = self.database.add_reminder(
            "Morning stretch", "Exercise", "", "08:00"
        )
        service = ReminderService(self.database)
        started = datetime(2026, 4, 1, 8, 2)
        first = service.check_due(started)[0]
        self.assertTrue(first["is_missed"])
        self.database.snooze_reminder(reminder_id, started, minutes=5)
        snoozed = service.check_due(started + timedelta(minutes=5))[0]
        self.assertFalse(snoozed["is_missed"])

    def test_theme_preference_persists(self):
        self.database.set_theme("dark")
        self.assertEqual(self.database.get_profile()["theme"], "dark")
        with self.assertRaises(ValueError):
            self.database.set_theme("blue")

    def test_profile_loads_without_an_account(self):
        self.assertFalse(self.database.account_exists())
        profile = self.database.get_profile()
        self.assertEqual(profile["display_name"], "HealthMate")
        self.assertEqual(
            set(profile), {"display_name", "daily_water_goal", "theme"}
        )

    def test_existing_profile_schema_migrates_without_losing_preferences(self):
        self.database.close()
        connection = sqlite3.connect(self.database.database_path)
        connection.execute("DROP TABLE profile")
        connection.execute(
            """
            CREATE TABLE profile (
                id INTEGER PRIMARY KEY CHECK(id = 1),
                display_name TEXT NOT NULL DEFAULT '',
                daily_water_goal INTEGER NOT NULL DEFAULT 8
                    CHECK(daily_water_goal BETWEEN 1 AND 30),
                theme TEXT NOT NULL DEFAULT 'light'
            )
            """
        )
        connection.execute("INSERT INTO profile VALUES (1, 'Alex', 6, 'dark')")
        connection.commit()
        connection.close()
        self.database = HealthMateDatabase(self.database.database_path)
        profile = self.database.get_profile()
        self.assertEqual(profile["display_name"], "Alex")
        self.assertEqual(profile["daily_water_goal"], 6)
        self.assertEqual(profile["theme"], "dark")
        self.database.update_profile("Alex", "")
        self.assertEqual(self.database.get_profile()["daily_water_goal"], 0)

    def test_existing_reminders_migrate_to_include_walking_category(self):
        legacy_path = Path(self.temp_dir.name) / "legacy.db"
        connection = sqlite3.connect(legacy_path)
        connection.execute(
            """
            CREATE TABLE reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL CHECK(length(trim(title)) BETWEEN 3 AND 60),
                category TEXT NOT NULL CHECK(category IN
                    ('Water', 'Medicine', 'Exercise', 'Break', 'Other')),
                reminder_date TEXT NOT NULL DEFAULT '',
                reminder_time TEXT NOT NULL,
                description TEXT NOT NULL DEFAULT '',
                status TEXT NOT NULL DEFAULT 'Active'
                    CHECK(status IN ('Active', 'Completed')),
                created_at TEXT NOT NULL
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE activity_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reminder_id INTEGER,
                reminder_title TEXT NOT NULL,
                scheduled_time TEXT NOT NULL,
                completion_time TEXT,
                status TEXT NOT NULL,
                FOREIGN KEY(reminder_id) REFERENCES reminders(id)
                    ON DELETE SET NULL
            )
            """
        )
        connection.execute(
            """
            INSERT INTO reminders
                (id, title, category, reminder_date, reminder_time, created_at)
            VALUES (1, 'Morning walk', 'Exercise', '', '08:00', '2026-04-01T08:00:00')
            """
        )
        connection.execute(
            """
            INSERT INTO activity_history
                (reminder_id, reminder_title, scheduled_time, status)
            VALUES (1, 'Morning walk', '01-04-2026 08:00', 'Notified')
            """
        )
        connection.commit()
        connection.close()

        legacy_database = HealthMateDatabase(legacy_path)
        try:
            self.assertEqual(legacy_database.get_reminder(1)["title"], "Morning walk")
            self.assertEqual(len(legacy_database.history()), 1)
            legacy_database.add_reminder("Park walk", "Walking", "", "09:00")
            self.assertEqual(legacy_database.get_reminder(2)["category"], "Walking")
            legacy_database.add_reminder(
                "Evening meditation", "Meditation", "", "20:00"
            )
            self.assertEqual(
                legacy_database.get_reminder(3)["category"], "Meditation"
            )
            self.assertEqual(
                legacy_database.connection.execute(
                    "PRAGMA foreign_key_check"
                ).fetchall(),
                [],
            )
        finally:
            legacy_database.close()

    def test_daily_streak_and_achievement_unlock(self):
        self.database.update_profile("Alex", 1)
        self.database.add_reminder("Daily walk", "Exercise", "", "08:00")
        start = date(2026, 4, 1)
        for offset in range(7):
            day = start + timedelta(days=offset)
            self.database.add_water_glasses(on_date=day)
            self.database.complete_reminder(
                1, datetime.combine(day, datetime.min.time()).replace(hour=8)
            )
        streak = self.database.health_streak(start + timedelta(days=6))
        self.assertEqual(
            streak, {"current": 7, "longest": 7, "total_completed_days": 7}
        )
        badges = self.database.unlock_achievements(start + timedelta(days=6))
        self.assertIn("hydration_hero", badges)
        self.assertIn("fitness_star", badges)
        self.assertIn("routine_master", badges)
        self.assertIn("seven_day_champion", badges)

    def test_reward_badges_for_three_and_all_daily_reminders(self):
        self.database.update_profile("Alex", "")
        for title in ("Walk", "Stretch", "Workout"):
            self.database.add_reminder(title, "Exercise", "", "08:00")
        for reminder_id in (1, 2, 3):
            self.database.complete_reminder(
                reminder_id, datetime(2026, 4, 1, 8, reminder_id)
            )
        badges = self.database.unlock_achievements(date(2026, 4, 1))
        self.assertIn("bronze_badge", badges)
        self.assertIn("gold_badge", badges)

    def test_health_master_unlocks_after_thirty_daily_goals(self):
        self.database.update_profile("Alex", 1)
        self.database.add_reminder("Daily walk", "Walking", "", "08:00")
        first_day = date(2026, 4, 1)
        for offset in range(30):
            day = first_day + timedelta(days=offset)
            self.database.add_water_glasses(on_date=day)
            self.database.complete_reminder(
                1, datetime.combine(day, datetime.min.time()).replace(hour=8)
            )
        streak = self.database.health_streak(first_day + timedelta(days=29))
        self.assertEqual(streak["current"], 30)
        self.assertEqual(streak["total_completed_days"], 30)
        self.assertIn(
            "health_master",
            self.database.unlock_achievements(first_day + timedelta(days=29)),
        )

    def test_unset_water_goal_is_not_counted_as_a_streak(self):
        self.assertEqual(
            self.database.health_streak(),
            {"current": 0, "longest": 0, "total_completed_days": 0},
        )
        stored = self.database.connection.execute(
            "SELECT current_streak, longest_streak, total_completed_days "
            "FROM health_streaks WHERE id = 1"
        ).fetchone()
        self.assertEqual(tuple(stored), (0, 0, 0))

    def test_weekly_report_and_csv_export(self):
        today = date.today()
        self.database.update_profile("Alex", 2)
        self.database.add_reminder("Morning walk", "Exercise", "", "08:00")
        self.database.add_water_glasses(2, today)
        self.database.complete_reminder(
            1, datetime.combine(today, datetime.min.time()).replace(hour=8)
        )
        summary = self.database.weekly_report(days=1)[0]
        self.assertEqual(summary["completed"], 1)
        self.assertEqual(summary["water_glasses"], 2)
        self.assertEqual(summary["completion_percentage"], 100)
        stored_progress = self.database.connection.execute(
            "SELECT completed_reminders, water_glasses, daily_goal_met "
            "FROM daily_progress WHERE progress_date = ?",
            (today.isoformat(),),
        ).fetchone()
        self.assertEqual(tuple(stored_progress), (1, 2, 1))
        destination = Path(self.temp_dir.name) / "reports" / "daily.csv"
        export_activity_report(self.database, destination, days=1)
        with destination.open(encoding="utf-8-sig", newline="") as csv_file:
            rows = list(csv.DictReader(csv_file))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["Completed reminders"], "1")
        with self.assertRaises(ValueError):
            export_activity_report(self.database, destination, days=2)


if __name__ == "__main__":
    unittest.main()
