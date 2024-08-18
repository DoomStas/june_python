from exceptions import InvalidQuantityError
from product import LoggingMixin, Product
from discount import Discount

class DiscountMixin:
    def apply_discount(self, discount: Discount):
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

    def __str__(self):
        cart_content = [f'{product} x {quantity}' for product, quantity in self.products.items()]
        total = f'Total cost: ${self.cost():.2f}'
        return '\n'.join(cart_content) + '\n' + total
