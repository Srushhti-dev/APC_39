#17.	Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students
student1 = {"Python", "Java", "DBMS", "CN"}
student2 = {"Python", "C++", "DBMS", "AI"}

common = student1.intersection(student2)

print("Subjects studied by both:", common)