"""Activity-history export helpers."""

import csv
from pathlib import Path


def export_history(database, destination):
    """Write all activity-history rows to a UTF-8 CSV file."""
    output_path = Path(destination)
    rows = database.history()
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", newline="", encoding="utf-8-sig") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(
                [
                    "ID",
                    "Reminder ID",
                    "Reminder",
                    "Scheduled time",
                    "Completion time",
                    "Status",
                    "Category",
                ]
            )
            writer.writerows(rows)
        return output_path
    except (OSError, csv.Error) as exc:
        raise RuntimeError(f"Could not export activity history: {exc}") from exc