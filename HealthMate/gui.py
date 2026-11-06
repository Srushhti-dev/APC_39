"""Tkinter user interface for HealthMate."""

import calendar
import tkinter as tk
from datetime import date, datetime, timedelta
from tkinter import filedialog, messagebox, ttk

from database import password_validation_error, username_validation_error
from history import export_history
from notification import ReminderNotification
from reports import export_activity_report
from reminder_service import ReminderService
from ui_icons import IconFactory
from validation import (
    ALLOWED_CATEGORIES,
    validate_medicine,
    validate_optional_water_goal,
    validate_profile_name,
    validate_reminder,
    validate_water_goal,
)


GREEN = "#197A55"
DARK_GREEN = "#125C40"
LIGHT_GREEN = "#E8F4EE"
BACKGROUND = "#F4F7F5"
TEXT = "#20342A"
MUTED = "#718078"
WHITE = "#FFFFFF"


class HealthMateApp:
    """Application window, navigation, forms, and reminder polling."""

    PAGES = [
        ("Dashboard", "Dashboard"),
        ("Water Tracker", "WaterTracker"),
        ("Water Reminder", "Water"),
        ("Medicine Reminder", "Medicine"),
        ("Exercise Reminder", "Exercise"),
        ("Meditation", "Meditation"),
        ("Custom Reminder", "Custom"),
        ("Manage Reminders", "Manage"),
        ("Activity History", "History"),
        ("Weekly Health Report", "Report"),
        ("Calendar", "Calendar"),
        ("Achievements", "Achievements"),
        ("Profile", "Profile"),
        ("Settings", "Settings"),
    ]

    def __init__(self, root, database):
        self.root = root
        self.database = database
        self.reminder_service = ReminderService(database)
        self.running = True
        self.current_page = "Dashboard"
        self.page_body = None
        self.active_notifications = {}
        self.history_search = None
        self.history_category = None
        self.clock_callback = None
        self.reminder_callback = None
        self.topbar_name = None
        self.account_username = None
        self.calendar_month = date.today().replace(day=1)
        self.calendar_selected = date.today()
        self.theme = self.database.get_profile()["theme"]
        self.icons = IconFactory()

        self.root.title("HealthMate | Daily Health Reminders")
        self.root.geometry("500x600")
        self.root.minsize(440, 500)
        self.root.configure(bg=BACKGROUND)
        self._configure_styles()
        self._show_login()

    def _show_login(self, create_account=None):
        for child in self.root.winfo_children():
            child.destroy()

        has_accounts = self.database.account_exists()
        creating_account = (
            not has_accounts if create_account is None else create_account
        )
        self.root.geometry("500x600")
        self.root.minsize(440, 500)
        outer = ttk.Frame(self.root, padding=30)
        outer.pack(fill="both", expand=True)
        outer.rowconfigure(0, weight=1)
        outer.columnconfigure(0, weight=1)

        card = self._card(outer, padding=30)
        card.grid(row=0, column=0, sticky="")
        ttk.Label(
            card, text="HealthMate", style="CardTitle.TLabel",
            font=("Segoe UI Semibold", 23),
        ).pack(anchor="w")
        ttk.Label(
            card,
            text=(
                "Create your local account to get started."
                if creating_account else "Sign in to continue to your health dashboard."
            ),
            style="Card.TLabel",
            wraplength=320,
        ).pack(anchor="w", pady=(5, 22))

        ttk.Label(card, text="Username", style="Card.TLabel").pack(anchor="w")
        username_entry = ttk.Entry(card, width=38)
        username_entry.pack(fill="x", pady=(5, 14))

        ttk.Label(card, text="Password", style="Card.TLabel").pack(anchor="w")
        password_entry = ttk.Entry(card, show="*", width=38)
        password_entry.pack(fill="x", pady=(5, 14))

        confirmation_entry = None
        if creating_account:
            ttk.Label(
                card, text="Confirm password", style="Card.TLabel"
            ).pack(anchor="w")
            confirmation_entry = ttk.Entry(card, show="*", width=38)
            confirmation_entry.pack(fill="x", pady=(5, 14))

        error_label = ttk.Label(
            card, text="", style="Card.TLabel", wraplength=320,
        )
        error_label.configure(foreground="#B42318")
        error_label.pack(anchor="w", pady=(0, 10))

        submit = lambda _event=None: self._submit_login(
            username_entry, password_entry, confirmation_entry,
            creating_account, error_label,
        )
        ttk.Button(
            card,
            text="Create account" if creating_account else "Sign in",
            style="Accent.TButton",
            command=submit,
        ).pack(fill="x")
        password_entry.bind("<Return>", submit)
        if confirmation_entry is not None:
            confirmation_entry.bind("<Return>", submit)
        if creating_account:
            ttk.Label(
                card,
                text=(
                    "Username: 3–30 letters, numbers, dots, underscores, or hyphens. "
                    "Password: at least 8 characters."
                ),
                style="Muted.TLabel",
                wraplength=320,
            ).pack(anchor="w", pady=(14, 0))
        if has_accounts:
            ttk.Button(
                card,
                text="Sign in instead" if creating_account else "Create new account",
                command=lambda: self._show_login(not creating_account),
            ).pack(fill="x", pady=(10, 0))
        username_entry.focus_set()

    def _submit_login(
        self, username_entry, password_entry, confirmation_entry,
        creating_account, error_label,
    ):
        username = username_entry.get()
        password = password_entry.get()

        username_error = username_validation_error(username)
        if username_error:
            error_label.configure(text=username_error)
            return
        if creating_account:
            password_error = password_validation_error(password)
            if password_error:
                error_label.configure(text=password_error)
                return
            if password != confirmation_entry.get():
                error_label.configure(text="Passwords do not match.")
                return
        elif not password:
            error_label.configure(text="Password cannot be empty.")
            return

        try:
            if creating_account:
                self.account_username = self.database.register_user(username, password)
            else:
                self.account_username = self.database.authenticate_user(username, password)
                if self.account_username is None:
                    error_label.configure(text="Incorrect username or password.")
                    return
            self.database.activate_user(self.account_username)
            self._open_application()
        except (ValueError, RuntimeError) as exc:
            error_label.configure(text=str(exc))

    def _open_application(self):
        for child in self.root.winfo_children():
            child.destroy()
        self.theme = self.database.get_profile()["theme"]
        self._configure_styles()
        self.root.geometry("1180x800")
        self.root.minsize(760, 600)
        self._build_shell()
        self.show_page("Dashboard")
        self._update_clock()
        self._check_reminders()

    def _cancel_background_callbacks(self):
        for callback in (self.clock_callback, self.reminder_callback):
            if callback is not None:
                try:
                    self.root.after_cancel(callback)
                except tk.TclError:
                    pass
        self.clock_callback = None
        self.reminder_callback = None

    def _configure_styles(self):
        palette = self._palette()
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure(".", font=("Segoe UI", 10), foreground=palette["text"])
        style.configure("TFrame", background=palette["background"])
        style.configure("White.TFrame", background=palette["card"])
        style.configure("Sidebar.TFrame", background=DARK_GREEN)
        style.configure(
            "TLabel", background=palette["background"], foreground=palette["text"]
        )
        style.configure("Sidebar.TLabel", background=DARK_GREEN, foreground=WHITE)
        style.configure(
            "Muted.TLabel", foreground=palette["muted"],
            background=palette["background"],
        )
        style.configure("Card.TLabel", background=palette["card"], foreground=palette["text"])
        style.configure(
            "Heading.TLabel", font=("Segoe UI Semibold", 20), foreground=palette["text"],
            background=palette["background"],
        )
        style.configure(
            "Subheading.TLabel", font=("Segoe UI Semibold", 13),
            foreground=palette["text"], background=palette["background"],
        )
        style.configure(
            "CardTitle.TLabel", font=("Segoe UI Semibold", 14),
            background=palette["card"], foreground=palette["text"],
        )
        style.configure(
            "Metric.TLabel", font=("Segoe UI Semibold", 24), foreground=GREEN,
            background=palette["card"],
        )
        style.configure(
            "Nav.TButton", background=DARK_GREEN, foreground="#E9F5EE",
            padding=(13, 10), anchor="w", borderwidth=0,
        )
        style.map(
            "Nav.TButton",
            background=[("active", GREEN), ("pressed", GREEN)],
            foreground=[("active", WHITE)],
        )
        style.configure(
            "Accent.TButton", background=GREEN, foreground=WHITE,
            padding=(13, 8), borderwidth=0,
        )
        style.map(
            "Accent.TButton",
            background=[("active", DARK_GREEN), ("pressed", DARK_GREEN)],
        )
        style.configure(
            "TButton", padding=(10, 7),
            background=palette["header"], foreground=palette["text"],
        )
        style.configure("TEntry", padding=7)
        style.configure("TCombobox", padding=6)
        style.configure(
            "Treeview", background=palette["card"],
            fieldbackground=palette["card"], foreground=palette["text"], rowheight=31,
            borderwidth=0,
        )
        style.configure(
            "Treeview.Heading", font=("Segoe UI Semibold", 9),
            background=palette["header"], foreground=palette["text"], padding=8,
        )
        style.configure(
            "TProgressbar", troughcolor=palette["header"], background=GREEN,
            bordercolor=palette["header"],
        )
        style.configure("TEntry", fieldbackground=palette["card"], foreground=palette["text"])
        style.configure("TCombobox", fieldbackground=palette["card"], foreground=palette["text"])
        self.root.configure(bg=palette["background"])

    def _palette(self):
        if self.theme == "dark":
            return {
                "background": "#18231E", "card": "#24332B",
                "text": "#E8F0EB", "muted": "#B0C0B6", "header": "#31443A",
            }
        return {
            "background": BACKGROUND, "card": WHITE, "text": TEXT,
            "muted": MUTED, "header": LIGHT_GREEN,
        }

    def _build_shell(self):
        self.shell = ttk.Frame(self.root)
        self.shell.pack(fill="both", expand=True)
        self.sidebar = ttk.Frame(self.shell, style="Sidebar.TFrame", width=230)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)
        ttk.Label(
            self.sidebar, text="HealthMate", style="Sidebar.TLabel",
            font=("Segoe UI Semibold", 21),
        ).pack(anchor="w", padx=22, pady=(27, 2))
        ttk.Label(
            self.sidebar, text="Small habits. Better days.",
            style="Sidebar.TLabel", font=("Segoe UI", 9),
        ).pack(anchor="w", padx=23, pady=(0, 27))

        self.nav_buttons = {}
        for label, page in self.PAGES:
            icon = self.icons.navigation(page)
            button = ttk.Button(
                self.sidebar,
                text=f"  {label}",
                image=icon,
                compound="left",
                style="Nav.TButton",
                command=lambda selected=page: self.show_page(selected),
            )
            button.image = icon
            button.pack(fill="x", padx=10, pady=2)
            self.nav_buttons[page] = button

        ttk.Label(
            self.sidebar,
            text="Keep this app open\nfor reminders to appear.",
            style="Sidebar.TLabel",
            font=("Segoe UI", 9),
            justify="left",
        ).pack(side="bottom", anchor="w", padx=22, pady=20)

        self.main_area = ttk.Frame(self.shell, padding=(28, 20, 28, 24))
        self.main_area.pack(side="left", fill="both", expand=True)
        self.topbar = ttk.Frame(self.main_area)
        self.topbar.pack(fill="x", pady=(0, 18))
        self.page_heading = ttk.Label(self.topbar, text="", style="Heading.TLabel")
        self.page_heading.pack(side="left")
        self.clock_label = ttk.Label(self.topbar, text="", style="Muted.TLabel")
        self.clock_label.pack(side="right", pady=(7, 0))
        self.topbar_name = ttk.Label(
            self.topbar, text=self.database.get_profile()["display_name"],
            style="Muted.TLabel",
        )
        self.topbar_name.pack(side="right", padx=(0, 12))
        self.theme_button = ttk.Button(
            self.topbar, text="☾ Dark mode" if self.theme == "light" else "☀ Light mode",
            command=self._toggle_theme,
        )
        self.theme_button.pack(side="right", padx=(0, 10))
        self.page_body = ttk.Frame(self.main_area)
        self.page_body.pack(fill="both", expand=True)

    def show_page(self, page):
        self.current_page = page
        for nav_page, button in self.nav_buttons.items():
            button.state(["pressed"] if nav_page == page else ["!pressed"])
        self.page_heading.configure(
            text=next((label for label, key in self.PAGES if key == page), page)
        )
        for child in self.page_body.winfo_children():
            child.destroy()

        renderers = {
            "Dashboard": self._render_dashboard,
            "WaterTracker": self._render_water_tracker,
            "Water": lambda: self._render_reminder_page("Water"),
            "Medicine": lambda: self._render_reminder_page("Medicine"),
            "Exercise": lambda: self._render_reminder_page("Exercise"),
            "Meditation": lambda: self._render_reminder_page("Meditation"),
            "Custom": lambda: self._render_reminder_page("Other", custom=True),
            "Manage": self._render_manage,
            "History": self._render_history,
            "Report": self._render_weekly_report,
            "Calendar": self._render_calendar,
            "Achievements": self._render_achievements,
            "Profile": self._render_profile,
            "Settings": self._render_settings,
        }
        try:
            renderers[page]()
        except (RuntimeError, tk.TclError) as exc:
            messagebox.showerror("Could not display page", str(exc), parent=self.root)

    def _toggle_theme(self):
        try:
            self.theme = "dark" if self.theme == "light" else "light"
            self.database.set_theme(self.theme)
            self._configure_styles()
            self.theme_button.configure(
                text="☾ Dark mode" if self.theme == "light" else "☀ Light mode"
            )
            self.show_page(self.current_page)
        except (RuntimeError, ValueError) as exc:
            messagebox.showerror("Theme could not be changed", str(exc), parent=self.root)

    def _update_clock(self):
        if self.running and self.root.winfo_exists():
            self.clock_label.configure(
                text=datetime.now().strftime("%A, %d %B %Y  |  %I:%M:%S %p")
            )
            self.clock_callback = self.root.after(1000, self._update_clock)

    def _check_reminders(self):
        if not self.running or not self.root.winfo_exists():
            return
        try:
            for reminder in self.reminder_service.check_due():
                self._show_notification(reminder)
        except (RuntimeError, ValueError) as exc:
            messagebox.showerror("Reminder check failed", str(exc), parent=self.root)
        self.reminder_callback = self.root.after(15000, self._check_reminders)

    def _show_notification(self, reminder):
        try:
            import winsound
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
        except ImportError:
            self.root.bell()
        popup = ReminderNotification(
            self.root,
            reminder,
            self._complete_reminder,
            self._snooze_reminder,
        )
        self.active_notifications[reminder["id"]] = popup
        popup.bind(
            "<Destroy>",
            lambda _event, reminder_id=reminder["id"]:
                self.active_notifications.pop(reminder_id, None),
        )

    def _card(self, parent, padding=18):
        return ttk.Frame(parent, style="White.TFrame", padding=padding)

    def _render_dashboard(self):
        self.database.unlock_achievements()
        profile = self.database.get_profile()
        ttk.Label(
            self.page_body, text=f"Welcome, {self.account_username}",
            font=("Segoe UI Semibold", 16),
        ).pack(anchor="w")
        ttk.Label(
            self.page_body,
            text="Build a healthier day, one reminder at a time.",
            style="Muted.TLabel",
        ).pack(anchor="w", pady=(3, 17))

        reminders = self.database.get_reminders()
        active = [item for item in reminders if item["status"] == "Active"]
        today_metrics = self.database.weekly_report(days=1)[0]
        today_done = today_metrics["completed"]
        progress = today_metrics["completion_percentage"]

        cards = ttk.Frame(self.page_body)
        cards.pack(fill="x")
        metrics = [
            ("Total reminders", len(reminders), "T"),
            ("Active", len(active), "A"),
            ("Completed today", today_done, "C"),
            ("Pending today", max(0, today_metrics["total"] - today_done), "P"),
        ]
        for label, value, symbol in metrics:
            card = self._card(cards)
            card.pack(side="left", fill="x", expand=True, padx=(0, 12))
            icon_label = ttk.Label(
                card, image=self.icons.create(symbol), style="Card.TLabel"
            )
            icon_label.image = self.icons.create(symbol)
            icon_label.pack(anchor="w", pady=(0, 6))
            ttk.Label(card, text=label, style="Muted.TLabel").pack(anchor="w")
            ttk.Label(card, text=str(value), style="Metric.TLabel").pack(
                anchor="w", pady=(7, 0)
            )

        streak = self.database.health_streak()
        streak_card = self._card(self.page_body, padding=12)
        streak_card.pack(fill="x", pady=(10, 0))
        ttk.Label(
            streak_card,
            text=(
                f"Health streak  ·  {streak['current']} current days  ·  "
                f"{streak['longest']} longest  ·  "
                f"{streak['total_completed_days']} total goal days"
            ),
            style="CardTitle.TLabel",
        ).pack(anchor="w")

        habit_row = ttk.Frame(self.page_body)
        habit_row.pack(fill="x", pady=12)
        progress_card = self._card(habit_row)
        progress_card.pack(side="left", fill="both", expand=True, padx=(0, 10))
        ttk.Label(progress_card, text="Today's progress", style="CardTitle.TLabel").pack(
            anchor="w"
        )
        ttk.Label(
            progress_card,
            text=f"{today_done} of {today_metrics['total']} reminders completed today",
            style="Muted.TLabel",
        ).pack(anchor="w", pady=(4, 9))
        progress_bar = ttk.Progressbar(
            progress_card, maximum=100, value=progress, mode="determinate"
        )
        progress_bar.pack(fill="x")
        ttk.Label(
            progress_card, text=f"{progress}% of today's reminders completed",
            style="Muted.TLabel",
        ).pack(anchor="e", pady=(6, 0))

        self._render_water_card(habit_row, compact=True)
        quote_card = self._card(self.page_body, padding=12)
        quote_card.pack(fill="x", pady=(0, 12))
        quotes = (
            "Small steps every day add up to remarkable change.",
            "Take care of your body. It is the only place you have to live.",
            "A little progress each day builds a healthier you.",
            "Make time for your health today; it will thank you tomorrow.",
            "Consistency is a kind of self-care.",
            "Rest, hydrate, move, and begin again.",
            "Your health is an investment, not an expense.",
        )
        quote = quotes[date.today().toordinal() % len(quotes)]
        ttk.Label(
            quote_card, text=f"Today's thought  ·  “{quote}”",
            style="Card.TLabel", wraplength=800,
        ).pack(anchor="w")

        upcoming_card = self._card(self.page_body)
        upcoming_card.pack(fill="both", expand=True)
        upcoming = self._upcoming(active)
        next_text = (
            f"Next reminder  ·  {upcoming[0][0]['title']} at "
            f"{upcoming[0][1].strftime('%a, %d %b %H:%M')}"
            if upcoming else "Upcoming reminders"
        )
        ttk.Label(upcoming_card, text=next_text, style="CardTitle.TLabel").pack(
            anchor="w", pady=(0, 10)
        )
        if not upcoming:
            ttk.Label(
                upcoming_card, text="No active reminders yet. Add one to get started.",
                style="Muted.TLabel",
            ).pack(anchor="w", pady=12)
        else:
            for reminder, due in upcoming[:6]:
                row = ttk.Frame(upcoming_card, style="White.TFrame")
                row.pack(fill="x", pady=5)
                ttk.Label(row, text=reminder["title"], style="Card.TLabel").pack(
                    side="left"
                )
                ttk.Label(
                    row,
                    text=f"{reminder['category']}  ·  {due.strftime('%a, %d %b at %H:%M')}",
                    style="Muted.TLabel",
                ).pack(side="right")

    def _render_water_card(self, parent, compact=False):
        card = self._card(parent)
        if compact:
            card.pack(side="left", fill="both", expand=True)
        else:
            card.pack(fill="x", pady=(0, 14))
        profile = self.database.get_profile()
        goal = profile["daily_water_goal"]
        glasses = self.database.water_glasses()
        ttk.Label(card, text="Water intake today", style="CardTitle.TLabel").pack(
            anchor="w"
        )
        if goal:
            remaining = max(0, goal - glasses)
            ttk.Label(
                card, text=f"{glasses} / {goal} glasses  ·  {remaining} remaining",
                style="Muted.TLabel",
            ).pack(anchor="w", pady=(5, 6))
            ttk.Progressbar(
                card, maximum=goal, value=min(glasses, goal), mode="determinate"
            ).pack(fill="x")
        else:
            ttk.Label(
                card, text=f"{glasses} glasses logged · Set your own goal in Profile.",
                style="Muted.TLabel",
            ).pack(anchor="w", pady=(5, 6))
        actions = ttk.Frame(card, style="White.TFrame")
        actions.pack(fill="x", pady=(8, 0))
        ttk.Button(
            actions, text="Add glass", style="Accent.TButton", command=self._add_glass,
        ).pack(side="right")
        ttk.Button(
            actions, text="Remove glass", command=self._remove_glass,
        ).pack(side="right", padx=(0, 8))

    def _add_glass(self):
        try:
            goal = self.database.get_profile()["daily_water_goal"]
            previous = self.database.water_glasses()
            total = self.database.add_water_glasses()
            badges = self.database.unlock_achievements()
            if goal > 0 and previous < goal <= total and "hydration_hero" in badges:
                messagebox.showinfo(
                    "Water goal reached!",
                    "Congratulations! You reached your personal water goal today.",
                    parent=self.root,
                )
            self._refresh_page()
        except (RuntimeError, ValueError) as exc:
            messagebox.showerror(
                "Water intake could not be saved", str(exc), parent=self.root
            )

    def _remove_glass(self):
        try:
            self.database.remove_water_glass()
            self._refresh_page()
        except (RuntimeError, ValueError) as exc:
            messagebox.showerror(
                "Water intake could not be changed", str(exc), parent=self.root
            )

    def _render_water_tracker(self):
        ttk.Label(
            self.page_body,
            text="Track each glass and work toward the daily goal in your profile.",
            style="Muted.TLabel",
        ).pack(anchor="w", pady=(0, 14))
        self._render_water_card(self.page_body)
        ttk.Label(
            self.page_body,
            text="Your daily total is saved locally in SQLite and resets automatically each day.",
            style="Muted.TLabel", wraplength=760,
        ).pack(anchor="w")



    @staticmethod
    def _upcoming(active):
        now = datetime.now()
        due_items = []
        for reminder in active:
            if reminder["reminder_date"]:
                due_date = datetime.strptime(reminder["reminder_date"], "%d-%m-%Y").date()
                due = datetime.combine(
                    due_date, datetime.strptime(reminder["reminder_time"], "%H:%M").time()
                )
                if due < now:
                    continue
            else:
                due = datetime.combine(
                    now.date(), datetime.strptime(reminder["reminder_time"], "%H:%M").time()
                )
                if due < now:
                    due += timedelta(days=1)
            due_items.append((reminder, due))
        return sorted(due_items, key=lambda item: item[1])

    def _render_reminder_page(self, category, custom=False):
        title = "Create a reminder"
        intro = {
            "Water": "Stay hydrated with a gentle reminder at the time you choose.",
            "Medicine": (
                "Enter the schedule prescribed by your healthcare professional. "
                "HealthMate does not recommend medicines or dosages."
            ),
            "Exercise": "Schedule a walk, workout, stretch, or other movement break.",
            "Meditation": (
                "Make space for a mindful pause. Set your own time and session length."
            ),
            "Other": "Add a one-time or repeating reminder for your daily routine.",
        }[category]
        ttk.Label(self.page_body, text=intro, style="Muted.TLabel", wraplength=800).pack(
            anchor="w", pady=(0, 14)
        )
        self._build_reminder_form(
            self.page_body, category, title, custom=custom, on_saved=self._refresh_page
        )
        list_card = self._card(self.page_body, padding=15)
        list_card.pack(fill="both", expand=True, pady=(16, 0))
        ttk.Label(
            list_card, text=f"{category} reminders", style="CardTitle.TLabel"
        ).pack(anchor="w", pady=(0, 8))
        rows = self.database.get_reminders(
            category=category, include_completed=False
        )
        if not rows:
            ttk.Label(list_card, text="No reminders in this category yet.",
                      style="Muted.TLabel").pack(anchor="w", pady=12)
            return
        self._create_tree(
            list_card,
            rows,
            columns=("title", "date", "time", "status"),
            headings=("Reminder", "Date", "Time", "Status"),
            height=5,
        )

    def _build_reminder_form(self, parent, category, heading, custom=False,
                             existing=None, on_saved=None, popup=None):
        form = self._card(parent)
        form.pack(fill="x")
        ttk.Label(form, text=heading, style="CardTitle.TLabel").grid(
            row=0, column=0, columnspan=4, sticky="w", pady=(0, 12)
        )
        initial = dict(existing) if existing is not None else {}
        ttk.Label(form, text="Reminder name").grid(row=1, column=0, sticky="w")
        title_entry = ttk.Entry(form)
        title_entry.grid(row=2, column=0, sticky="ew", padx=(0, 12), pady=(4, 10))
        title_entry.insert(0, initial.get("title", ""))

        ttk.Label(form, text="Category").grid(row=1, column=1, sticky="w")
        category_var = tk.StringVar(value=initial.get("category", category))
        if custom:
            category_input = ttk.Combobox(
                form, textvariable=category_var,
                values=sorted(ALLOWED_CATEGORIES), state="readonly",
            )
        else:
            category_input = ttk.Entry(form, textvariable=category_var, state="readonly")
        category_input.grid(row=2, column=1, sticky="ew", padx=(0, 12), pady=(4, 10))

        ttk.Label(form, text="Date (DD-MM-YYYY, blank = daily)").grid(
            row=1, column=2, sticky="w"
        )
        date_entry = ttk.Entry(form)
        date_entry.grid(row=2, column=2, sticky="ew", padx=(0, 12), pady=(4, 10))
        date_entry.insert(0, initial.get("reminder_date", ""))

        ttk.Label(form, text="Time (24-hour HH:MM)").grid(row=1, column=3, sticky="w")
        time_entry = ttk.Entry(form)
        time_entry.grid(row=2, column=3, sticky="ew", pady=(4, 10))
        time_entry.insert(0, initial.get("reminder_time", ""))

        ttk.Label(form, text="Description / instructions (optional)").grid(
            row=3, column=0, columnspan=2, sticky="w"
        )
        description_entry = ttk.Entry(form)
        description_entry.grid(
            row=4, column=0, columnspan=3, sticky="ew", padx=(0, 12), pady=(4, 11)
        )
        description_entry.insert(0, initial.get("description", ""))

        for column in range(4):
            form.columnconfigure(column, weight=1)

        def save():
            try:
                fields = (
                    validate_medicine(
                        title_entry.get(), time_entry.get(), date_entry.get(),
                        description_entry.get(),
                    )
                    if category == "Medicine"
                    else validate_reminder(
                        title_entry.get(), category_var.get(), date_entry.get(),
                        time_entry.get(), description_entry.get(),
                    )
                )
                reminder_id = initial.get("id")
                if reminder_id is None:
                    self.database.add_reminder(
                        fields["title"], fields["category"], fields["date"],
                        fields["time"], fields["description"],
                    )
                    messagebox.showinfo(
                        "Reminder saved", "Reminder added successfully!",
                        parent=popup or self.root,
                    )
                else:
                    self.database.update_reminder(
                        reminder_id, fields["title"], fields["category"], fields["date"],
                        fields["time"], fields["description"],
                    )
                    messagebox.showinfo(
                        "Reminder saved", "Reminder updated successfully!",
                        parent=popup or self.root,
                    )
                if popup:
                    popup.destroy()
                if on_saved:
                    on_saved()
            except (ValueError, RuntimeError) as exc:
                messagebox.showerror("Check your reminder", str(exc), parent=popup or self.root)

        button_text = "Save changes" if existing else "Add reminder"
        ttk.Button(form, text=button_text, style="Accent.TButton", command=save).grid(
            row=4, column=3, sticky="e", pady=(4, 11)
        )

    def _render_manage(self):
        ttk.Label(
            self.page_body,
            text="Search by name, then filter by category and pending, completed, or missed status.",
            style="Muted.TLabel",
        ).pack(anchor="w", pady=(0, 15))
        filters = ttk.Frame(self.page_body)
        filters.pack(fill="x", pady=(0, 10))
        ttk.Label(filters, text="Search").pack(side="left")
        search_var = tk.StringVar()
        search_entry = ttk.Entry(filters, textvariable=search_var, width=22)
        search_entry.pack(side="left", padx=(6, 14))
        ttk.Label(filters, text="Category").pack(side="left")
        category_var = tk.StringVar(value="All")
        category_input = ttk.Combobox(
            filters, textvariable=category_var,
            values=["All", *sorted(ALLOWED_CATEGORIES)], state="readonly", width=14,
        )
        category_input.pack(side="left", padx=(6, 14))
        ttk.Label(filters, text="Status").pack(side="left")
        status_var = tk.StringVar(value="All")
        status_input = ttk.Combobox(
            filters, textvariable=status_var,
            values=["All", "Pending", "Completed", "Missed"],
            state="readonly", width=12,
        )
        status_input.pack(side="left", padx=6)

        card = self._card(self.page_body)
        card.pack(fill="both", expand=True)
        tree_frame = ttk.Frame(card, style="White.TFrame")
        tree_frame.pack(fill="both", expand=True)
        tree = [None]
        actions = ttk.Frame(card, style="White.TFrame")
        actions.pack(fill="x", pady=(13, 0))

        def selected_id():
            selection = tree[0].selection() if tree[0] else ()
            if not selection:
                messagebox.showwarning(
                    "No reminder selected", "Please select a reminder first.",
                    parent=self.root,
                )
                return None
            return int(selection[0])

        def refresh():
            for child in tree_frame.winfo_children():
                child.destroy()
            today = date.today().strftime("%d-%m-%Y")
            now = datetime.now()
            day_history = self.database.history()
            notified = {
                row["reminder_id"] for row in day_history
                if row["reminder_id"]
                and row["scheduled_time"].startswith(today)
                and row["status"] in ("Notified", "Snoozed")
            }
            done = {
                row["reminder_id"] for row in day_history
                if row["reminder_id"]
                and row["scheduled_time"].startswith(today)
                and row["status"] == "Done"
            }
            rows = []
            for reminder in self.database.get_reminders():
                status = reminder["status"]
                if status == "Active":
                    if reminder["id"] in done:
                        status = "Completed"
                    else:
                        scheduled_date = (
                            datetime.strptime(
                                reminder["reminder_date"], "%d-%m-%Y"
                            ).date()
                            if reminder["reminder_date"] else now.date()
                        )
                        due = datetime.combine(
                            scheduled_date,
                            datetime.strptime(
                                reminder["reminder_time"], "%H:%M"
                            ).time(),
                        )
                        if reminder["id"] not in notified and due < now:
                            status = "Missed"
                        else:
                            status = "Pending"
                if category_var.get() != "All" and reminder["category"] != category_var.get():
                    continue
                if status_var.get() != "All" and status != status_var.get():
                    continue
                if search_var.get().strip().casefold() not in reminder["title"].casefold():
                    continue
                row = dict(reminder)
                row["status"] = status
                rows.append(row)
            tree[0] = self._create_tree(
                tree_frame, rows,
                columns=("title", "category", "date", "time", "status"),
                headings=("Reminder", "Category", "Date", "Time", "Status"),
                height=13,
            )

        ttk.Button(
            actions, text="Edit", command=lambda: self._edit_selected(selected_id())
        ).pack(side="left")
        ttk.Button(
            actions, text="Mark as done",
            command=lambda: self._complete_selected(selected_id()),
        ).pack(side="left", padx=8)
        ttk.Button(
            actions, text="Delete",
            command=lambda: self._delete_selected(selected_id()),
        ).pack(side="left")
        ttk.Button(
            actions, text="Refresh", command=self._refresh_page
        ).pack(side="right")
        ttk.Button(filters, text="Search", command=refresh).pack(side="left", padx=(8, 0))
        category_input.bind("<<ComboboxSelected>>", lambda _event: refresh())
        status_input.bind("<<ComboboxSelected>>", lambda _event: refresh())
        search_entry.bind("<Return>", lambda _event: refresh())
        refresh()

    def _create_tree(self, parent, rows, columns, headings, height=8):
        container = ttk.Frame(parent, style="White.TFrame")
        container.pack(fill="both", expand=True)
        tree = ttk.Treeview(
            container, columns=columns, show="headings", height=height,
            selectmode="browse",
        )
        for column, heading in zip(columns, headings):
            tree.heading(column, text=heading)
            tree.column(column, width=145, minwidth=85, anchor="w")
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        for row in rows:
            values = []
            for column in columns:
                if column == "title":
                    values.append(row["title"])
                elif column == "date":
                    values.append(row["reminder_date"] or "Daily")
                elif column == "time":
                    values.append(row["reminder_time"])
                else:
                    values.append(row[column])
            tree.insert("", "end", iid=str(row["id"]), values=values)
        return tree

    def _edit_selected(self, reminder_id):
        if reminder_id is None:
            return
        reminder = self.database.get_reminder(reminder_id)
        if reminder is None or reminder["status"] != "Active":
            messagebox.showwarning("Reminder unavailable", "Only active reminders can be edited.")
            return
        popup = tk.Toplevel(self.root)
        popup.title("Edit reminder")
        popup.geometry("880x235")
        popup.transient(self.root)
        popup.grab_set()
        body = ttk.Frame(popup, padding=18)
        body.pack(fill="both", expand=True)
        self._build_reminder_form(
            body, reminder["category"], "Update reminder",
            custom=True, existing=reminder, on_saved=self._refresh_page, popup=popup,
        )

    def _complete_selected(self, reminder_id):
        if reminder_id is None:
            return
        try:
            self._complete_reminder(reminder_id)
        except (ValueError, RuntimeError) as exc:
            messagebox.showerror("Could not complete reminder", str(exc))

    def _complete_reminder(self, reminder_id):
        self.database.complete_reminder(reminder_id)
        self.database.unlock_achievements()
        popup = self.active_notifications.pop(reminder_id, None)
        if popup and popup.winfo_exists():
            popup.destroy()
        self._refresh_page()

    def _snooze_reminder(self, reminder_id, minutes=5):
        try:
            self.database.snooze_reminder(reminder_id, minutes=minutes)
            popup = self.active_notifications.pop(reminder_id, None)
            if popup and popup.winfo_exists():
                popup.destroy()
            self._refresh_page()
        except (ValueError, RuntimeError) as exc:
            messagebox.showerror("Could not snooze reminder", str(exc))

    def _delete_selected(self, reminder_id):
        if reminder_id is None:
            return
        if not messagebox.askyesno(
            "Delete reminder", "Delete this reminder permanently?", parent=self.root
        ):
            return
        try:
            self.database.delete_reminder(reminder_id)
            self.active_notifications.pop(reminder_id, None)
            messagebox.showinfo(
                "Reminder deleted", "Reminder deleted successfully!", parent=self.root
            )
            self._refresh_page()
        except (ValueError, RuntimeError) as exc:
            messagebox.showerror("Could not delete reminder", str(exc))

    def _render_history(self):
        controls = ttk.Frame(self.page_body)
        controls.pack(fill="x", pady=(0, 13))
        ttk.Label(controls, text="Search").pack(side="left")
        search_var = tk.StringVar()
        search_entry = ttk.Entry(controls, textvariable=search_var, width=28)
        search_entry.pack(side="left", padx=(8, 15))
        ttk.Label(controls, text="Category").pack(side="left")
        category_var = tk.StringVar(value="All")
        category_input = ttk.Combobox(
            controls, textvariable=category_var, values=["All", *sorted(ALLOWED_CATEGORIES)],
            state="readonly", width=15,
        )
        category_input.pack(side="left", padx=8)
        card = self._card(self.page_body)
        card.pack(fill="both", expand=True)
        tree_frame = ttk.Frame(card, style="White.TFrame")
        tree_frame.pack(fill="both", expand=True)

        def refresh():
            for child in tree_frame.winfo_children():
                child.destroy()
            rows = self.database.history(search_var.get(), category_var.get())
            self._create_tree(
                tree_frame, rows,
                columns=("reminder_title", "category", "scheduled_time",
                         "completion_time", "status"),
                headings=("Reminder", "Category", "Scheduled time",
                          "Completion time", "Activity status"),
                height=15,
            )
            if not rows:
                ttk.Label(
                    card, text="No activity matches your search.",
                    style="Muted.TLabel",
                ).pack(anchor="w", pady=(8, 0))
            else:
                for child in card.winfo_children():
                    if isinstance(child, ttk.Label) and child.cget("text") == "No activity matches your search.":
                        child.destroy()

        ttk.Button(controls, text="Search", command=refresh).pack(side="left")
        ttk.Button(
            controls, text="Export CSV", style="Accent.TButton",
            command=self._export_history,
        ).pack(side="right")
        search_entry.bind("<Return>", lambda _event: refresh())
        category_input.bind("<<ComboboxSelected>>", lambda _event: refresh())
        refresh()

    def _render_weekly_report(self):
        ttk.Label(
            self.page_body,
            text="Your last seven days of reminders, hydration, and exercise.",
            style="Muted.TLabel",
        ).pack(anchor="w", pady=(0, 12))
        rows = self.database.weekly_report(days=7)
        chart_card = self._card(self.page_body, padding=10)
        chart_card.pack(fill="both", expand=True)
        try:
            from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
            from matplotlib.figure import Figure
        except ImportError as exc:
            raise RuntimeError(
                "Weekly charts require Matplotlib. Install it with "
                "'python -m pip install -r requirements.txt'."
            ) from exc

        figure = Figure(figsize=(8, 4.8), dpi=90, facecolor=self._palette()["card"])
        axis = figure.add_subplot(211)
        axis.set_facecolor(self._palette()["card"])
        labels = [row["date"].strftime("%a %d") for row in rows]
        axis.bar(labels, [row["completion_percentage"] for row in rows],
                 color=GREEN, width=0.58, label="Reminder completion (%)")
        axis.set_ylim(0, 100)
        axis.set_ylabel("Completion (%)")
        axis.grid(axis="y", alpha=0.2)
        axis.tick_params(colors=self._palette()["text"])
        axis.yaxis.label.set_color(self._palette()["text"])
        for spine in axis.spines.values():
            spine.set_color(self._palette()["header"])
        water_axis = axis.twinx()
        water_axis.plot(
            labels, [row["water_glasses"] for row in rows],
            color="#4AA3D8", marker="o", linewidth=2, label="Water glasses",
        )
        water_axis.set_ylabel("Water glasses")
        water_axis.tick_params(colors=self._palette()["text"])
        water_axis.yaxis.label.set_color(self._palette()["text"])
        exercise_axis = figure.add_subplot(212, sharex=axis)
        exercise_axis.bar(
            labels, [row["exercise_completed"] for row in rows],
            color="#80B89B", width=0.58,
        )
        exercise_axis.set_ylabel("Exercise reminders completed")
        exercise_axis.grid(axis="y", alpha=0.2)
        exercise_axis.tick_params(colors=self._palette()["text"])
        exercise_axis.yaxis.label.set_color(self._palette()["text"])
        figure.tight_layout()
        chart = FigureCanvasTkAgg(figure, master=chart_card)
        chart.draw()
        chart.get_tk_widget().pack(fill="both", expand=True)

        table_card = self._card(self.page_body, padding=12)
        table_card.pack(fill="x", pady=(12, 0))
        tree = ttk.Treeview(
            table_card,
            columns=("day", "completed", "scheduled", "water", "exercise", "progress"),
            show="headings", height=5,
        )
        for column, heading in (
            ("day", "Day"), ("completed", "Done"), ("scheduled", "Scheduled"),
            ("water", "Water"), ("exercise", "Exercise"), ("progress", "Progress"),
        ):
            tree.heading(column, text=heading)
            tree.column(column, width=90, anchor="center")
        for row in rows:
            tree.insert(
                "", "end",
                values=(
                    row["date"].strftime("%a, %d %b"),
                    row["completed"], row["total"],
                    f"{row['water_glasses']} / {row['water_goal']}",
                    row["exercise_completed"], f"{row['completion_percentage']}%",
                ),
            )
        tree.pack(fill="x")
        actions = ttk.Frame(self.page_body)
        actions.pack(fill="x", pady=(10, 0))
        ttk.Button(
            actions, text="Export daily CSV",
            command=lambda: self._export_activity_report(1),
        ).pack(side="left")
        ttk.Button(
            actions, text="Export weekly CSV", style="Accent.TButton",
            command=lambda: self._export_activity_report(7),
        ).pack(side="left", padx=8)

    def _export_activity_report(self, days):
        label = "daily" if days == 1 else "weekly"
        destination = filedialog.asksaveasfilename(
            parent=self.root, title=f"Export {label} report",
            defaultextension=".csv", filetypes=[("CSV files", "*.csv")],
            initialfile=f"healthmate_{label}_report.csv",
        )
        if not destination:
            return
        try:
            export_activity_report(self.database, destination, days=days)
            messagebox.showinfo(
                "Export complete", f"The {label} report was exported successfully.",
                parent=self.root,
            )
        except (RuntimeError, ValueError) as exc:
            messagebox.showerror("Export failed", str(exc), parent=self.root)

    def _render_calendar(self):
        controls = ttk.Frame(self.page_body)
        controls.pack(fill="x", pady=(0, 8))
        month_label = ttk.Label(controls, style="Subheading.TLabel")
        month_label.pack(side="left", expand=True)
        grid = ttk.Frame(self.page_body)
        grid.pack(fill="x")
        detail_card = self._card(self.page_body, padding=12)
        detail_card.pack(fill="both", expand=True, pady=(12, 0))

        def display():
            month_label.configure(text=self.calendar_month.strftime("%B %Y"))
            for child in grid.winfo_children():
                child.destroy()
            month_data = calendar.monthcalendar(
                self.calendar_month.year, self.calendar_month.month
            )
            reminders = self.database.get_reminders()
            scheduled_days = set()
            for reminder in reminders:
                if reminder["reminder_date"]:
                    scheduled_days.add(
                        datetime.strptime(reminder["reminder_date"], "%d-%m-%Y").date()
                    )
                else:
                    scheduled_days.update(
                        date(self.calendar_month.year, self.calendar_month.month, day)
                        for week in month_data for day in week if day
                    )
            for column, weekday in enumerate(("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")):
                ttk.Label(grid, text=weekday, style="Muted.TLabel").grid(
                    row=0, column=column, sticky="nsew", pady=4
                )
                grid.columnconfigure(column, weight=1)
            for row_index, week in enumerate(month_data, start=1):
                for column, day_number in enumerate(week):
                    if not day_number:
                        ttk.Label(grid, text="").grid(
                            row=row_index, column=column, sticky="nsew", pady=2
                        )
                        continue
                    day = date(
                        self.calendar_month.year, self.calendar_month.month, day_number
                    )
                    marker = " •" if day in scheduled_days else ""
                    selected = day == self.calendar_selected
                    ttk.Button(
                        grid, text=f"{day_number}{marker}",
                        style="Accent.TButton" if selected else "TButton",
                        command=lambda chosen=day: self._select_calendar_day(chosen),
                    ).grid(row=row_index, column=column, sticky="nsew", padx=2, pady=2)
            for child in detail_card.winfo_children():
                child.destroy()
            self._render_calendar_day(detail_card, self.calendar_selected)

        def change_month(delta):
            year = self.calendar_month.year
            month = self.calendar_month.month + delta
            if month == 0:
                year, month = year - 1, 12
            elif month == 13:
                year, month = year + 1, 1
            self.calendar_month = date(year, month, 1)
            final_day = calendar.monthrange(year, month)[1]
            self.calendar_selected = date(
                year, month, min(self.calendar_selected.day, final_day)
            )
            display()

        ttk.Button(
            controls, text="‹", command=lambda: change_month(-1)
        ).pack(side="left")
        ttk.Button(
            controls, text="Today",
            command=lambda: self._select_calendar_day(date.today()),
        ).pack(side="right")
        ttk.Button(
            controls, text="›", command=lambda: change_month(1)
        ).pack(side="right", padx=(0, 6))
        display()

    def _select_calendar_day(self, selected):
        self.calendar_selected = selected
        self.calendar_month = selected.replace(day=1)
        self._refresh_page()

    def _render_calendar_day(self, parent, selected):
        ttk.Label(
            parent, text=f"Activities for {selected.strftime('%A, %d %B %Y')}",
            style="CardTitle.TLabel",
        ).pack(anchor="w", pady=(0, 8))
        ttk.Label(
            parent,
            text=f"Water: {self.database.water_glasses(selected)} glasses",
            style="Muted.TLabel",
        ).pack(anchor="w", pady=(0, 8))
        day_key = selected.strftime("%d-%m-%Y")
        rows = []
        history = self.database.history()
        done_ids = {
            item["reminder_id"] for item in history
            if item["reminder_id"] and item["status"] == "Done"
            and item["scheduled_time"].startswith(day_key)
        }
        notified_ids = {
            item["reminder_id"] for item in history
            if item["reminder_id"] and item["status"] in ("Notified", "Snoozed")
            and item["scheduled_time"].startswith(day_key)
        }
        for reminder in self.database.get_reminders():
            if reminder["reminder_date"] and reminder["reminder_date"] != day_key:
                continue
            scheduled = datetime.combine(
                selected, datetime.strptime(reminder["reminder_time"], "%H:%M").time()
            )
            status = (
                "Completed" if reminder["id"] in done_ids
                else "Pending" if reminder["id"] in notified_ids
                else "Upcoming" if scheduled > datetime.now()
                else "Missed"
            )
            rows.append(
                (reminder["reminder_time"], reminder["title"], reminder["category"], status)
            )
        for item in history:
            if item["scheduled_time"].startswith(day_key):
                rows.append(
                    (
                        item["scheduled_time"][11:],
                        item["reminder_title"],
                        item["category"] or "Activity",
                        f"Activity · {item['status']}",
                    )
                )
        tree = ttk.Treeview(
            parent, columns=("time", "title", "category", "status"),
            show="headings", height=7,
        )
        for column, heading in (
            ("time", "Time"), ("title", "Activity"), ("category", "Category"),
            ("status", "Status"),
        ):
            tree.heading(column, text=heading)
            tree.column(column, width=120, anchor="w")
        for row in sorted(rows):
            tree.insert("", "end", values=row)
        tree.pack(fill="both", expand=True)
        if not rows:
            ttk.Label(
                parent, text="No scheduled reminders or activity for this date.",
                style="Muted.TLabel",
            ).pack(anchor="w", pady=8)

    def _render_achievements(self):
        unlocked = self.database.unlock_achievements()
        streak = self.database.health_streak()
        ttk.Label(
            self.page_body,
            text=f"Current streak: {streak['current']} days    ·    "
                 f"Longest streak: {streak['longest']} days",
            style="Subheading.TLabel",
        ).pack(anchor="w", pady=(0, 14))
        badges = (
            ("bronze_badge", "Bronze Badge", "Complete 3 reminders in one day.", "B"),
            ("gold_badge", "Gold Badge", "Complete all scheduled daily reminders.", "G"),
            ("hydration_hero", "Water Champion", "Reach your personal daily water goal.", "W"),
            ("fitness_star", "Fitness Star", "Complete an exercise reminder.", "F"),
            ("routine_master", "Routine Master", "Complete today's reminders and water goal.", "R"),
            ("seven_day_champion", "Weekly Star", "Meet your daily goals seven days in a row.", "7"),
            ("health_master", "Health Master", "Maintain a 30-day health streak.", "30"),
        )
        grid = ttk.Frame(self.page_body)
        grid.pack(fill="x")
        for index, (badge_id, title, description, symbol) in enumerate(badges):
            card = self._card(grid)
            card.grid(
                row=index // 2, column=index % 2, sticky="nsew",
                padx=(0, 10), pady=(0, 10),
            )
            icon_label = ttk.Label(
                card, image=self.icons.create(symbol, size=42), style="Card.TLabel"
            )
            icon_label.image = self.icons.create(symbol, size=42)
            icon_label.pack(anchor="w", pady=(0, 7))
            ttk.Label(
                card, text=f"{'Unlocked' if badge_id in unlocked else 'Locked'} · {title}",
                style="CardTitle.TLabel",
            ).pack(anchor="w")
            ttk.Label(
                card,
                text=(f"Unlocked {unlocked[badge_id][:10]}" if badge_id in unlocked
                      else description),
                style="Muted.TLabel", wraplength=320,
            ).pack(anchor="w", pady=(6, 0))
        grid.columnconfigure(0, weight=1)
        grid.columnconfigure(1, weight=1)

    def _render_profile(self):
        profile = self.database.get_profile()
        card = self._card(self.page_body)
        card.pack(fill="x")
        ttk.Label(card, text="Your health profile", style="CardTitle.TLabel").pack(
            anchor="w", pady=(0, 12)
        )
        ttk.Label(card, text="Username").pack(anchor="w")
        ttk.Label(
            card, text=self.account_username or "Not signed in",
            style="Muted.TLabel",
        ).pack(anchor="w", pady=(4, 12))
        ttk.Label(card, text="Display name").pack(anchor="w")
        name_entry = ttk.Entry(card)
        name_entry.pack(fill="x", pady=(4, 12))
        name_entry.insert(0, profile["display_name"])
        ttk.Label(card, text="Daily water goal (glasses)").pack(anchor="w")
        goal_entry = ttk.Entry(card)
        goal_entry.pack(fill="x", pady=(4, 14))
        if profile["daily_water_goal"]:
            goal_entry.insert(0, str(profile["daily_water_goal"]))

        def save():
            try:
                name = validate_profile_name(name_entry.get())
                goal = validate_optional_water_goal(goal_entry.get())
                self.database.update_profile(name, goal)
                self.database.unlock_achievements()
                if self.topbar_name is not None:
                    self.topbar_name.configure(text=name)
                messagebox.showinfo(
                    "Profile saved", "Your name and water goal were updated.",
                    parent=self.root,
                )
                self._refresh_page()
            except (ValueError, RuntimeError) as exc:
                messagebox.showerror("Check your profile", str(exc), parent=self.root)

        ttk.Button(
            card, text="Save profile", style="Accent.TButton", command=save,
        ).pack(anchor="e")
        ttk.Label(
            self.page_body,
            text=(
                "Choose a personal daily goal from 1 to 30 glasses. "
                "HealthMate does not set or prescribe a goal for you."
            ),
            style="Muted.TLabel",
        ).pack(anchor="w", pady=(10, 0))

    def _export_history(self):
        destination = filedialog.asksaveasfilename(
            parent=self.root, title="Export activity history",
            defaultextension=".csv", filetypes=[("CSV files", "*.csv")],
            initialfile="healthmate_history.csv",
        )
        if not destination:
            return
        try:
            export_history(self.database, destination)
            messagebox.showinfo(
                "Export complete", "Activity history exported successfully!",
                parent=self.root,
            )
        except RuntimeError as exc:
            messagebox.showerror("Export failed", str(exc), parent=self.root)

    def _render_settings(self):
        card = self._card(self.page_body)
        card.pack(fill="x")
        ttk.Label(card, text="Reminder settings", style="CardTitle.TLabel").pack(
            anchor="w", pady=(0, 10)
        )
        settings = [
            ("Automatic check interval", "Every 15 seconds"),
            ("Snooze options", "5, 10, or 15 minutes"),
            ("Repeating reminders", "Leave Date blank to repeat daily"),
            ("One-time reminders", "Enter a future date as DD-MM-YYYY"),
            ("Notifications", "Popup and sound; HealthMate must remain open"),
            ("Database", str(self.database.database_path)),
        ]
        for label, value in settings:
            row = ttk.Frame(card, style="White.TFrame")
            row.pack(fill="x", pady=7)
            ttk.Label(row, text=label, style="Card.TLabel").pack(side="left")
            ttk.Label(row, text=value, style="Muted.TLabel", wraplength=480).pack(
                side="right"
            )
        ttk.Label(
            card,
            text=(
                "Medicine reminders only store the schedule and instructions you enter. "
                "Use the plan prescribed by your healthcare professional."
            ),
            wraplength=750,
            style="Muted.TLabel",
        ).pack(anchor="w", pady=(18, 0))

    def _refresh_page(self):
        self.show_page(self.current_page)

    def close(self):
        if messagebox.askyesno(
            "Close HealthMate",
            "Reminders will not appear while HealthMate is closed. Exit now?",
            parent=self.root,
        ):
            self.running = False
            self._cancel_background_callbacks()
            self.root.destroy()
