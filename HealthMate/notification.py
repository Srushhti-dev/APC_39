"""Simple, non-blocking Tkinter reminder notifications."""

import tkinter as tk
from tkinter import ttk


class ReminderNotification(tk.Toplevel):
    """Popup with completion and configurable snooze actions."""

    def __init__(self, parent, reminder, on_done, on_snooze):
        super().__init__(parent)
        self.title("HealthMate reminder")
        self.resizable(False, False)
        self.transient(parent)
        self.configure(bg="white")
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        body = ttk.Frame(self, padding=20)
        body.pack(fill="both", expand=True)
        ttk.Label(        body,
        text=(
            "You missed this health routine"
            if reminder.get("is_missed")
            else "It's time for your health routine"
        ),
                  style="Heading.TLabel").pack(anchor="w", pady=(0, 8))
        ttk.Label(body, text=reminder["title"], style="CardTitle.TLabel").pack(anchor="w")
        ttk.Label(
            body,
            text=f"{reminder['category']}  •  Scheduled for {reminder['reminder_time']}",
            style="Muted.TLabel",
        ).pack(anchor="w", pady=(4, 12))
        if reminder["description"]:
            ttk.Label(body, text=reminder["description"], wraplength=320).pack(
                anchor="w", pady=(0, 12)
            )

        buttons = ttk.Frame(body)
        buttons.pack(fill="x")
        ttk.Button(
            buttons, text="Mark as done",
            command=lambda: self._finish(on_done, reminder["id"]),
            style="Accent.TButton",
        ).pack(side="left")
        for minutes in (5, 10, 15):
            ttk.Button(
                buttons,
                text=f"Snooze {minutes} min",
                command=lambda interval=minutes: self._finish(
                    on_snooze, reminder["id"], interval
                ),
            ).pack(side="left", padx=(8, 0))
        self.update_idletasks()
        x = parent.winfo_rootx() + max(20, parent.winfo_width() - self.winfo_width() - 30)
        y = parent.winfo_rooty() + 70
        self.geometry(f"+{x}+{y}")
        self.lift()

    def _finish(self, callback, reminder_id, minutes=None):
        if minutes is None:
            callback(reminder_id)
        else:
            callback(reminder_id, minutes)
        self.destroy()
