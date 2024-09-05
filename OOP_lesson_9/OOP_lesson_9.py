# Task 1

class Account:
    def __init__(self, initial):
        self._balance = initial

    @property
    def balance(self):
        return self._balance

    def __setattr__(self, name, value):
        if name == '_balance':
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'Cannot be changed "{name}"')

    def __getattr__(self, name):
        return f'Property "{name}" does not exist'

acc = Account(100)
print(acc.balance)

try:
    acc.balance = 200
except AttributeError as x:
    print(x)

print(acc.not_exxisting)


# Task 2


class User:
    def __init__(self, first_name, last_name):
        self._first_name, self._last_name = first_name, last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def __setattr__(self, name, value):
        if name in {'_first_name', '_last_name'}:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'Cannot modify "{name}"')

    def __getattr__(self, name):
            return f'Property "{name}" does not exist'

user = User('Jan', 'Kowalski')
print(user.first_name)
print(user.last_name)

try:
    user.first_name = 'Stas'
except AttributeError as x:
    print(x)

print(user.age)


#Task 3


class Rectangle:
    def __init__(self, width, height):
        self._width, self._height = width, height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __setattr__(self, name, value):
        if name in {'_width','_height'}:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'Cannot modify "{name}"')

    def __getattr__(self, name):
        return f'Property "{name}" does not exist'

    def area(self):
        return self._width * self._height

rec = Rectangle(5, 10)
print(rec.width, rec.height)
print(rec.area())

try:
    rec.width = 20
except AttributeError as x:
    print(x)

print(rec.square)