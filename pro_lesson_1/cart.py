from exceptions import InvalidQuantityError
from product import LoggingMixin, Product
from discount import PercentageDiscount, FixedAmountDiscount
from math import gcd
class DiscountMixin:
    def apply_discount(self, discount: PercentageDiscount | FixedAmountDiscount):
        for product in self.products:
            new_price = discount.apply(self.products[product] * product.price_product)
            product.price_product = new_price / self.products[product]

class Cart(DiscountMixin, LoggingMixin):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.products = {}
        self.log(f'Created {title}')

    def add_product(self, product: Product, quantity: int | float = 1):
        if quantity <= 0:
            self.log(f'Attempted to add invalid quantity for {product.product_name}: {quantity}')
            raise InvalidQuantityError(quantity)
        if isinstance(product, Product):
            if product in self.products:
                self.products[product] += quantity
            else:
                self.products[product] = quantity
        self.log(f"Added {quantity} of {product.product_name} to the cart.")

    def cost(self):
        return sum(product.price_product * quantity for product, quantity in self.products.items())

    def pay(self, payment_processor):
        total_cost = self.cost()
        payment_processor.pay(total_cost)
        self.log(f"Payment processed for a total of ${total_cost:.2f} using {payment_processor}")

    def __iadd__(self, other_cart):
        if isinstance(other_cart, Cart):
            for product, quantity in other_cart.products.items():
                if product in self.products:
                    self.products[product] += quantity
                else:
                    self.products[product] = quantity
            self.log(f'Cart "{self.title}" combined with cart "{other_cart.title}"')
        else:
            raise TypeError("Can only combine with another Cart instance")
        return self

    def __iter__(self):
        self._iter_index = 0
        self._iter_products = list(self.products.items())
        return self

    def __next__(self):
        if self._iter_index < len(self._iter_products):
            product, quantity = self._iter_products[self._iter_index]
            self._iter_index += 1
            return product, quantity
        else:
            raise StopIteration

    def __str__(self):
        cart_content = [f'{product} x {quantity}' for product, quantity in self.products.items()]
        total = f'Total cost: ${self.cost():.2f}'
        return '\n'.join(cart_content) + '\n' + total

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        common_divisor = gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return int(self.__float__())

    def __eq__(self, other):
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __lt__(self, other):
        return (self.numerator * other.denominator <
                other.numerator * self.denominator)

    def __le__(self, other):
        return (self.numerator * other.denominator <=
                other.numerator * self.denominator)

    def __gt__(self, other):
        return (self.numerator * other.denominator >
                other.numerator * self.denominator)

    def __ge__(self, other):
        return (self.numerator * other.denominator >=
                other.numerator * self.denominator)

    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator +
                         other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = (self.numerator * other.denominator -
                         other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
