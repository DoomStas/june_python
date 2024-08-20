import logging
from exceptions import InvalidPriceError

class LoggingMixin:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(f'{self.__class__.__name__}.log')
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def log(self, message):
        self.logger.debug(message)

class Product(LoggingMixin):
    """
    Class for product representation.
    """
    def __init__(self, product_name, description_product, price_product: float):
        super().__init__()
        if not isinstance(price_product, (int, float)):
            raise TypeError('Price must be a number')
        if price_product <= 0:
            self.log(f'Attempted to set invalid price for {product_name}: ${price_product:.2f}')
            raise InvalidPriceError(price_product)
        self.product_name = product_name
        self.description_product = description_product
        self.price_product = price_product
        self.log(f'Created {self}')

    def __str__(self):
        return f'{self.product_name} - {self.description_product}: ${self.price_product:.2f}'

    def set_price(self, new_price: float):
        if new_price <= 0:
            self.log(f"Attempted to set invalid price for {self.product_name}: ${new_price:.2f}")
            raise InvalidPriceError(new_price)
        self.price_product = new_price
        self.log(f"Price updated for {self.product_name} to ${new_price:.2f}")

    def __eq__(self, other):
        return (self.product_name == other.product_name and
                self.description_product == other.description_product and
                self.price_product == other.price_product)

    def __hash__(self):
        return hash((self.product_name, self.description_product, self.price_product))