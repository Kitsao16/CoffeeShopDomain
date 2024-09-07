# Add the project root to the Python path
import sys
from customer.customer import Customer
from coffee.coffee import Coffee


sys.path.append('/home/user/PycharmProjects/CoffeeShopDomain')

# Import the necessary classes

# Create customer instances
customer1 = Customer(name="John")
customer2 = Customer(name="Jane")

# Create coffee instances
espresso = Coffee(name="Espresso")
latte = Coffee(name="Latte")

# Customer1 creates an order for Espresso
order1 = customer1.create_order(coffee=espresso, price=2.50)

# Customer2 creates an order for Latte
order2 = customer2.create_order(coffee=latte, price=3.75)

# Customer1 creates another order for Latte
order3 = customer1.create_order(coffee=latte, price=3.50)

# Output customer details and their orders
print(customer1)  # Should print "Customer: John"
print("Orders:")
for order in customer1.orders():
    print(f"  {order}")  # Print each order's details

# Output the coffees that customer1 has ordered
print("Coffees ordered by John:")
for coffee in customer1.coffees():
    print(f"  {coffee.name}")  # Should list 'Espresso' and 'Latte'

# Output coffee details and their customers
print(espresso)  # Should print "Coffee: Espresso"
print("Customers who ordered Espresso:")
for customer in espresso.customers():
    print(f"  {customer.name}")  # Should list 'John'

# Output the total number of orders for Latte
print(f"Total orders for Latte: {latte.num_orders()}")  # Should be 2

# Output the average price for Latte
print(f"Average price for Latte: ${latte.average_price():.2f}")  # Should be the average of 3.75 and 3.50

# Attempt to change the name of the coffee after instantiation (should not be allowed)
try:
    espresso.name = "Espresso Roast"
except ValueError as e:
    print(f"Error: {e}")  # Should raise an error because coffee name should not change after instantiation

# Change the customer's name (should be allowed)
customer1.name = "Johnny"
print(f"Updated customer name: {customer1.name}")  # Should print "Johnny"
