#Task 1

def generator(func, start, n):
    for _ in range(n):
        yield start
        start = func(start)
def arithmetic(x):
    return x + 2

gen = generator(arithmetic,1, 20)

for value in gen:
    print(value)
    if value >= 15:
        break



# Task 2

import time

def memoize(y):
    cach = {}
    def memoize_function(x):
        if x not in cach:
            cach[x] = y(x)
        return cach[x]
    return memoize_function

def fibonacci(z):
    return z if z <= 1 else fibonacci(z-1) + fibonacci(z-2)

z = 40

start_time = time.time()
print(f'z={z} {fibonacci(z)}')
print(f'{time.time() - start_time}')

fibonacci_memoized = memoize(fibonacci)

start_time = time.time()
print(f'z={z} {fibonacci(z)}')
print({time.time() - start_time})


#Task 3

def function_sum(num, func):
    return sum(func(x) for x in num)

def square(x):
    return x ** 2

num = [1, 2, 3, 4]
res = function_sum(num, square)
print(res)