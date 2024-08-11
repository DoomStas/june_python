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

class Product:
    """
    Class for product representation.
    """
    def __init__(self, product_name, description_product, price_product: int | float):
        self.product_name = product_name
        self.description_product = description_product
        self.price_product = price_product

    def __str__(self):
        return f'{self.product_name} - {self.description_product}: ${self.price_product:.2f}'


class Cart(DiscountMixin):

    def __init__(self, title):
        self.title = title
        self.products = {}

    def add_product(self,product: Product, quantity: int | float =1):
        isinstance(product, Product) and (product in self.products and self.products.update
        ({product: self.products[product] + quantity}) or self.products.update({product: quantity}))

    def cost(self):
        return sum(product.price_product * quantity for product, quantity in self.products.items())

    def pay(self, payment_processor):
        total_cost = self.cost()
        payment_processor.pay(total_cost)

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