from ecommerce.Products.product import create_product
from ecommerce.Products.catalog import display_products
from ecommerce.Customers.customer import create_customer
from ecommerce.Customers.profile import display_customer
from ecommerce.Orders.order import create_order
from ecommerce.Orders.tracking import track_order
from ecommerce.Payments.payment import make_payment
from ecommerce.Payments.refund import refund

p=create_product(101,"Laptop",50000)
c=create_customer(1,"Amit")
o=create_order(1001,p)
display_products([p])
display_customer(c)
track_order(o)
make_payment(p["price"])
refund(p["price"])
