cities = {"Pune": 7000000, "Mumbai": 20000000, "Delhi": 30000000, "Nashik": 2000000}
city = input("Enter city to remove: ")
if city in cities:
    del cities[city]
print(cities)
