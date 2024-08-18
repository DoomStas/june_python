class InvalidPriceError(Exception):
    def __init__(self, price):
        super().__init__(f'Invalid price: {price}. The price must be a positive number.')

class InvalidQuantityError(Exception):
    def __init__(self, quantity):
        super().__init__(f'Invalid quantity: {quantity}. Quantity must be a positive number.')
