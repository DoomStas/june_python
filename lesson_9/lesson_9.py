# Task 1

def tax (money, rate):
    tax = (money * rate) / 100
    return tax

money = float(input('Enter your money: '))
rate = float(input('Enter rate: '))

res = tax(money, rate)
print(f'You must pay: {res:.2f}')



# Task 2
import random
import string
def gen_pas(pas):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(pas))
    return password

pas = int(input('Enter lenght password: '))

password = gen_pas(pas)
print({password})

# Task 3

x = range(999, 99, -1)
y = range(999, 99, -1)

palidrome = 0
num_1 = 0
num_2 = 0

def is_palindrome(num):
    return str(num) == str(num)[::-1]

for i in x:
    for j in y:
        gen = i * j
        if is_palindrome(gen) and gen > palidrome:
            palidrome = gen
            num_1 = i
            num_2 = j

print(f'Largest palidrome is {palidrome} received from {num_1} * {num_2}')

# Task 4

from typing import List
import string


def text_to_numbers(text: str) -> List[int]:
    for char in string.punctuation:
        text = text.replace(char, ' ')
    return list(map(int, text.split()))


def is_arithmetic_progression(numbers: List[int]) -> bool:
    if len(numbers) < 2:
        return False

    d = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] - numbers[i - 1] != d:
            return False
    return True


def is_geometric_progression(numbers: List[int]) -> bool:
    if len(numbers) < 2:
        return False

    q = numbers[1] // numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] // numbers[i - 1] != q:
            return False
    return True


def next_arihmetic_number(numbers: List[int]) -> int:
    d = numbers[1] - numbers[0]
    return numbers[-1] + d


def next_geometric_number(numbers: List[int]) -> int:
    q = numbers[1] // numbers[0]
    return numbers[-1] * q


def base(numbers: List[int]) -> int:
    if is_arithmetic_progression(numbers):
        return next_arihmetic_number(numbers)

    if is_geometric_progression(numbers):
        return next_geometric_number(numbers)

    return None


def main():
    text = input("Enter a list of numbers separated by a space: ")
    numbers = text_to_numbers(text)
    res = base(numbers)
    if res:
        print(f"The next number in the sequence is: {res}")
    else:
        print(f"The sequence is not defined by an arithmetic or geometric progression.")


if __name__ == "__main__":
    main()


# Task 5

from num2words import num2words

def words(money):
    dollars, cent = map(int, money.split(','))
    dollars_in_word = num2words(dollars)
    cents_in_word = num2words(cent)
    res = f'{dollars_in_word} dollars {cents_in_word} cents'
    return res

money = input('Enter yor maney: ').strip()

print(words(money))




# Klass work

data_2 = [
    '1 Bob Simson 19.58$ decorations',
    '2 Mary 66.7$ food',
    '3 Mary 98.91$ toys',
    '4 Aleksa 72.29$ drinks',
    '5 Maria Simson 84.48$ food',
    '6 Aleksa 100.41$ accessories',
    '7 Mary 19.9$ accessories',
    '8 Bob Simson 83.88$ drinks',
    '9 Bob Simson 58.21$ instruments',
    '10 Maria Simson 20.61$ accessories',
]

data_1 = [
    '1 Bob Simson 23.58$ decorations',
    '2 Mary 34.7$ food',
    '3 Mary 45.91$ toys',
    '4 Aleksa 72.29$ drinks',
    '5 Maria Simson 84.48$ food',
    '6 Aleksa 100.41$ accessories',
    '7 Mary 19.9$ accessories',
    '8 Bob Simson 83.88$ drinks',
    '9 Bob Simson 58.21$ instruments',
    '10 Maria Simson 20.61$ accessories',
]


def expenses_by_category(data):
    expenses = {}
    for item in data:
        item = item.split()
        *_, money, category = item
        money = float(money.replace('$', ''))
        expenses[category] = expenses.get(category, 0) + money

    return expenses


res = expenses_by_category(data_1)
print(res)
res = expenses_by_category(data_2)
print(res)



# Klass work

import random

def add(*args, **kwargs):
    total = 0
    for arg in args:
        if isinstance(arg, int) and arg % 2:
            total += arg
    return total

print(add(1, 2, 3, 4, 5, 6, 7, a=1, b=2,c=3))

# Task 1
def salary(amount: int | float, tax_rate: int | float) -> int | float:
    """
    Returns the salary after tax deduction.
    :param amount: The amount of money
    :param tax_rate: The tax rate
    :return: The salary after tax deduction
    """
    if not isinstance(amount, int | float):
        raise TypeError('amount must be an int or float')
    if not isinstance(tax_rate, int | float):
        raise TypeError('tax_rate must be an int or float')
    if amount < 0:
        raise ValueError('amount must be a positive number')
    if tax_rate < 0 or tax_rate > 1:
        raise ValueError('tax_rate must be between 0 and 1')

    return amount - amount * tax_rate


# print(salary(1000, 0.1))
# print(salary(1000, 1.2))
# print(salary(1000, '0.5'))


# Task 2
def password_gen(length: int, special: bool = False) -> str:
    """
    Returns a password of the given length.
    :param length: The length of the password
    :param special: Whether to include special characters
    :return: The generated password
    """
    import random
    import string

    if not isinstance(length, int):
        raise TypeError('length must be an int')
    if length < 2:
        raise ValueError('length must be at least 2')

    chars = string.ascii_letters + string.digits + string.punctuation if special else ''
    return ''.join(random.sample(chars, length))


# Task 3
def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def max_palindrom(start=100, stop=1000):
    res = []
    for i in range(start, stop):
        for j in range(i, stop):
            if is_palindrome(str(i * j)):
                res.append((i * j, i, j))

    return max(res, key=lambda tpl: tpl[0])


res = max_palindrom()
print(res)

#Bonus task

from typing import List

def is_odd(item):
    return item % 2

def is_neg(item):
    return item < 0

def filter(x: List[int], func):
    res = []
    for item in x:
        if func(item):
            res.append(item)
    return res

x = [1, -2, 3, -4, 5, -6, 7, 8]
print(filter(x, is_odd))
print(filter(x, is_neg))
print(filter(x, lambda item: item % 2 == 0))
print(filter(x, lambda item: item > 0))
