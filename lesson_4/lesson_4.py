# Task 1
ticket = input("Enter your numbers ticket: ")
ticket = list(map(int, ticket))

if len(ticket) % 2:
    print("Error")
else:
    mid = len(ticket) // 2
    firs_halh = ticket[:mid]
    two_half = ticket[mid:]
    res = "You win" if sum(firs_halh) == sum(two_half) else "You lose"
    print(res)


# Task 2

numbers = input("Enter text: ")
res = "Ok" if numbers == numbers[::-1] else "Not ok"
print(res)



# Task 3

r = int(input("Enter radius: "))
x, y = map(int, input("Enter coordinates: ").split())
d = (x**2 + y**2) ** 0.5
if d <= r:
    print("Your coordinates in radius")
else:
    print("Your coordinates is not in radius")



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