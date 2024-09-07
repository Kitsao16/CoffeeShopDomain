from typing import TYPE_CHECKING
from utils.validation import validate_name

# Importing for type hinting only when type checking is enabled
if TYPE_CHECKING:
    from order.order import Order  # Import the Order class for type hints
    from customer.customer import Customer  # Import the Customer class for type hints


class Coffee:
    def __init__(self, name: str):
        """
        Initializes a new Coffee instance with a name and sets up an empty list for orders.

        Args:
            name (str): The name of the coffee.

        Raises:
            ValueError: If the name is not a valid string or less than 3 characters.
        """
        self._name = None  # Initialize the private name attribute (underscore indicates privacy)
        self._name_set = False  # A flag to track if the coffee name has been set (it can't be changed later)
        self.name = name  # Use the property setter to validate and set the name
        self._orders = []  # Initialize an empty list to store orders associated with this coffee

    @property
    def name(self) -> str:
        """
        Retrieves the name of the coffee.

        Returns:
            str: The coffee's name.
        """
        return self._name  # Return the private attribute _name

    @name.setter
    def name(self, name: str):
        """
        Sets the coffee's name and performs validation to ensure it's a valid string.

        Args:
            name (str): The new name for the coffee.

        Raises:
            ValueError: If the name is not valid or if the name has already been set.
        """
        # Ensure that the name can only be set once (throws an error if trying to change it)
        if self._name_set:
            raise ValueError("Coffee name cannot be changed after instantiation.")
        # Validate the name using an external validation function (ensures string between 3 and 50 characters)
        validate_name(name, 3, 50)
        self._name = name  # Assign the validated name to the private _name attribute
        self._name_set = True  # Mark the name as set to prevent further changes

    def orders(self) -> list['Order']:
        """
        Returns a list of all orders associated with this coffee.

        Returns:
            List[Order]: A list of Order instances that include this coffee.
        """
        return self._orders  # Return the list of orders associated with this coffee

    def customers(self) -> list['Customer']:
        """
        Returns a list of unique customers who have ordered this coffee.

        Returns:
            List[Customer]: A list of unique Customer instances.
        """
        # Use a set to avoid duplicate customers and return a list of all unique customers who ordered this coffee
        return list({order.customer for order in self._orders})

    def num_orders(self) -> int:
        """
        Calculates the total number of orders for this coffee.

        Returns:
            int: The total number of orders.
        """
        return len(self._orders)  # Return the number of orders in the list

    def average_price(self) -> float:
        """
        Calculates the average price of this coffee based on all orders.

        Returns:
            float: The average price of this coffee, or 0 if there are no orders.
        """
        if not self._orders:  # Check if there are no orders
            return 0  # Return 0 if there are no orders
        # Calculate the total price of all orders and divide by the number of orders to get the average
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)

    def add_order(self, order: 'Order'):
        """
        Adds a new order to this coffee's order list.

        Args:
            order (Order): The Order instance to be added.
        """
        self._orders.append(order)  # Append the order to the list of orders

    def __str__(self) -> str:
        """
        Returns a string representation of the Coffee instance.

        Returns:
            str: A string containing the coffee's name.
        """
        return f"Coffee: {self._name}"  # Return a readable string representation of the Coffee object
