# HealthMate – Smart Daily Health Reminder System

HealthMate is a local-first Tkinter desktop app for daily health routines.
On first launch, create a local account; later launches require signing in.
It includes reminders, SQLite activity history, input validation, CSV exports,
hydration tracking, achievements, streaks, weekly charts, a calendar, local
preferences, and light/dark themes.

> HealthMate is a personal organizer, not a medical device. Enter only the
> medicine schedule prescribed by your healthcare professional; the app does
> not recommend medicine or dosage. Keep the application open for reminders.

## Features

- **Personalized dashboard:** Profile name, live date/time, total/active/
  completed reminders, upcoming schedules, daily completion progress, quote,
  and hydration progress.
- **Local sign-in:** Sign in to an existing account or create another account
  with validated credentials. Passwords are stored as salted hashes, and each
  account has a separate profile, reminders, and health history.
- **Reminders:** Daily or dated water, medicine, exercise, walking, meditation,
  break, and custom reminders; edit/delete/complete actions; duplicate prevention; search and
  category/status filters. Automatic checks run using Tkinter `after()`.
- **Meditation:** A dedicated reminder page with a generated lotus icon in the
  sidebar; choose your own session time and description. Every sidebar
  destination has its own related icon.
- **Smart notifications:** Popup and system notification sound, missed
  reminder indication, Mark as done, and 5/10/15-minute snooze options.
- **Water tracker:** Optional user-chosen daily goal (1–30 glasses), add/remove
  glass actions, saved daily totals,
  remaining glasses, and a visual progress bar.
- **Health achievements:** Bronze Badge, Gold Badge, Water Champion, Fitness
  Star, Routine Master, Weekly Star, and Health Master unlock automatically.
- **Health streak:** Current, longest, and total completed daily-goal days.
- **Weekly report:** Matplotlib graphs for daily reminder completion and water
  intake, plus exercise and completion statistics. Export daily or weekly CSV.
- **Calendar:** Monthly view with reminder markers and the selected day's
  scheduled reminders and activity history.
- **Profile and theme:** Persisted display name, water goal, and light/dark mode.
- **Settings:** View reminder behavior and the local database location.
- **Activity history:** Search/filter reminder activity and export history CSV.

## Project files

| File | Purpose |
| --- | --- |
| `main.py` | Starts the Tkinter event loop and opens the SQLite database. |
| `gui.py` | Sign-in, dashboard, navigation, forms, calendar, charts, and settings. |
| `ui_icons.py` | Generates cached dashboard and navigation icons using Pillow. |
| `database.py` | SQLite schema, local account, reminders, profile, water, reports, streaks, and achievements. |
| `validation.py` | Shared validation for reminder, profile, time/date, and water-goal inputs. |
| `reminder_service.py` | Polls due reminders and prepares notifications. |
| `notification.py` | Non-blocking notification popup with completion and snooze actions. |
| `history.py` | Exports detailed activity history to CSV. |
| `reports.py` | Exports daily and weekly health summaries to CSV. |
| `test_validation.py` | Reminder and field-validation tests. |
| `test_database.py` | Account validation, persistence, reminder, and scheduler tests. |
| `test_advanced_features.py` | Water, profile, streak, achievements, snooze, duplicate, and report tests. |
| `requirements.txt` | Matplotlib and Pillow for charts and generated icons. |
| `data/healthmate.db` | Created on first launch; contains local app data. |

### SQLite structure

Initialization creates or upgrades these tables without deleting existing data:

- `reminders`: schedule, category (including Walking and Meditation), status,
  description, and snooze time.
- `activity_history`: notification, snooze, completion, and activity records.
- `profile`: display name, daily water goal, and selected theme.
- `water_intake`: one daily glass total per ISO date.
- `daily_progress`: daily completion and water-goal snapshots.
- `health_streaks`: saved current/longest streak and completed-goal-day totals.
- `achievements`: unlocked badge and timestamp.
- `local_account`: usernames, salted password hashes, and private data-file paths.

The database file is local and should not be shared if it contains personal
profile or activity information.

## Install and run on Windows / VS Code

1. Install Python 3.10 or later from [python.org](https://www.python.org/downloads/).
   Include the Tcl/Tk option during installation.
2. Open the project folder in VS Code, then open **Terminal → New Terminal**.
3. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If activation is blocked, use `.venv\Scripts\python.exe` instead.
4. Install chart and icon dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Run the tests and launch the app:

   ```powershell
   python -m unittest -v
   python main.py
   ```

6. On first launch, create a local account. On later launches, sign in to an
   existing account or choose **Create new account**. Each account keeps its
   own profile and health data. Set the display name and water goal under
   **Profile**.

The database and its directory are created automatically. The reminder
scheduler works while HealthMate is open; it does not run as a Windows service
or notify while the app is closed.

## Example output

```text
HealthMate                                      Sunday, 01 November 2026
Welcome, Alex
Total: 6    Active: 4    Completed today: 2    Pending today: 3
Today's reminder progress: 2 of 5 (40%)
Water today: 5 glasses · personal goal: 8 · 3 remaining
Health streak: 3 current days · 7 longest · 12 total goal days
Next reminder: Morning walk · Walking · 09:30
Today's thought: Small steps every day add up to remarkable change.
```

The sample assumes Alex chose a personal water goal of 8 glasses in **Profile**;
the application does not set a default target.

In the weekly report, each day shows reminder completion percentage, glasses
consumed against the water goal, and completed exercise reminders. The chart
plots completion percentage and water intake for the selected week.

## Validation and tests

Run the complete test suite with `python -m unittest -v`. It includes validation
cases for empty/whitespace fields, reminder names, dates, times, categories,
descriptions, profile names, and positive water goals. Database tests cover
duplicate reminders, water persistence, snooze timing, daily streaks,
achievements, and CSV contents.

Important input rules:

- Username: 3–30 letters, numbers, dots, underscores, or hyphens; start with
  a letter or number. Password: at least 8 characters and not only spaces.
- Reminder names: 3–60 characters (medicine names: 2–60).
- Time: strict 24-hour `HH:MM`; date: real `DD-MM-YYYY` date, not in the past.
- Leave a reminder date blank to repeat it daily.
- Daily water goal: whole number from 1 to 30. Each Add glass click adds one.
- Water goal is unset until the user chooses one in **Profile**; HealthMate
  does not prescribe a daily target.
- Duplicate active reminders with the same name/category/date/time are rejected.

## Troubleshooting

| Issue | Resolution |
| --- | --- |
| `py` is not recognized | Reinstall Python with **Add Python to PATH**, or use `python`. |
| `No module named tkinter` | Install a standard Windows Python distribution that includes Tcl/Tk. |
| Weekly report says Matplotlib is missing | Run `python -m pip install -r requirements.txt` in the active environment. |
| No reminder popup appears | Keep HealthMate open and check that the reminder is active and due. |
| Permission error saving database or CSV | Close another application using the file or choose a writable destination. |
| PowerShell blocks environment activation | Use `.venv\Scripts\python.exe` directly. |
