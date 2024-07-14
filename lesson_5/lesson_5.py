# Task 1

for i in range(7, 101, 7):
    print(i)

# Task 2
summa = 0
count = 0

for i in range(1, 100):
    if i % 2 !=0:
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
    for i in range(1, n+1):
        factorial *= i
    print(f'Factorial {n} is {factorial}')


# Task 5

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in x:
    res = i * 5
    print(f"{i} x 5 = {res}")

# Task 6

height = int(input("Enter height: "))
width = int(input("Enter width: "))

for i in range(height):
    for j in range(width):
        print("*", end="")
    print()

# Task 7

x = [0, 5, 2, 4, 7, 1, 3, 19]

for num in x:
    if num % 2 !=0:
        print(num)


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


# Task 10

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = [9, 10, 11, 12]
j = [13, 14, 15, 16]

res = [x[i] + y[i] + z[i] + j[i] for i in range(len(x))]

print(x, y, z, j, res)



# Task 11

i = input("Enter list: ")
i = i.split()
i.reverse()
print(i)



# Task 12

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


# Task 13


x = int(input("Enter number: "))

if x % 2 == 0:
    print("Error")

else:
    for i in range(x, 0, -2):
        y = (x - i) // 2
        print(" " * y + "*" * i)

    for i in range(3, x + 1, 2):
        y = (x - i) // 2
        print(" " * y + "*" * i)



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


