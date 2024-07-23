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
words = len(set(text.split()))

print(words)


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


# # Task 4
#
# friendships = {
#     "Stas": {"Dima", "Dan", "Jan"},
#     "Dima": {"Stas", "Dan"},
#     "Dan": {"Stas", "Dima", "Jan"},
#     "Jan": {"Stas", "Dan"}
# }
#
# user_names = input('Enter names: ').split()
# user_names = set(user_names)
#
# for user_name in user_names:
#     if user_name in friendships:
#         common = friendships[user_name] & user_names
#         print(f"Common friends with {user_name}: {common}")
#     else:
#         print(f"{user_name} is not in friends")



# Task 5

text_1 = set(input('Enter text: ').lower().split())
text_2 = set(input('Enter text: ').lower().split())

common = text_1 & text_2

if common:
    long = max(common)
    print(f'Longest word is {long}')
else:
    print('In texts not found double words')











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
