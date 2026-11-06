"""SQLite persistence and reminder operations for HealthMate."""

import hashlib
import hmac
import re
import secrets
import sqlite3
from contextlib import contextmanager
from datetime import date, datetime, timedelta
from pathlib import Path

from validation import (
    validate_optional_water_goal,
    validate_profile_name,
    validate_reminder,
    validate_water_goal,
)


DEFAULT_DATABASE = Path(__file__).resolve().parent / "data" / "healthmate.db"
PASSWORD_ITERATIONS = 310_000
USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{2,29}$")


def username_validation_error(username):
    """Return the username validation message, or None when valid."""
    if not isinstance(username, str) or not username.strip():
        return "Username cannot be empty."
    if not USERNAME_PATTERN.fullmatch(username.strip()):
        return (
            "Use 3–30 letters, numbers, dots, underscores, or hyphens; "
            "start with a letter or number."
        )
    return None


def password_validation_error(password):
    """Return the account password validation message, or None when valid."""
    if not isinstance(password, str) or len(password) < 8:
        return "Password must be at least 8 characters."
    if not password.strip():
        return "Password cannot contain only spaces."
    return None


class HealthMateDatabase:
    """Small SQLite data-access layer with parameterized queries."""

    def __init__(self, database_path=DEFAULT_DATABASE):
        self.database_path = Path(database_path)
        self.account_database_path = self.database_path.resolve()
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(str(self.database_path))
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.account_connection = self.connection
        self.initialize()

    @contextmanager
    def _transaction(self, connection=None):
        connection = connection or self.connection
        try:
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise

    def initialize(self):
        """Create app tables and add missing columns without resetting user data."""
        self.connection.execute("PRAGMA foreign_keys = OFF")
        try:
            with self._transaction() as connection:
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS local_account (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL COLLATE NOCASE UNIQUE,
                        password_salt BLOB NOT NULL,
                        password_hash BLOB NOT NULL,
                        created_at TEXT NOT NULL,
                        database_path TEXT NOT NULL
                    )
                    """
                )
                account_schema = connection.execute(
                    "SELECT sql FROM sqlite_master WHERE type = 'table' "
                    "AND name = 'local_account'"
                ).fetchone()["sql"]
                normalized_schema = re.sub(r"\s+", "", account_schema).lower()
                account_columns = {
                    row["name"] for row in connection.execute(
                        "PRAGMA table_info(local_account)"
                    ).fetchall()
                }
                if "check(id=1)" in normalized_schema:
                    path_expression = (
                        "database_path" if "database_path" in account_columns
                        else "?"
                    )
                    insert_values = (
                        "id, username, password_salt, password_hash, created_at, "
                        f"{path_expression}"
                    )
                    if "database_path" in account_columns:
                        connection.execute(
                            """
                            CREATE TABLE local_account_migrated (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT NOT NULL COLLATE NOCASE UNIQUE,
                                password_salt BLOB NOT NULL,
                                password_hash BLOB NOT NULL,
                                created_at TEXT NOT NULL,
                                database_path TEXT NOT NULL
                            )
                            """
                        )
                        connection.execute(
                            "INSERT INTO local_account_migrated "
                            f"({insert_values}) SELECT {insert_values} "
                            "FROM local_account"
                        )
                    else:
                        connection.execute(
                            """
                            CREATE TABLE local_account_migrated (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT NOT NULL COLLATE NOCASE UNIQUE,
                                password_salt BLOB NOT NULL,
                                password_hash BLOB NOT NULL,
                                created_at TEXT NOT NULL,
                                database_path TEXT NOT NULL
                            )
                            """
                        )
                        connection.execute(
                            """
                            INSERT INTO local_account_migrated
                                (id, username, password_salt, password_hash,
                                 created_at, database_path)
                            SELECT id, username, password_salt, password_hash,
                                   created_at, ?
                            FROM local_account
                            """,
                            (str(self.account_database_path),),
                        )
                    connection.execute("DROP TABLE local_account")
                    connection.execute(
                        "ALTER TABLE local_account_migrated RENAME TO local_account"
                    )
                    account_columns.add("database_path")
                elif "database_path" not in account_columns:
                    connection.execute(
                        "ALTER TABLE local_account ADD COLUMN "
                        "database_path TEXT NOT NULL DEFAULT ''"
                    )
                    account_columns.add("database_path")
                connection.execute(
                    "UPDATE local_account SET database_path = ? "
                    "WHERE database_path = ''",
                    (str(self.account_database_path),),
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS reminders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL CHECK(length(trim(title)) BETWEEN 3 AND 60),
                        category TEXT NOT NULL CHECK(category IN
                            ('Water', 'Medicine', 'Exercise', 'Walking', 'Meditation',
                             'Break', 'Other')),
                        reminder_date TEXT NOT NULL DEFAULT '',
                        reminder_time TEXT NOT NULL,
                        description TEXT NOT NULL DEFAULT '',
                        status TEXT NOT NULL DEFAULT 'Active'
                            CHECK(status IN ('Active', 'Completed')),
                        created_at TEXT NOT NULL,
                        snooze_until TEXT
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS activity_history (
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
                    CREATE TABLE IF NOT EXISTS profile (
                        id INTEGER PRIMARY KEY CHECK(id = 1),
                        display_name TEXT NOT NULL DEFAULT '',
                        daily_water_goal INTEGER NOT NULL DEFAULT 0
                            CHECK(daily_water_goal BETWEEN 0 AND 30),
                        theme TEXT NOT NULL DEFAULT 'light'
                            CHECK(theme IN ('light', 'dark'))
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS water_intake (
                        intake_date TEXT PRIMARY KEY,
                        glasses INTEGER NOT NULL DEFAULT 0 CHECK(glasses >= 0),
                        updated_at TEXT NOT NULL
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS achievements (
                        badge_id TEXT PRIMARY KEY,
                        unlocked_at TEXT NOT NULL
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS daily_progress (
                        progress_date TEXT PRIMARY KEY,
                        completed_reminders INTEGER NOT NULL DEFAULT 0,
                        total_reminders INTEGER NOT NULL DEFAULT 0,
                        water_glasses INTEGER NOT NULL DEFAULT 0,
                        water_goal INTEGER NOT NULL DEFAULT 0,
                        daily_goal_met INTEGER NOT NULL DEFAULT 0
                            CHECK(daily_goal_met IN (0, 1))
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS health_streaks (
                        id INTEGER PRIMARY KEY CHECK(id = 1),
                        current_streak INTEGER NOT NULL DEFAULT 0,
                        longest_streak INTEGER NOT NULL DEFAULT 0,
                        total_completed_days INTEGER NOT NULL DEFAULT 0,
                        as_of_date TEXT NOT NULL
                    )
                    """
                )
                connection.execute(
                    "INSERT OR IGNORE INTO profile (id) VALUES (1)"
                )
                columns = {
                    row["name"]
                    for row in connection.execute("PRAGMA table_info(reminders)")
                }
                if "snooze_until" not in columns:
                    connection.execute(
                        "ALTER TABLE reminders ADD COLUMN snooze_until TEXT"
                    )
                reminder_schema = connection.execute(
                    "SELECT sql FROM sqlite_master WHERE type = 'table' "
                    "AND name = 'reminders'"
                ).fetchone()
                if (
                    reminder_schema
                    and "'meditation'" not in reminder_schema["sql"].lower()
                ):
                    connection.execute(
                        """
                        CREATE TABLE reminders_new (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL CHECK(length(trim(title)) BETWEEN 3 AND 60),
                            category TEXT NOT NULL CHECK(category IN
                                ('Water', 'Medicine', 'Exercise', 'Walking', 'Meditation',
                                 'Break', 'Other')),
                            reminder_date TEXT NOT NULL DEFAULT '',
                            reminder_time TEXT NOT NULL,
                            description TEXT NOT NULL DEFAULT '',
                            status TEXT NOT NULL DEFAULT 'Active'
                                CHECK(status IN ('Active', 'Completed')),
                            created_at TEXT NOT NULL,
                            snooze_until TEXT
                        )
                        """
                    )
                    connection.execute(
                        """
                        INSERT INTO reminders_new
                            (id, title, category, reminder_date, reminder_time,
                             description, status, created_at, snooze_until)
                        SELECT id, title, category, reminder_date, reminder_time,
                               description, status, created_at, snooze_until
                        FROM reminders
                        """
                    )
                    connection.execute("DROP TABLE reminders")
                    connection.execute(
                        "ALTER TABLE reminders_new RENAME TO reminders"
                    )
                profile_schema = connection.execute(
                    "SELECT sql FROM sqlite_master WHERE type = 'table' "
                    "AND name = 'profile'"
                ).fetchone()
                if (
                    profile_schema
                    and "between 1 and 30" in profile_schema["sql"].lower()
                ):
                    connection.execute(
                        """
                        CREATE TABLE profile_new (
                            id INTEGER PRIMARY KEY CHECK(id = 1),
                            display_name TEXT NOT NULL DEFAULT '',
                            daily_water_goal INTEGER NOT NULL DEFAULT 0
                                CHECK(daily_water_goal BETWEEN 0 AND 30),
                            theme TEXT NOT NULL DEFAULT 'light'
                                CHECK(theme IN ('light', 'dark'))
                        )
                        """
                    )
                    connection.execute(
                        """
                        INSERT INTO profile_new
                            (id, display_name, daily_water_goal, theme)
                        SELECT id, display_name, daily_water_goal, theme
                        FROM profile
                        """
                    )
                    connection.execute("DROP TABLE profile")
                    connection.execute("ALTER TABLE profile_new RENAME TO profile")
                connection.execute(
                    "CREATE INDEX IF NOT EXISTS idx_history_reminder_time "
                    "ON activity_history(reminder_id, scheduled_time)"
                )
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not initialize the database: {exc}") from exc
        finally:
            self.connection.execute("PRAGMA foreign_keys = ON")

    def account_exists(self):
        try:
            return self.account_connection.execute(
                "SELECT 1 FROM local_account LIMIT 1"
            ).fetchone() is not None
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not check the local account: {exc}") from exc

    def register_user(self, username, password):
        """Create a local account with a separate database for its health data."""
        username_error = username_validation_error(username)
        if username_error:
            raise ValueError(username_error)
        username = username.strip()
        password_error = password_validation_error(password)
        if password_error:
            raise ValueError(password_error)

        salt = secrets.token_bytes(16)
        password_hash = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt, PASSWORD_ITERATIONS
        )
        account_count = self.account_connection.execute(
            "SELECT COUNT(*) FROM local_account"
        ).fetchone()[0]
        if account_count == 0:
            database_path = self.account_database_path
        else:
            username_key = hashlib.sha256(
                username.casefold().encode("utf-8")
            ).hexdigest()
            database_path = (
                self.account_database_path.parent
                / f"{self.account_database_path.stem}_users"
                / f"{username_key}.db"
            )
        try:
            with self._transaction(self.account_connection) as connection:
                connection.execute(
                    """
                    INSERT INTO local_account
                        (username, password_salt, password_hash, created_at,
                         database_path)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        username, salt, password_hash,
                        datetime.now().isoformat(timespec="seconds"),
                        str(database_path),
                    ),
                )
            return username
        except sqlite3.IntegrityError as exc:
            raise ValueError("An account with this username already exists.") from exc
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not create the local account: {exc}") from exc

    def authenticate_user(self, username, password):
        """Return the account username on success, otherwise None."""
        if not isinstance(username, str) or not isinstance(password, str):
            return None
        try:
            account = self.account_connection.execute(
                "SELECT * FROM local_account WHERE username = ?",
                (username.strip(),),
            ).fetchone()
            if account is None:
                return None
            candidate = hashlib.pbkdf2_hmac(
                "sha256",
                password.encode("utf-8"),
                account["password_salt"],
                PASSWORD_ITERATIONS,
            )
            if hmac.compare_digest(candidate, account["password_hash"]):
                return account["username"]
            return None
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not sign in: {exc}") from exc

    def activate_user(self, username):
        """Open the private health-data database belonging to an account."""
        try:
            account = self.account_connection.execute(
                "SELECT database_path FROM local_account WHERE username = ?",
                (username.strip(),),
            ).fetchone()
            if account is None:
                raise ValueError("The local account could not be found.")
            database_path = Path(account["database_path"]).resolve()
            if database_path == self.database_path.resolve():
                return

            if self.account_connection is self.connection:
                self.account_connection = sqlite3.connect(
                    str(self.account_database_path)
                )
                self.account_connection.row_factory = sqlite3.Row
                self.account_connection.execute("PRAGMA foreign_keys = ON")

            self.connection.close()
            self.database_path = database_path
            self.database_path.parent.mkdir(parents=True, exist_ok=True)
            self.connection = sqlite3.connect(str(self.database_path))
            self.connection.row_factory = sqlite3.Row
            self.connection.execute("PRAGMA foreign_keys = ON")
            self.initialize()
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not open this account's health data: {exc}") from exc

    def add_reminder(self, title, category, reminder_date, reminder_time, description=""):
        fields = validate_reminder(
            title, category, reminder_date, reminder_time, description
        )
        created_at = datetime.now().isoformat(timespec="seconds")
        try:
            with self._transaction() as connection:
                duplicate = connection.execute(
                    """
                    SELECT 1 FROM reminders
                    WHERE lower(title) = lower(?) AND category = ?
                      AND reminder_date = ? AND reminder_time = ?
                      AND status = 'Active'
                    LIMIT 1
                    """,
                    (
                        fields["title"], fields["category"], fields["date"],
                        fields["time"],
                    ),
                ).fetchone()
                if duplicate:
                    raise ValueError("An active reminder with these details already exists.")
                cursor = connection.execute(
                    """
                    INSERT INTO reminders
                        (title, category, reminder_date, reminder_time,
                         description, status, created_at)
                    VALUES (?, ?, ?, ?, ?, 'Active', ?)
                    """,
                    (
                        fields["title"],
                        fields["category"],
                        fields["date"],
                        fields["time"],
                        fields["description"],
                        created_at,
                    ),
                )
                return cursor.lastrowid
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not save the reminder: {exc}") from exc

    def update_reminder(self, reminder_id, title, category, reminder_date, reminder_time, description=""):
        fields = validate_reminder(
            title, category, reminder_date, reminder_time, description
        )
        try:
            with self._transaction() as connection:
                duplicate = connection.execute(
                    """
                    SELECT 1 FROM reminders
                    WHERE lower(title) = lower(?) AND category = ?
                      AND reminder_date = ? AND reminder_time = ?
                      AND status = 'Active' AND id != ?
                    LIMIT 1
                    """,
                    (
                        fields["title"], fields["category"], fields["date"],
                        fields["time"], reminder_id,
                    ),
                ).fetchone()
                if duplicate:
                    raise ValueError("An active reminder with these details already exists.")
                cursor = connection.execute(
                    """
                    UPDATE reminders
                    SET title = ?, category = ?, reminder_date = ?,
                        reminder_time = ?, description = ?, snooze_until = NULL
                    WHERE id = ? AND status = 'Active'
                    """,
                    (
                        fields["title"],
                        fields["category"],
                        fields["date"],
                        fields["time"],
                        fields["description"],
                        reminder_id,
                    ),
                )
                if cursor.rowcount == 0:
                    raise ValueError("The selected reminder is no longer active.")
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not update the reminder: {exc}") from exc

    def get_reminders(self, category=None, include_completed=True):
        query = "SELECT * FROM reminders"
        conditions = []
        parameters = []
        if category and category != "All":
            conditions.append("category = ?")
            parameters.append(category)
        if not include_completed:
            conditions.append("status = 'Active'")
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += " ORDER BY CASE status WHEN 'Active' THEN 0 ELSE 1 END, reminder_time, id"
        try:
            return self.connection.execute(query, parameters).fetchall()
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not load reminders: {exc}") from exc

    def get_reminder(self, reminder_id):
        try:
            return self.connection.execute(
                "SELECT * FROM reminders WHERE id = ?", (reminder_id,)
            ).fetchone()
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not load the reminder: {exc}") from exc

    def has_duplicate(self, title, category, reminder_date, reminder_time, exclude_id=None):
        query = """
            SELECT 1 FROM reminders
            WHERE lower(title) = lower(?) AND category = ?
                AND reminder_date = ? AND reminder_time = ? AND status = 'Active'
        """
        parameters = [title.strip(), category, reminder_date, reminder_time]
        if exclude_id is not None:
            query += " AND id != ?"
            parameters.append(exclude_id)
        try:
            return self.connection.execute(query, parameters).fetchone() is not None
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not check for duplicate reminders: {exc}") from exc

    def delete_reminder(self, reminder_id):
        try:
            with self._transaction() as connection:
                cursor = connection.execute(
                    "DELETE FROM reminders WHERE id = ?", (reminder_id,)
                )
                if cursor.rowcount == 0:
                    raise ValueError("The selected reminder could not be found.")
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not delete the reminder: {exc}") from exc

    def complete_reminder(self, reminder_id, now=None):
        now = now or datetime.now()
        timestamp = now.isoformat(timespec="seconds")
        scheduled = now.strftime("%d-%m-%Y %H:%M")
        try:
            with self._transaction() as connection:
                reminder = connection.execute(
                    "SELECT * FROM reminders WHERE id = ?", (reminder_id,)
                ).fetchone()
                if reminder is None or reminder["status"] != "Active":
                    raise ValueError("This reminder is already completed or unavailable.")
                if not reminder["reminder_date"]:
                    done_today = connection.execute(
                        """
                        SELECT 1 FROM activity_history
                        WHERE reminder_id = ? AND status = 'Done'
                          AND substr(scheduled_time, 1, 10) = ?
                        LIMIT 1
                        """,
                        (reminder_id, now.strftime("%d-%m-%Y")),
                    ).fetchone()
                    if done_today:
                        raise ValueError("This reminder is already completed today.")
                cursor = connection.execute(
                    """
                    UPDATE activity_history
                    SET status = 'Done', completion_time = ?
                    WHERE id = (
                        SELECT id FROM activity_history
                        WHERE reminder_id = ? AND status IN ('Notified', 'Snoozed')
                        ORDER BY id DESC LIMIT 1
                    )
                    """,
                    (timestamp, reminder_id),
                )
                if cursor.rowcount == 0:
                    connection.execute(
                        """
                        INSERT INTO activity_history
                            (reminder_id, reminder_title, scheduled_time,
                             completion_time, status)
                        VALUES (?, ?, ?, ?, 'Done')
                        """,
                        (reminder_id, reminder["title"], scheduled, timestamp),
                    )
                if reminder["reminder_date"]:
                    connection.execute(
                        "UPDATE reminders SET status = 'Completed', snooze_until = NULL "
                        "WHERE id = ?",
                        (reminder_id,),
                    )
                else:
                    connection.execute(
                        "UPDATE reminders SET snooze_until = NULL WHERE id = ?",
                        (reminder_id,),
                    )
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not complete the reminder: {exc}") from exc

    def snooze_reminder(self, reminder_id, now=None, minutes=5):
        if minutes not in (5, 10, 15):
            raise ValueError("Choose a snooze interval of 5, 10, or 15 minutes.")
        now = now or datetime.now()
        snooze_until = now.replace(microsecond=0) + timedelta(minutes=minutes)
        scheduled = now.strftime("%d-%m-%Y %H:%M")
        try:
            with self._transaction() as connection:
                reminder = connection.execute(
                    "SELECT * FROM reminders WHERE id = ? AND status = 'Active'",
                    (reminder_id,),
                ).fetchone()
                if reminder is None:
                    raise ValueError("This reminder is no longer active.")
                connection.execute(
                    "UPDATE reminders SET snooze_until = ? WHERE id = ?",
                    (snooze_until.isoformat(timespec="seconds"), reminder_id),
                )
                connection.execute(
                    """
                    INSERT INTO activity_history
                        (reminder_id, reminder_title, scheduled_time,
                         completion_time, status)
                    VALUES (?, ?, ?, NULL, 'Snoozed')
                    """,
                    (reminder_id, reminder["title"], scheduled),
                )
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not snooze the reminder: {exc}") from exc

    def due_reminders(self, now=None):
        now = now or datetime.now()
        today = now.strftime("%d-%m-%Y")
        now_iso = now.isoformat(timespec="seconds")
        try:
            rows = self.connection.execute(
                """
                SELECT r.* FROM reminders AS r
                WHERE r.status = 'Active'
                  AND (r.reminder_date = '' OR r.reminder_date = ?)
                  AND (
                    (r.snooze_until IS NOT NULL AND r.snooze_until <= ?)
                    OR (
                      r.snooze_until IS NULL
                      AND r.reminder_time <= ?
                      AND NOT EXISTS (
                        SELECT 1 FROM activity_history AS h
                        WHERE h.reminder_id = r.id
                          AND substr(h.scheduled_time, 1, 10) = ?
                          AND h.status IN ('Notified', 'Done', 'Snoozed')
                      )
                    )
                  )
                ORDER BY r.reminder_time, r.id
                """,
                (today, now_iso, now.strftime("%H:%M"), today),
            ).fetchall()
            return rows
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not check due reminders: {exc}") from exc

    def mark_notified(self, reminder_id, now=None):
        now = now or datetime.now()
        scheduled = now.strftime("%d-%m-%Y %H:%M")
        try:
            with self._transaction() as connection:
                reminder = connection.execute(
                    "SELECT * FROM reminders WHERE id = ? AND status = 'Active'",
                    (reminder_id,),
                ).fetchone()
                if reminder is None:
                    return False
                connection.execute(
                    """
                    INSERT INTO activity_history
                        (reminder_id, reminder_title, scheduled_time,
                         completion_time, status)
                    VALUES (?, ?, ?, NULL, 'Notified')
                    """,
                    (reminder_id, reminder["title"], scheduled),
                )
                connection.execute(
                    "UPDATE reminders SET snooze_until = NULL WHERE id = ?",
                    (reminder_id,),
                )
                return True
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not record the reminder notification: {exc}") from exc

    def history(self, search="", category="All"):
        query = """
            SELECT h.id, h.reminder_id, h.reminder_title, h.scheduled_time,
                   h.completion_time, h.status, r.category
            FROM activity_history AS h
            LEFT JOIN reminders AS r ON r.id = h.reminder_id
        """
        conditions = []
        parameters = []
        if search.strip():
            conditions.append("h.reminder_title LIKE ?")
            parameters.append(f"%{search.strip()}%")
        if category and category != "All":
            conditions.append("r.category = ?")
            parameters.append(category)
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += " ORDER BY h.id DESC"
        try:
            return self.connection.execute(query, parameters).fetchall()
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not load activity history: {exc}") from exc

    def get_profile(self):
        """Return the persisted display name, water goal, and theme."""
        try:
            row = self.connection.execute(
                """
                SELECT display_name, daily_water_goal, theme
                FROM profile WHERE id = 1
                """
            ).fetchone()
            profile = dict(row) if row else {
                "display_name": "HealthMate", "daily_water_goal": 0,
                "theme": "light",
            }
            if not profile["display_name"]:
                profile["display_name"] = "HealthMate"
            return profile
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not load your profile: {exc}") from exc

    def update_profile(self, display_name, daily_water_goal):
        display_name = validate_profile_name(display_name)
        daily_water_goal = validate_optional_water_goal(daily_water_goal)
        try:
            with self._transaction() as connection:
                connection.execute(
                    """
                    INSERT INTO profile (id, display_name, daily_water_goal, theme)
                    VALUES (1, ?, ?, 'light')
                    ON CONFLICT(id) DO UPDATE SET
                        display_name = excluded.display_name,
                        daily_water_goal = excluded.daily_water_goal
                    """,
                    (display_name, daily_water_goal),
                )
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not save your profile: {exc}") from exc

    def set_theme(self, theme):
        if theme not in ("light", "dark"):
            raise ValueError("Choose either the light or dark theme.")
        try:
            with self._transaction() as connection:
                connection.execute(
                    "UPDATE profile SET theme = ? WHERE id = 1", (theme,)
                )
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not save the selected theme: {exc}") from exc

    def water_glasses(self, on_date=None):
        on_date = on_date or date.today()
        date_key = on_date.isoformat()
        try:
            row = self.connection.execute(
                "SELECT glasses FROM water_intake WHERE intake_date = ?",
                (date_key,),
            ).fetchone()
            return row["glasses"] if row else 0
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not load water intake: {exc}") from exc

    def add_water_glasses(self, amount=1, on_date=None):
        if not isinstance(amount, int) or isinstance(amount, bool) or not 1 <= amount <= 20:
            raise ValueError("Water intake must be between 1 and 20 glasses.")
        on_date = on_date or date.today()
        date_key = on_date.isoformat()
        timestamp = datetime.now().isoformat(timespec="seconds")
        try:
            with self._transaction() as connection:
                connection.execute(
                    """
                    INSERT INTO water_intake (intake_date, glasses, updated_at)
                    VALUES (?, ?, ?)
                    ON CONFLICT(intake_date) DO UPDATE SET
                        glasses = water_intake.glasses + excluded.glasses,
                        updated_at = excluded.updated_at
                    """,
                    (date_key, amount, timestamp),
                )
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not save water intake: {exc}") from exc
        return self.water_glasses(on_date)

    def remove_water_glass(self, on_date=None):
        """Remove one accidentally logged glass without allowing negative totals."""
        on_date = on_date or date.today()
        date_key = on_date.isoformat()
        try:
            with self._transaction() as connection:
                row = connection.execute(
                    "SELECT glasses FROM water_intake WHERE intake_date = ?",
                    (date_key,),
                ).fetchone()
                if row is None or row["glasses"] == 0:
                    raise ValueError("There is no water glass to remove for this date.")
                if row["glasses"] == 1:
                    connection.execute(
                        "DELETE FROM water_intake WHERE intake_date = ?", (date_key,)
                    )
                    return 0
                connection.execute(
                    """
                    UPDATE water_intake SET glasses = glasses - 1, updated_at = ?
                    WHERE intake_date = ?
                    """,
                    (datetime.now().isoformat(timespec="seconds"), date_key),
                )
                return row["glasses"] - 1
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not remove water intake: {exc}") from exc

    def _day_metrics(self, target_date):
        day_key = target_date.strftime("%d-%m-%Y")
        try:
            history = self.connection.execute(
                """
                SELECT reminder_id, status FROM activity_history
                WHERE substr(scheduled_time, 1, 10) = ?
                """,
                (day_key,),
            ).fetchall()
            done_ids = {row["reminder_id"] for row in history
                        if row["status"] == "Done" and row["reminder_id"] is not None}
            reminders = self.connection.execute(
                """
                SELECT id, category FROM reminders
                WHERE reminder_date = '' OR reminder_date = ?
                """,
                (day_key,),
            ).fetchall()
            applicable = {row["id"] for row in reminders}
            exercise_ids = {
                row["id"] for row in reminders
                if row["category"] in ("Exercise", "Walking")
            }
            done_count = len(done_ids & applicable)
            total = len(applicable)
            water = self.water_glasses(target_date)
            goal = self.get_profile()["daily_water_goal"]
            percentage = round(done_count * 100 / total) if total else 0
            metrics = {
                "date": target_date,
                "completed": done_count,
                "total": total,
                "completion_percentage": percentage,
                "water_glasses": water,
                "water_goal": goal,
                "exercise_completed": len(done_ids & exercise_ids),
                "daily_goal_met": goal > 0 and water >= goal and done_count == total,
            }
            with self._transaction() as connection:
                connection.execute(
                    """
                    INSERT INTO daily_progress
                        (progress_date, completed_reminders, total_reminders,
                         water_glasses, water_goal, daily_goal_met)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT(progress_date) DO UPDATE SET
                        completed_reminders = excluded.completed_reminders,
                        total_reminders = excluded.total_reminders,
                        water_glasses = excluded.water_glasses,
                        water_goal = excluded.water_goal,
                        daily_goal_met = excluded.daily_goal_met
                    """,
                    (
                        target_date.isoformat(), done_count, total, water, goal,
                        int(metrics["daily_goal_met"]),
                    ),
                )
            return metrics
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not calculate health activity: {exc}") from exc

    def weekly_report(self, days=7, end_date=None):
        if not isinstance(days, int) or isinstance(days, bool) or not 1 <= days <= 31:
            raise ValueError("Report length must be between 1 and 31 days.")
        end_date = end_date or date.today()
        return [
            self._day_metrics(end_date - timedelta(days=offset))
            for offset in range(days - 1, -1, -1)
        ]

    def health_streak(self, end_date=None):
        """Return the active and longest consecutive daily-goal streak."""
        end_date = end_date or date.today()
        try:
            water_rows = self.connection.execute(
                "SELECT intake_date, glasses FROM water_intake"
            ).fetchall()
            reminders = self.connection.execute(
                "SELECT id, reminder_date FROM reminders"
            ).fetchall()
            done_rows = self.connection.execute(
                """
                SELECT reminder_id, scheduled_time FROM activity_history
                WHERE status = 'Done' AND reminder_id IS NOT NULL
                """
            ).fetchall()
            goal = self.get_profile()["daily_water_goal"]
            done_by_day = {}
            for row in done_rows:
                day = datetime.strptime(
                    row["scheduled_time"][:10], "%d-%m-%Y"
                ).date()
                done_by_day.setdefault(day, set()).add(row["reminder_id"])
        except (sqlite3.Error, ValueError) as exc:
            raise RuntimeError(f"Could not calculate health streak: {exc}") from exc

        if goal == 0:
            streak = {"current": 0, "longest": 0, "total_completed_days": 0}
            self._save_health_streak(end_date, streak)
            return streak

        goal_dates = set()
        for row in water_rows:
            day = date.fromisoformat(row["intake_date"])
            if day > end_date or row["glasses"] < goal:
                continue
            day_key = day.strftime("%d-%m-%Y")
            applicable = {
                reminder["id"] for reminder in reminders
                if not reminder["reminder_date"] or reminder["reminder_date"] == day_key
            }
            if len(applicable - done_by_day.get(day, set())) == 0:
                goal_dates.add(day)

        current = 0
        cursor = end_date
        while cursor in goal_dates:
            current += 1
            cursor -= timedelta(days=1)
        longest = 0
        run = 0
        previous = None
        for day in sorted(goal_dates):
            run = run + 1 if previous and day == previous + timedelta(days=1) else 1
            longest = max(longest, run)
            previous = day
        streak = {
            "current": current,
            "longest": longest,
            "total_completed_days": len(goal_dates),
        }
        self._save_health_streak(end_date, streak)
        return streak

    def _save_health_streak(self, as_of_date, streak):
        try:
            with self._transaction() as connection:
                connection.execute(
                    """
                    INSERT INTO health_streaks
                        (id, current_streak, longest_streak,
                         total_completed_days, as_of_date)
                    VALUES (1, ?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        current_streak = excluded.current_streak,
                        longest_streak = excluded.longest_streak,
                        total_completed_days = excluded.total_completed_days,
                        as_of_date = excluded.as_of_date
                    """,
                    (
                        streak["current"], streak["longest"],
                        streak["total_completed_days"], as_of_date.isoformat(),
                    ),
                )
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not save health streak: {exc}") from exc

    def unlock_achievements(self, on_date=None):
        on_date = on_date or date.today()
        metrics = self._day_metrics(on_date)
        streak = self.health_streak(on_date)
        earned = []
        if metrics["completed"] >= 3:
            earned.append("bronze_badge")
        if metrics["total"] > 0 and metrics["completed"] == metrics["total"]:
            earned.append("gold_badge")
        if metrics["water_goal"] > 0 and metrics["water_glasses"] >= metrics["water_goal"]:
            earned.append("hydration_hero")
        if metrics["exercise_completed"]:
            earned.append("fitness_star")
        if metrics["daily_goal_met"]:
            earned.append("routine_master")
        if streak["current"] >= 7:
            earned.append("seven_day_champion")
        if streak["current"] >= 30:
            earned.append("health_master")
        try:
            with self._transaction() as connection:
                for badge_id in earned:
                    connection.execute(
                        "INSERT OR IGNORE INTO achievements (badge_id, unlocked_at) "
                        "VALUES (?, ?)",
                        (badge_id, datetime.now().isoformat(timespec="seconds")),
                    )
            rows = self.connection.execute(
                "SELECT badge_id, unlocked_at FROM achievements ORDER BY unlocked_at"
            ).fetchall()
            return {row["badge_id"]: row["unlocked_at"] for row in rows}
        except sqlite3.Error as exc:
            raise RuntimeError(f"Could not update health achievements: {exc}") from exc

    def close(self):
        self.connection.close()
        if self.account_connection is not self.connection:
            self.account_connection.close()
