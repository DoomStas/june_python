#Task 2

def geometric_progression (x, y):
    while True:
        yield x
        x*=y
progression = geometric_progression(7, 12)

for _ in range(10):
    print(next(progression))


# Task 3

def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop =0, start
    if step == 0:
        raise ValueError('Step must be > 0')
    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step

for i in my_range(4, 14, 2):
    print(i)


# Task 4

def numbers(lim):
    for num in range(2, lim):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num

for prime in numbers(20):
    print(prime)

# Task 5

from datetime import datetime, timedelta

def date_range(start_date, end_date):
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    while current_date < end_date:
        yield current_date.strftime('%Y-%m-%d')
        current_date += timedelta(days=1)

for date in date_range('1990-03-21', '2024-08-27'):
    print(date)