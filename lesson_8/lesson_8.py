# Task 1
text = input('Enter the text: ')
words = text.split()
un_words = set(words)
if len(words) == len(un_words):
    print('All words is uniqui')
else:
    print('You have not uniqui words in text')



# Task 2

text = input('Enter the text: ')
count = 0
for i in text:
    if text.count(i) == 1:
        count += 1
print(count)


# Task 3

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

if len(data) == len(set(data)):
    print('All words is uniqui')
else:
    print('You have not uniqui words in text')


# Task 4

friendships = {
    "Stas": {"Dima", "Dan", "Jan"},
    "Dima": {"Stas", "Dan"},
    "Dan": {"Stas", "Dima", "Jan"},
    "Jan": {"Stas", "Dan"}
}

user_1 = input('Enter names: ')
user_2 = input('Enter names: ')

friends_1 = friendships.get(user_1,set)
friends_2 = friendships.get(user_1,set)

mutual_friends = friends_1 & friends_2
mutual_friends = mutual_friends or 'No mutual driends'

print(mutual_friends)



# Task 5

import string
text_1 = input('Enter text: ')
text_2 = input('Enter text: ')

for item in string.punctuation:
    text_1 = text_1.replace(item, ' ')
    text_2 = text_2.replace(item, ' ')

text_1 = set(text_1.lower().split())
text_2 = set(text_2.lower().split())

comon_words = text_1 & text_2
print(max(comon_words, key=len))







# Klass work

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
categories = {}
family = {}

for line in data:
    tmp = line.split()
    _, *name, money, category = tmp
    name = ' '.join(name)
    category = tmp[-1]
    money = float(tmp[-2].replace('$', ''))
    categories[category] = categories.get(category, 0) + money
    family[name] = family.get(name, 0) + money
print(categories)
print(family)

#Klass work 2

text_1 = input('Text')
text_2 = input('Text')

text_1 = set(text_1.split())
text_2 = set(text_2.split())

res = text_1.intersection(text_2)
print(*res)
