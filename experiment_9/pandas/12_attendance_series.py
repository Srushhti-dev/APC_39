import pandas as pd

attendance = {
    "Aarav": 92,
    "Priya": 74,
    "Rohan": 88,
    "Sneha": 68,
    "Vikram": 95
}

s = pd.Series(attendance)

print("Average attendance:", s.mean())
print("\nBelow 75%:\n", s[s < 75])
print("\nAbove 90%:\n", s[s > 90])
print("\nHighest attendance:", s.max())
