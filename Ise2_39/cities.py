cities = ["Pune", "Mumbai", "Kolhapur", "Delhi", "Bangalore"]

city = input("Enter a city name: ")

if city in cities:
    print("City exists in the list.")
else:
    print("City does not exist in the list.")