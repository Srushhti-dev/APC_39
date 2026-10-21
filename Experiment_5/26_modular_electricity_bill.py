def slab_charge(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 100 * 5 + (units - 100) * 7
    else:
        return 100 * 5 + 100 * 7 + (units - 200) * 10

def fixed_charge():
    return 100

def calculate_tax(amount):
    return amount * 0.05

def discount(amount):
    if amount > 5000:
        return amount * 0.10
    return 0

def electricity_bill(units):
    charge = slab_charge(units)
    fixed = fixed_charge()
    subtotal = charge + fixed
    tax = calculate_tax(subtotal)
    disc = discount(subtotal)
    return subtotal + tax - disc

units = int(input("Enter units: "))
print("Final Bill =", electricity_bill(units))
