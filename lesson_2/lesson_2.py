# Task 1

num = int(input("Enter a negative number: "))
if num < 0:
    print(f"Your number is {num}")
else:
    print(f"This is not negative number")


# Task 2

num = int(input("Enter a number: "))
(num < 20 and print(f"{num} is lass than 20."))
(num >= 20 and print(f"{num} is not lass than 20."))


# Task 3

num = int(input("Enter a number: "))
(num == 0 and print(f"{num} is equals 0"))
(num !=0 and print(f"{num} is not equals 0"))


# Task 4

num = int(input("Enter a number: "))
res = (num % 2 == 0 and "paired number" or "unpaired number")
print(f"{num} is {res}")


# Task 5

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
num_3 = int(input("Enter a number: "))

(num_1 >= num_2 and num_1 >= num_3 and print(num_1) or num_2 >= num_1 and num_2>= num_3 and print(num_2) or num_3 >= num_1 and num_3 >= num_2 and print(num_3))


# Task 6

qa = input("Do you have driver licence? (yes/no): ")
(qa == "yes" and print("Ви можете керувати автомобілем") or qa == "no" and print("Ви не можете керувати автомобілем"))

# Task 7

qa = int(input("Enter your age: "))
(qa >= 18 and print("Ви можете отримати посвідчення водія") or qa < 18 and print("Ви не відповідаєте критеріям для отримання посвідчення водія"))


# Task 8

num = int(input("Enter a number: "))
res = (num % 2 == 0 and num > 0 and "Число є додатнім і парним") or "Число не задовольняє критерії"
print(res)


# Task 9
num = int(input("Enter a number: "))
res = (num % 3 == 0 and num % 5 != 0 and "Число підходить") or "Число не підходить"
print(res)