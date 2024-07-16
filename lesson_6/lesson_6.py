# Task 1

x = input("Enter text: ")
i = 0
for lit in x:
    if lit == "b":
        i += 1
print(i)




# Task 3

x = input("Enter text")
sum_cod = 0
for i in x:
    sum_cod += ord(i)
print(sum_cod)


# Task 4
import math

PI = math.pi

for i in range(2, 12):
    print(f"{PI:.{i}f}")



# Task 5

x = input(" Enter text: ")
y = x.split()
print(max(y))

















# Klass work

text = input("Enter text")

while "  " in text:
    text = text.replace("  ", " ")
print({text})

# Klass work v2

x = input("Enter text")
res = x.split()
print(res)

# Klass work v3

text = input("Enter text")
res = " ".join(text.split())
print(res)


# Klass work v4
import string
text = input("Enter text")
for item in string.punctuation:
    text=text.replace(item, " ")
res = " ".join(text.split())
print(res)


# Klass work 2

import string

text = input("Enter text: ")
for item in string.punctuation:
    text = text.replace(item, " ")
res = text.split()
print(len(res))