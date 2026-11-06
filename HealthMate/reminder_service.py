"""Reminder scheduling and notification state transitions."""

from datetime import datetime


class ReminderService:
    """Checks due reminders without creating background threads."""

    def __init__(self, database):
        self.database = database

    def check_due(self, now=None):
        """Record and return due reminders so each is emitted only once."""
        checked_at = now or datetime.now()
        notifications = []
        for reminder in self.database.due_reminders(checked_at):
            if self.database.mark_notified(reminder["id"], checked_at):
                item = dict(reminder)
                scheduled = datetime.strptime(
                    f"{item['reminder_date'] or checked_at.strftime('%d-%m-%Y')} "
                    f"{item['reminder_time']}",
                    "%d-%m-%Y %H:%M",
                )
                item["is_missed"] = (
                    not item.get("snooze_until")
                    and scheduled < checked_at.replace(second=0, microsecond=0)
                )
                notifications.append(item)
        return notifications
