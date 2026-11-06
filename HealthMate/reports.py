"""Health activity report exports."""

import csv
from pathlib import Path


def export_activity_report(database, destination, days=1):
    """Export a one-day or weekly summary to a UTF-8 CSV file."""
    output_path = Path(destination)
    if days not in (1, 7):
        raise ValueError("Choose a daily (1-day) or weekly (7-day) report.")
    rows = database.weekly_report(days=days)
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", newline="", encoding="utf-8-sig") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(
                [
                    "Date",
                    "Completed reminders",
                    "Scheduled reminders",
                    "Completion percentage",
                    "Water glasses",
                    "Water goal",
                    "Completed exercise reminders",
                ]
            )
            for row in rows:
                writer.writerow(
                    [
                        row["date"].isoformat(),
                        row["completed"],
                        row["total"],
                        row["completion_percentage"],
                        row["water_glasses"],
                        row["water_goal"],
                        row["exercise_completed"],
                    ]
                )
        return output_path
    except (OSError, csv.Error) as exc:
        raise RuntimeError(f"Could not export the activity report: {exc}") from exc
