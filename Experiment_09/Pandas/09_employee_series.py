import pandas as pd

salaries = {
    "Amit": 60000,
    "Neha": 48000,
    "Rahul": 55000,
    "Pooja": 75000,
    "Karan": 52000
}

s = pd.Series(salaries)

print("Series:\n", s)
print("\nHighest salary:", s.max())
print("Lowest salary:", s.min())
print("Average salary:", s.mean())
print("\nEmployees earning more than ₹50,000:\n", s[s > 50000])
