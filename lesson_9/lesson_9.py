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