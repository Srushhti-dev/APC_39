patients = (
    (101, "Srushhti", 25, "A+"),
    (102, "Arya", 30, "B+"),
    (103, "Aditi", 45, "O+"),
    (104, "Harsh", 28, "A+")
)


print("Patient Records:")

for patient in patients:
    print("ID:", patient[0],
          "Name:", patient[1],
          "Age:", patient[2],
          "Blood Group:", patient[3])


search_id = int(input("\nEnter Patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == search_id:
        print("Patient Found:")
        print("ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[3])
        found = True

if not found:
    print("Patient not found.")

print("\nTotal number of patients:", len(patients))

blood_group = input("\nEnter blood group to search: ")

print("Patients with blood group", blood_group, ":")

for patient in patients:
    if patient[3] == blood_group:
        print(patient)