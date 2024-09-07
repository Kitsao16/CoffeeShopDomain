from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customer.customer import Customer  # Import Customer class for type hints
    from coffee.coffee import Coffee  # Import Coffee class for type hints


class Order:
    # Define the minimum and maximum valid price for an order
    MIN_PRICE = 1.0
    MAX_PRICE = 10.0

    def __init__(self, customer: 'Customer', coffee: 'Coffee', price: float):
        """
        Initializes a new Order instance with customer, coffee, and price details.

        Args:
            customer (Customer): The customer placing the order.
            coffee (Coffee): The coffee being ordered.
            price (float): The price of the order.

        Raises:
            ValueError: If customer or coffee are not the correct types or if price is invalid.
        """
        from customer.customer import Customer  # Local import to avoid circular import
        from coffee.coffee import Coffee  # Local import to avoid circular import

        # Ensure customer is a valid Customer instance
        if not isinstance(customer, Customer):
            raise ValueError("customer must be of type Customer.")

        # Ensure coffee is a valid Coffee instance
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be of type Coffee.")

        # Ensure price is within the allowed range
        if not isinstance(price, float) or not (self.MIN_PRICE <= price <= self.MAX_PRICE):
            raise ValueError(f"Price must be a float between {self.MIN_PRICE} and {self.MAX_PRICE}.")

        # Assign the validated customer, coffee, and price to private attributes
        self._customer = customer
        self._coffee = coffee
        self._price = price
        self.order_date = datetime.now()  # Record the current date and time for the order

        # Link this order back to the customer and coffee (add this order to their respective lists)
        customer.add_order(self)
        coffee.add_order(self)

    @property
    def customer(self) -> 'Customer':
        """
        Retrieves the customer who placed this order.

        Returns:
            Customer: The customer who placed the order.
        """
        return self._customer  # Return the customer associated with this order

    @property
    def coffee(self) -> 'Coffee':
        """
        Retrieves the coffee in this order.

        Returns:
            Coffee: The coffee that was ordered.
        """
        return self._coffee  # Return the coffee associated with this order

    @property
    def price(self) -> float:
        """
        Retrieves the price of this order.

        Returns:
            float: The price of the order.
        """
        return self._price  # Return the price of this order

    def __str__(self) -> str:
        """
        Returns a string representation of the Order instance.

        Returns:
            str: A string containing the order details.
        """
        # Return a readable string representation of the order, including customer, coffee, and price
        return f"Order({self._customer.name}, {self._coffee.name}, ${self._price:.2f})"
