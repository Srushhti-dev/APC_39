scores = [45, 120, 75, 30, 105, 55, 90, 150, 40, 65]

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Number of centuries:", centuries)
print("Number of half-centuries:", half_centuries)