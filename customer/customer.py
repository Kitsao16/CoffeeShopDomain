from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from order.order import Order  # Import Order class for type hints
    from coffee.coffee import Coffee  # Import Coffee class for type hints


class Customer:
    def __init__(self, name: str):
        """
        Initializes a new Customer instance with a name and an empty list of orders.

        Args:
            name (str): The name of the customer.

        Raises:
            ValueError: If the name is not a valid string between 1 and 15 characters.
        """
        self._name = None  # Initialize private name attribute
        self.name = name  # Use the property setter to validate and assign the name
        self._orders = []  # List to store the customer's orders

    @property
    def name(self) -> str:
        """
        Retrieves the customer's name.

        Returns:
            str: The customer's name.
        """
        return self._name  # Return the private name attribute

    @name.setter
    def name(self, name: str):
        """
        Sets the customer's name with validation.

        Args:
            name (str): The name to assign to the customer.

        Raises:
            ValueError: If the name is not a string or not between 1 and 15 characters.
        """
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name  # Assign the valid name
        else:
            raise ValueError("Customer name must be a string between 1 and 15 characters.")

    def orders(self) -> list['Order']:
        """
        Returns a list of all orders made by the customer.

        Returns:
            List[Order]: A list of Order instances.
        """
        return self._orders  # Return the list of orders made by the customer

    def coffees(self) -> list['Coffee']:
        """
        Returns a list of unique coffees the customer has ordered.

        Returns:
            List[Coffee]: A list of unique Coffee instances.
        """
        return list({order.coffee for order in self._orders})  # Return unique coffees

    def create_order(self, coffee: 'Coffee', price: float) -> 'Order':
        """
        Creates a new Order for the customer.

        Args:
            coffee (Coffee): The coffee to be ordered.
            price (float): The price of the coffee.

        Returns:
            Order: The newly created Order instance.
        """
        from order.order import Order  # Local import to avoid circular dependency
        order = Order(self, coffee, price)  # Create a new Order instance
        self.add_order(order)  # Add the new order to the customer's order list
        return order  # Return the created order

    def add_order(self, order: 'Order'):
        """
        Adds an order to the customer's order list.

        Args:
            order (Order): The Order instance to add.
        """
        self._orders.append(order)  # Append the new order to the list of orders

    def __str__(self) -> str:
        """
        Returns a string representation of the Customer instance.

        Returns:
            str: A string containing the customer's name.
        """
        return f"Customer: {self._name}"  # Return a readable string representation of the Customer object
