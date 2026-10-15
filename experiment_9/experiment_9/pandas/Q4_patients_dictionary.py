import pandas as pd

data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Asha", "Ravi", "Meena", "Suresh", "Kiran"],
    "Age": [65, 45, 72, 58, 80],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Diabetes"],
    "Medical_Charges": [60000, 25000, 90000, 40000, 75000]
}

df = pd.DataFrame(data)

print("Patients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage medical charge:", df["Medical_Charges"].mean())
print("Maximum medical charge:", df["Medical_Charges"].max())

print("\nPatients with medical charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])
