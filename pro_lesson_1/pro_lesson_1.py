import datetime


class Discount:
    def apply(self, price: float):
        raise NotImplementedError('Method apply is guilty of re-assignments in similar classes')

class Percentage_Discount(Discount):
    def __init__(self, percentage: float):
        self.percentege = percentage
    def apply(self, price: float):
        discount_amount = price * (self.percentege / 100)
        return price - discount_amount

class Fixid_Amount_Discount(Discount):
    def __init__(self, amount: float):
        self.amount = amount
    def apply(self, price: float):
        return max(0, price - self.amount)

class LogginMixin:
    def log(self, message: str):
        stamp = datetime.datetime.now().strftime("%d %B %Y, %I:%M:%S %p")
        log_message = f'[{stamp}] {message}'
        print(log_message)
        with open('log.txt', 'a') as log_file:
            log_file.write(log_message + 'n')
class DiscountMixin:
    def apply_discount(self, discount: Discount):
        for product in self.products:
            new_price = discount.apply(self.products[product] * product.price_product)
            product.price_product = new_price / self.products[product]

class PaymentProcessor:
    def pay(self, amount: float):
        raise NotImplementedError('Method pay is guilty of re-assignments in similar classes')

class Credit_Card_Processor(PaymentProcessor):
    def pay(self, amount: float):
        print(f'Credit card payment in the amount of {amount:.2f} was successful.')

class Pay_Pal_Processor(PaymentProcessor):
    def pay(self, amount: float):
        print(f'PayPal payment for ${amount:.2f} was successful.')

class Bank_Transfer_Processor(PaymentProcessor):
    def pay(self, amount: float):
        print(f'Payment via bank transfer in the amount of ${amount:.2f} was successful.')

class InvalidPriceError(Exception):
    def __init__(self, price):
        super().__init__(f'Invalid price: {price} The price must be a positive number')
class Product(LogginMixin):
    """
    Class for product representation.
    """
    def __init__(self, product_name, description_product, price_product: int | float):
        if price_product <=0:
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
class InvalidQuantityError(Exception):
    def __init__(self, quantity):
        super().__init__(f'Invalid quantity {quantity}')

class Cart(DiscountMixin, LogginMixin):

    def __init__(self, title):
        self.title = title
        self.products = {}
        self.log(f'Create {title}')

    def add_product(self,product: Product, quantity: int | float =1):
        if quantity <=0:
            self.log(f'Attempted to add invalid quantity for {product.product_name}: {quantity}')
            raise InvalidQuantityError(quantity)
        isinstance(product, Product) and (product in self.products and self.products.update
        ({product: self.products[product] + quantity}) or self.products.update({product: quantity}))
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



you_cart = Cart('Cart')
while input('Do you want to add a product? (y/n) ').lower().strip() == 'y':
    product_name = input('Enter product name: ').strip().title()
    description_product = input('Enter description product: ').strip().title()
    price_product = float(input('Enter price product: ').strip())
    quantity = int(input('Enter quantity: ').strip())
    product = Product(product_name, description_product, price_product)
    you_cart.add_product(product, quantity)

print(you_cart)

discount_type = input("\nSelect discount type (percentage/fixed): ").strip().lower()
if discount_type == 'percentage':
    percentage = float(input("Enter discount percentage: "))
    discount = Percentage_Discount(percentage)
elif discount_type == 'fixed':
    amount = float(input("Enter discount amount: "))
    discount = Fixid_Amount_Discount(amount)
else:
    discount = None

if discount:
    you_cart.apply_discount(discount)

print("\nCart after discount: ")
print(you_cart)

print('Select payment method: ')
print("1: Credit Card")
print("2: PayPal")
print("3: Bank Transfer")
choice = int(input("Enter your choice: ").strip())

if choice == 1:
    processor = Credit_Card_Processor()
elif choice == 2:
    processor = Pay_Pal_Processor()
elif choice == 3:
    processor = Bank_Transfer_Processor()
else:
    print("Error")
    processor = None

if processor:
    you_cart.pay(processor)