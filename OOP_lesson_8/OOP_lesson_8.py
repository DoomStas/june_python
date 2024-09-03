# Task 1

def decorator(fun):
    def wrapper(*args, **kwargs):
        print('Before the start')
        res = fun(*args, **kwargs)
        print('End')
        return res
    return wrapper
@decorator
def function():
    print('Function')
function()


#Task 2

import json
import os

def cache_file(file):
    def decorator(func):
        def wrapper(*args):
            cache = json.load(open(file)) if os.path.exists(file) else {}
            key = str(args)
            if key not in cache:
                cache[key] = func(*args)
                json.dump(cache, open(file, 'w'))
            else:
                print('Res cache')
            return cache[key]
        return wrapper
    return decorator
@cache_file('cache.json')
def function(x, y):
    return x * y

print(function(123, 256))
print(function(123, 256))


# Task 3

def handler_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'Error {e}')
            return None
    return wrapper
@handler_exception
def divide(x, y):
    return x / y
print(divide(15,3))
print(divide(20, 2))


# Task 4

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print({time.time() - start_time})
        return res
    return wrapper
@measure_time
def function():
    time.sleep(3)

function()


# Task 5

def log(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res
    return wrapper
@log
def add(a, b):
    return a + b

add( 32, 55)


# Task 6

def limit_calls(max_calls):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if not hasattr(wrapper, 'call_count'):
                wrapper.call_count = 0
            if wrapper.call_count < max_calls:
                wrapper.call_count += 1
                return func(*args, **kwargs)
            print(max_calls)
        return wrapper
    return decorator
@limit_calls(3)
def function(x):
    return x * 2

print(function(1))
print(function(2))
print(function(3))
print(function(4))


#Task 7


def cache_res(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper
@cache_res
def fibomacci(n):
    return n if n <= 1 else fibomacci(n-1) + fibomacci(n-2)

print(fibomacci(100))
print(fibomacci(100))