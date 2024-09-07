CoffeeShopDomain
CoffeeShopDomain is a Python-based project designed to model a basic coffee shop domain, where customers can place orders for different types of coffee. The system models the interactions between Customers, Coffees, and Orders, while including essential data validations and relationships between these entities.

Project Structure
bash
Copy code
CoffeeShopDomain/
│
├── coffee/
│   ├── __init__.py               # Package initialization
│   └── coffee.py                 # Contains Coffee class
│
├── customer/
│   ├── __init__.py               # Package initialization
│   └── customer.py               # Contains Customer class
│
├── order/
│   ├── __init__.py               # Package initialization
│   └── order.py                  # Contains Order class
│
├── utils/
│   ├── __init__.py               # Package initialization
│   └── validation.py             # Contains utility functions for validation
│
└── main.py                       # Main entry point for testing
Components
1. Coffee Class (coffee/coffee.py)
The Coffee class represents a type of coffee in the system. It stores the name of the coffee and manages all the orders placed for that specific type of coffee.

Key Methods:
__init__(self, name: str): Initializes a new Coffee object with a valid name and an empty list of orders.

name (Property):

Getter: Retrieves the coffee's name.
Setter: Validates and sets the name. Once set, the name cannot be changed.
orders(self): Returns all the orders associated with this coffee.

customers(self): Returns a list of unique customers who have ordered this coffee.

num_orders(self): Returns the total number of orders for this coffee.

average_price(self): Returns the average price of all orders for this coffee. If no orders exist, returns 0.

add_order(self, order: 'Order'): Adds an order to this coffee's order list.

__str__(self): Returns a string representation of the coffee (name of the coffee).

Example Usage:
python
Copy code
from coffee.coffee import Coffee

espresso = Coffee("Espresso")
print(espresso)  # Output: Coffee: Espresso
2. Customer Class (customer/customer.py)
The Customer class models a customer in the system. A customer can place orders for different types of coffee.

Key Methods:
__init__(self, name: str): Initializes a new Customer object with a valid name and an empty list of orders.

name (Property):

Getter: Retrieves the customer's name.
Setter: Validates and sets the customer's name.
orders(self): Returns all the orders made by the customer.

coffees(self): Returns a list of unique coffee types the customer has ordered.

create_order(self, coffee: 'Coffee', price: float): Creates and returns a new order for the specified coffee and price.

add_order(self, order: 'Order'): Adds an order to the customer's order list.

__str__(self): Returns a string representation of the customer (name of the customer).

Example Usage:
python
Copy code
from customer.customer import Customer

john = Customer("John Doe")
print(john)  # Output: Customer: John Doe
3. Order Class (order/order.py)
The Order class represents an order placed by a customer for a particular coffee type. It tracks the customer, coffee, price, and date of the order.

Key Methods:
__init__(self, customer: 'Customer', coffee: 'Coffee', price: float): Initializes a new order with the specified customer, coffee, and price.

customer (Property): Retrieves the customer who placed the order.

coffee (Property): Retrieves the coffee that was ordered.

price (Property): Retrieves the price of the order.

__str__(self): Returns a string representation of the order, including customer, coffee, and price.

Example Usage:
python
Copy code
from customer.customer import Customer
from coffee.coffee import Coffee
from order.order import Order

john = Customer("John Doe")
latte = Coffee("Latte")
order = Order(john, latte, 5.0)
print(order)  # Output: Order(John Doe, Latte, $5.00)
4. validate_name Function (utils/validation.py)
This utility function ensures that names are strings of valid length (between min_length and max_length).

Key Function:
validate_name(name: str, min_length: int, max_length: int): Validates that the name is a string and its length is between min_length and max_length. Raises a ValueError if the validation fails.
Example Usage:
python
Copy code
from utils.validation import validate_name

validate_name("Cappuccino", 3, 50)  # This will pass
validate_name("", 3, 50)  # This will raise a ValueError
Running the Application
The main.py file contains a sample implementation to test the interaction between Customers, Coffees, and Orders.

Sample Code in main.py:                                                                                                                               # Add the project root to the Python path
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
To run the project, simply execute:
python main.py                                  
