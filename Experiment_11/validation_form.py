import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Registration Form")
root.geometry("300x300")

tk.Label(root, text="Student Registration",
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Name").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Age").pack()
age = tk.Entry(root)
age.pack()

tk.Label(root, text="Email").pack()
email = tk.Entry(root)
email.pack()

def register():
    n = name.get().strip()
    a = age.get().strip()
    e = email.get().strip()

    if n == "" or a == "" or e == "":
        messagebox.showerror("Error", "Fill all fields")
    elif not n.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Enter a valid name")
    elif not a.isdigit() or int(a) < 1 or int(a) > 120:
        messagebox.showerror("Error", "Enter a valid age")
    elif "@" not in e or "." not in e:
        messagebox.showerror("Error", "Enter a valid email")
    else:
        messagebox.showinfo("Success", "Registration Successful!")

tk.Button(root, text="Register",
          command=register).pack(pady=15)

root.mainloop()