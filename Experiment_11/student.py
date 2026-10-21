from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Student Form")
root.geometry("300x300")

Label(root, text="Student Form",
      font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Student Name").pack()
name = Entry(root)
name.pack()

Label(root, text="Roll Number").pack()
roll = Entry(root)
roll.pack()

Label(root, text="Select Subjects").pack(pady=5)

s1 = IntVar()
s2 = IntVar()
s3 = IntVar()

Checkbutton(root, text="Python", variable=s1).pack()
Checkbutton(root, text="Java", variable=s2).pack()
Checkbutton(root, text="Database", variable=s3).pack()

def submit():
    subjects = []

    if s1.get():
        subjects.append("Python")
    if s2.get():
        subjects.append("Java")
    if s3.get():
        subjects.append("Database")

    messagebox.showinfo(
        "Student Details",
        f"Name: {name.get()}\n"
        f"Roll No: {roll.get()}\n"
        f"Subjects: {', '.join(subjects)}"
    )

Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()