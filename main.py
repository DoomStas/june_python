# Task 1
name = input("Name: ")
print(f"Hello, {name}!")


# Task 2

number_1 = int(input("Enter the numbers: "))
number_2 = int(input("Enter the numbers: "))
number_3 = int(input("Enter the numbers: "))
number_4 = int(input("Enter the numbers: "))
number_5 = int(input("Enter the numbers: "))

min_num = min(number_1, number_2, number_3, number_4, number_5)
max_num = max(number_1, number_2, number_3, number_4, number_5)
average_num = (number_1 + number_2 + number_3 + number_4 + number_5)/ 5

print(f"Минимальное значение: {min_num}")
print(f"Максимальное значение: {max_num}")
print(f"Среднее значение: {average_num}")



# Task 3

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)


# Task 4

import math
radius = float(input("Enter radius: "))

diameter = 2 * radius
circumference = 2 * radius * math.pi
area = math.pi * radius**2

print(f"Диаметр: {diameter}")
print(f"Длина: {circumference}")
print(f"Площадь: {area}")

# Task 5

p = 1000
r = 0.10

year_10 = 10
year_20 = 20
year_30 = 30

a_10 = p * (1 + r) ** year_10
a_20 = p * (1 + r) ** year_20
a_30 = p * (1 + r) ** year_30

print(f"Депозит через {year_10} лет: {a_10:.2f} $")
print(f"Депозит через {year_20} лет: {a_20:.2f} $")
print(f"Депозит через {year_30} лет: {a_30:.2f} $")

# Task 6

dolars = int(input("Введите сумму для конвертации: "))

ua= dolars * 40.64

print(f"При обмене Вы получите: {ua:.2f} гривен")

# Task 7

num = int(input("Введите трехзначное число: "))

print(num // 100)
print(num // 10 % 10)
print(num % 10)