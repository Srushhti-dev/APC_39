products = {}

def add_product(name, price, quantity):
    products[name] = [price, quantity]

def remove_product(name):
    if name in products:
        del products[name]

def subtotal():
    total = 0
    for price, quantity in products.values():
        total += price * quantity
    return total

def coupon_discount(amount):
    return amount * 0.10 if amount >= 5000 else 0

def gst(amount):
    return amount * 0.18

def invoice():
    sub = subtotal()
    discount = coupon_discount(sub)
    taxable = sub - discount
    tax = gst(taxable)

    print("Subtotal =", sub)
    print("Discount =", discount)
    print("GST =", tax)
    print("Final Amount =", taxable + tax)

add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)
invoice()
