import pandas as pd

ages = {
    "P101": 65,
    "P102": 45,
    "P103": 72,
    "P104": 58,
    "P105": 80
}

series = pd.Series(ages)

print("Average age:", series.mean())
print("Oldest patient:", series.idxmax(), "=", series.max())
print("Youngest patient:", series.idxmin(), "=", series.min())

print("\nPatients above 60 years:")
print(series[series > 60])
