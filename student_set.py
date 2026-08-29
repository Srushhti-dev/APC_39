#20.	Create sets representing students enrolled in: Python ,Java 
#21.	Find students enrolled in both courses and students enrolled in only one course.
python_students = {"Srushhti","Arya","Aditi","Rahul","Harsh"}
java_students = {"Arya","Vaishnavi","Aditi","siddhi","vedika"}

both = python_students & java_students
only_one = python_students ^ java_students

print("Students in both courses:", both)
print("Students in only one course:", only_one)


