class PaymentProcessor:
    def pay(self, amount: float):
        raise NotImplementedError('Method pay must be implemented in subclasses')

class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount: float):
        print(f'Credit card payment in the amount of {amount:.2f} was successful.')

class PayPalProcessor(PaymentProcessor):
    def pay(self, amount: float):
        print(f'PayPal payment for ${amount:.2f} was successful.')

class BankTransferProcessor(PaymentProcessor):
    def pay(self, amount: float):
        print(f'Payment via bank transfer in the amount of ${amount:.2f} was successful.')
