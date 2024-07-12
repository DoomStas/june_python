# Task 1
ticket = input("Enter your 4 numbers ticket: ")
ticket = list(map(int, ticket))

if len(ticket) != 4:
    print("Error")
else:
    firs_halh = ticket[0:1]
    two_half = ticket[2:3]
    res = "You win" if sum(firs_halh) == sum(two_half) else "You lose"
    print(res)

# Task 1 Teacher

ticket_number = input("Enter ticket number: ")
ticket_number = list(map(int, ticket_number))

if len(ticket_number) % 2:
    print("Invalid ticket number")
else:
    mid = len(ticket_number) // 2
    first_half = ticket_number[:mid]
    second_half = ticket_number[mid:]

    res = "Lucky ticket" if sum(first_half) == sum(second_half) else "Unlucky ticket"
    print(res)



# Task 2

numbers = input("Enter 6 numbers: ")
numbers = list(map(int, numbers))
if len(numbers) != 6:
    print("Error")
else:
    if numbers == numbers [::-1]:
        print ("Ok")
    else:
        print("No ok")


# Task 2 Teacher

text = input("Enter text: ")
res = "Palindrome" if text == text[::-1] else "Not palindrome"
print(res)



# Task 3

R = 4

x = int(input("Coordinats X: "))
y = int(input("Coordinats Y: "))

res= "OK" if x**2 + y**2 <= R**2 else "NO OK"

print(res)


# Task 3 Teacher

r = int(input("Enter radius: "))
x, y = map(int, input("Enter coordinates: ").split())
d = (x**2 + y**2) ** 0.5
if d <= r:
    print("Point is inside the circle")
else:
    print("Point is outside the circle")




# Class work

money = int(input("Your money: "))
APPLE = 40
BANANA = 50
TEA = 10

if money < min(APPLE, BANANA, TEA):
    print("Sorry, try next time")
if money >= APPLE:
    money -= APPLE
    print("You buy apple")

if money >= BANANA:
    money -= BANANA
    print("You buy banana")

if money >= TEA:
    money -= TEA
    print("You buy tea")