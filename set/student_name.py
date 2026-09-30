#5.	Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
students = {"Srushhti","Arya","Aditi","Rahul","Harsh"}.lower()

name = input("enter a name:")
if name in students:
    print("Present")
else:
    print("Absent")