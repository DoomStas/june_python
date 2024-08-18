class Discount:
    def apply(self, price: float):
        raise NotImplementedError('Method apply must be implemented in subclasses')

class PercentageDiscount(Discount):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply(self, price: float):
        discount_amount = price * (self.percentage / 100)
        return price - discount_amount

class FixedAmountDiscount(Discount):
    def __init__(self, amount: float):
        self.amount = amount

    def apply(self, price: float):
        return max(0, price - self.amount)
