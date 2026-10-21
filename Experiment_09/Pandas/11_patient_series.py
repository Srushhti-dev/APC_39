import pandas as pd

ages = {
    "P001": 45,
    "P002": 67,
    "P003": 72,
    "P004": 55,
    "P005": 81
}

s = pd.Series(ages)

print("Average age:", s.mean())
print("\nOldest patient:", s.idxmax(), "Age:", s.max())
print("Youngest patient:", s.idxmin(), "Age:", s.min())
print("\nPatients above 60:\n", s[s > 60])
