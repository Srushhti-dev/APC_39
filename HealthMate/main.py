"""Start the HealthMate desktop application."""


import tkinter as tk
from tkinter import messagebox

from database import HealthMateDatabase
from gui import HealthMateApp


def main():
    database = None
    try:
        database = HealthMateDatabase()
        root = tk.Tk()
        app = HealthMateApp(root, database)
        root.protocol("WM_DELETE_WINDOW", app.close)
        root.mainloop()
    except (OSError, RuntimeError) as exc:
        try:
            messagebox.showerror("HealthMate could not start", str(exc))
        except tk.TclError:
            print(f"HealthMate could not start: {exc}")
    finally:
        if database is not None:
            database.close()


if __name__ == "__main__":
    main()
