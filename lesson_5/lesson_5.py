# Task 1

for i in range(7, 101, 7):
    print(i)

# Task 2
summa = 0
count = 0

for i in range(1, 100):
    if i % 2:
        summa +=i
        count +=1

print(f"Sum of unpaired numbers: {summa}, Numbers of unpaired: {count}")

#Task 3

i = 1
count = 0

while i <= 200:
    print(i, end=" ")
    count += 1
    if count % 5 == 0:
        print()
    i += 1


# Task 4

n = int(input("Enter a number: "))
factorial = 1

if factorial < 0:
    print("Error")
else:
    for i in range(2, n + 1):
        factorial *= i
    print(factorial)             


# Task 5

for i in range(1, 11):
    print(f"{i} x 5 = {i * 5}")

# Task 6

height = int(input("Enter height: "))
width = int(input("Enter width: "))

for i in range(height):
    for j in range(width):
        print("*", end="")
    print()


# Task 6_2

width, height = int(input("Enter width")), int(input("Enter height"))

res = f"{"*" * width}\n" + f"*{" " * (width - 2)}*\n" * (height - 2) + f"{"*" * width}\n"
print(res)


# Task 7

n = [0, 5, 2, 4, 7, 1, 3, 19]
count = 0
for item in n:
    for digit in str(item):
        if int(digit) % 2:
            count += 1
print(count)



#Task 8

x = [4, 7, 9, 11]

y = x + [2 * i for i in x]
print(y)

# Task 9

salary = []

while len(salary) <12:
    s = int(input("Enter the salary:"))
    if s <= 0:
        print("Salary cannot be negative or zero")
        continue
    salary.append(s)
print(f"Averge salary: {sum(salary) / len(salary)}")

# Task 9_2

import random
salary = [random.randint(1_000, 5_000) for _ in range(12)]
print(salary)
print(f'Avg: {sum(salary) / len(salary):.2f}')


# Task 10

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
s = 0
for i in range(3):
    for j in range(3):
        s += a[i][j]
print(s)



# Task 10_2

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = 0
for row in a:
    s += sum(row)
    print(*row, sep='\t')
print(s)


# Task 11

i = input("Enter list: ")
i = i.split()
i.reverse()
print(i)


# Task 11_2

i = input("Enter list: ")
for item in reversed(i):
    print(item)



# Task 12

res = []
for n in range(2, 100):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        res.append(n)
print(res)


# Task 13


x = int(input("Enter number: "))




stars = int(input("Enter the number of stars: "))
spaces = 0
res = []

if x % 2 == 0:
    print("Error")

for i in range(stars, 0, -2):
    res.append(f"{' ' * spaces}{'*' * i}")
    spaces += 1

res += res[-2::-1]
print("\n".join(res))


# Klass work

month = ("Jan", "Feb", "Mar", "Apr", "Maj", "June")
salery = []
salery.append(1000)
salery.append(2000)
salery.append(3000)
salery.append(4000)
salery.append(5000)
salery.append(6000)

print(f'Minimum salary: {min(salery)}')
print(f"Maximum salary: {max(salery)}")
print(f"Averge salary: {sum(salery) / len(salery)}")

min_index = salery.index(min(salery))
max_index = salery.index(max(salery))

print(f"Minimum salary month: {month[max_index]}")
print(f"Maximum salery month: {month[max_index]}")



#Klass work 2

salary = []

while len(salery) <6:
    s = int(input("Enter the salary:"))
    if s > 0:
        salary.append(s)
print("Salaries are: ", salary)



#Klass work 2_2

salary = []

while len(salery) <6:
    s = int(input("Enter the salary:"))
    if s <= 0:
        print("Salary cannot be negative or zero")
        continue
    salary.append(s)
print("Salaries are: ", salary)




#Klass work 2_3

salary = []

while len(salery) <6:
    s = int(input("Enter the salary:"))
    if s <= 0:
        print("Salary cannot be negative or zero")
        break
    salary.append(s)
else:
    print("You have entered 6 salaries successfully!")
print("Salaries are: ", salary)

#Klass work 3

salary = []
while True:
    ans = input("Enter dslary or stop: ")
    if ans == "stop":
        break
    salary.append(int(ans))
print("Salsries: ", salary)


# Klass work 4

x = "Hello"

for item in x:
    print(item)

# Klass work 5

for i in range(10):
    print(i)


# Klass work 6

x = [1, 2, 3, 4, 5, 6, 7]

for index, item in enumerate(x):
    print(index, item)

# Klass work 7

x = [1, 2, 3, 4, 5, 6, 7]

y = []
for item in x:
    y.append(item * 3)

print(y)

# Klass work 7_2

x = [1, 2, 3, 4, 5, 6, 7]

y = [item * 3 for item in x]
print(y)


