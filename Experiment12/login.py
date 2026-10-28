
import tkinter as tk
import re
from tkinter import messagebox

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    user_pattern = r'^[A-Za-z]{3,15}$'
    pass_pattern = r'^[A-Za-z0-9@#$]{6,}$'

    if not re.fullmatch(user_pattern, username):
        messagebox.showerror("Error", "Invalid Username!")
    elif not re.fullmatch(pass_pattern, password):
        messagebox.showerror("Error", "Invalid Password!")
    else:
        messagebox.showinfo("Success", "Login Successful!")

root = tk.Tk()
root.title("User Login")
root.geometry("350x300")
root.configure(bg="lightblue")

tk.Label(root, text="USER LOGIN",
         font=("Arial", 18, "bold"),
         bg="lightblue").pack(pady=15)

tk.Label(root, text="Username",
         bg="lightblue").pack()

username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password",
         bg="lightblue").pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login",
          command=validate_login,
          bg="blue", fg="white").pack(pady=20)

root.mainloop()

