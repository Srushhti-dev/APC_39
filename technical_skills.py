#22.	Create two sets representing technical skills of two employees. Find:Common skills ,Skills unique to Employee 1 ,Skills unique to Employee 2 ,	All available skills
employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Python", "HTML", "SQL", "JavaScript"}

print("Common skills:", employee1 & employee2)
print("Skills unique to Employee 1:", employee1 - employee2)
print("Skills unique to Employee 2:", employee2 - employee1)
print("All available skills:", employee1 | employee2)