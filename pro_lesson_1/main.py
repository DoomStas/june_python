from product import Product
from cart import Cart
from discount import PercentageDiscount, FixedAmountDiscount
from payment import CreditCardProcessor, PayPalProcessor, BankTransferProcessor

if __name__ == "__main__":
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
        discount = PercentageDiscount(percentage)
    elif discount_type == 'fixed':
        amount = float(input("Enter discount amount: "))
        discount = FixedAmountDiscount(amount)
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
        processor = CreditCardProcessor()
    elif choice == 2:
        processor = PayPalProcessor()
    elif choice == 3:
        processor = BankTransferProcessor()
    else:
        print("Error")
        processor = None

    if processor:
        you_cart.pay(processor)
