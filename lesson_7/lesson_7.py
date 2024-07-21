# Task 1

text = input('Enter your text: ')
words = text.split()
res= {}

for word in words:
    if word in res:
        res[word] += 1
    else:
        res[word] = 1
print(res)


# Task 2

translations = {
    'hello': 'привіт',
    'goodbye': 'до побачення',
    'cat': 'кіт',
    'dog': 'собака'
}

text = input('Enter your word: ').strip().lower()

if text in translations:
    print(f'{text} is {translations[text]}')
else:
    print(f'{text} is incorect')


# Task 3
contact = {}
option = input("Enter the option number: 1- add contact, 2 - del. contact, 3 - See number: ").strip()

if option == 1:
    name = input("Enter the name: ").strip()
    telefon = input("Enter the number: ").strip()
    contact[name] = telefon
    print('Number add')

elif option == 2:
    clean_num = input("Enter name who you need delet: ").strip()
    if clean_num in contact:
        del contact[clean_num]
        print(f"{clean_num} is delet")
    else:
        print(f"{clean_num} no in contacts")

elif option == 3:
    numbers = input("Enter the name who you need see telefon number: ").strip()
    if numbers in contact:
        print(f"Telefon number {numbers} is {contact[numbers]}")
    else:
        print(f"{numbers} is not in contacts")


# Task 4

wal = {
    'USD': 1.0,
    'EUR': 0.92,
    'UA': 41.35
}

money = float(input("Enter the money: "))
from_wal = input("Enter from convert (USD, EUR, UA): ")
to_wal = input("Enter to convert (USD, EUR, UA): ")

res = (money / wal[from_wal]) * wal[to_wal]

print(f'{res:.2f}')



#Klass work

data = [
    '1 Bob Simson 19.58$ decorations',
    '2 Mary 66.7$ food',
    '3 Mary 98.91$ toys',
    '4 Aleksa 72.29$ drinks',
    '5 Maria Simson 84.48$ food',
    '6 Aleksa 100.41$ accessories',
    '7 Mary 19.9$ accessories',
    '8 Bob Simson 83.88$ drinks',
    '9 Bob Simson 58.21$ instruments',
    '10 Maria Simson 20.61$ accessories',
]

res = sum(float(i.split()[-2].replace('$', '')) for i in data if 'food' in i.lower())

print(f' Your Food Cost {res} $')


# Klass work 2

text = input('Enter a text: ')

res = {}

for char in text:
    if char in res:
        res[char] += 1
    else:
        res[char] = 1

print(res)

# Klass work 2_2

text = input('Enter a text: ')

res = {}

for char in text:
    res[char] = res.get(char, 0) + 1

print(res)