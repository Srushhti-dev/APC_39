import pandas as pd

data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Anil", "Meena", "Suresh", "Kavita", "Raj"],
    "Age": [65, 45, 72, 58, 67],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Diabetes"],
    "Medical_Charges": [55000, 12000, 80000, 30000, 62000]
}

df = pd.DataFrame(data)
print("Patients above 60:\n", df[df["Age"] > 60])
print("\nAverage medical charge:", df["Medical_Charges"].mean())
print("\nMaximum medical charge:", df["Medical_Charges"].max())
print("\nCharges greater than ₹50,000:\n", df[df["Medical_Charges"] > 50000])
