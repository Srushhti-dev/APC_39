names = ["Rahul", "Priya", "Amit"]
ages = [25, 30, 45]

# Display patients
print("Patients:")

for i in range(len(names)):
    print("Name:", names[i], "Age:", ages[i])

# Add patient
new_name = input("Enter new patient name: ")
new_age = int(input("Enter patient age: "))

names.append(new_name)
ages.append(new_age)

print("\nPatient added.")

# Delete patient
delete_name = input("Enter patient name to delete: ")

if delete_name in names:
    index = names.index(delete_name)

    names.pop(index)
    ages.pop(index)

    print("Patient deleted.")
else:
    print("Patient not found.")

# Display updated patients
print("\nUpdated Patient List:")

for i in range(len(names)):
    print("Name:", names[i], "Age:", ages[i])