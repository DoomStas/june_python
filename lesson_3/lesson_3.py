# Task 1

apart = int(input("Enter number of apartment: "))
if  apart < 1 or apart > 144:
    print("Error")

apart_on_floar = 4
floar = 9
entrance = 4

res_entrance = (apart-1) // (apart_on_floar*floar) + 1
res_floar = ((apart-1) % (apart_on_floar * floar)) // apart_on_floar + 1
num_on_floar = ((apart-1) % (apart_on_floar * floar)) % apart_on_floar + 1

print (f"Your entrance is: {res_entrance}")
print (f"Your floar is: {res_floar}")
print (f"Your number on floar is: {num_on_floar}")


# Task 2

year = int(input("Enter the year: "))
high_year = "366" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "365"
print(high_year)



# Task 3

a = int(input("Size 1: "))
b = int(input("Size 2: "))
c = int(input("Size 3: "))

if a + b > c and b + c > a and c + a > b:
    print("Triagle exists")
else:
    print("Triagle not exists")


# Task 4
user_password = "Qwerty1234"
pas = input("Enter the password: ")
if pas == user_password:
    print("Password OK")
else:
    print ("Password error")

# Task 5

money = int(input("Sum you buy: "))
if money > 1000:
    res = money - (money * 0.1)
    print(f"Pay {res} $")
else:
    print(f"Pay {money} $")


# Task 6

month = int(input("Enter number of month: "))
if month < 1 or month > 12:
    print("Error")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31 days")
elif month == 2:
    print("If this hight year is - 28 days, if not - 29 days")
else:
    print("30 days")


# Task 7

rei = int(input("Enter your grade (1-5): "))
if rei < 1 or rei > 5:
    print("Error")
elif rei == 1:
    print("Жахливо")
elif rei == 2:
    print("Погано")
elif rei == 3:
    print("Задовільно")
elif rei == 4:
    print("Добре")
else:
    print("Відмінно")

# Task 8

mass = float(input("Enter your masses (kg): "))
height = float(input("Enter your height (met): "))

bmi = mass / (height ** 2)

if bmi < 18:
    print("Недостатньо ваги")
elif bmi <= 25:
    print("Нормальна вага")
elif bmi <= 40:
    print("Надлишкова вага")
else:
    print("Ожиріння")