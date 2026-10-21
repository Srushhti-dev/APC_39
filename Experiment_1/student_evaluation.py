#WAP to evaluate student persformance

marks=float(input("Enter Marks:"))

if marks>=90 and marks<=100:
    print("Excellent")
elif marks>=80 and marks<=90:
    print("Very Good")
elif marks>=70 and marks<=80:
    print("Good")
elif marks>=60 and marks<=70:
    print("Average")
else:
    print("Poor")