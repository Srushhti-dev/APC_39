contacts = {"Amit": "9876543210", "Rahul": "9876501234"}

name = input("Enter name to add: ")
phone = input("Enter phone number: ")
contacts[name] = phone

name = input("Enter name to search: ")
if name in contacts:
    print("Phone:", contacts[name])
else:
    print("Contact not found")

name = input("Enter name to update: ")
if name in contacts:
    phone = input("Enter new phone number: ")
    contacts[name] = phone

name = input("Enter name to delete: ")
if name in contacts:
    del contacts[name]

print("All contacts:")
for name, phone in contacts.items():
    print(name, ":", phone)
