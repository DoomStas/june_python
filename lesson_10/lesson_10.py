def read_file(file_path):
    data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            li = line.strip().split()
            number = int(li[0])
            name = ' '.join(li[1:-2])
            amount = float(li[-2][:-1])
            category = li[-1]
            data.append((number, name, amount,category))
    return data

def sum_by_category(data):
    category_sum = {}
    for _, _, amount, category in data:
        if category in category_sum:
            category_sum[category] += amount
        else:
            category_sum[category] = amount
    return category_sum

def money_member(data):
    member_sum = {}
    for _, name, amount, _ in data:
        if name in member_sum:
            member_sum[name] += amount
        else:
            member_sum[name] = amount
    return member_sum

def member_buy(data, member_name):
    purchases = 0
    spent = 0.0

    for i in data:
        if i [1] == member_name:
            purchases += 1
            spent += i[2]
    return purchases, spent

file_path = 'hw_10_test.txt'
data = read_file(file_path)

all_category = sum_by_category(data)
print('Total cost by category: ')
for category, total in all_category.items():
    print(f'{category}: {total:.2f} ')

member_total = money_member(data)
print('Costs of each family member: ')
for member, total in member_total.items():
    print(f'{member}: {total:.2f}')

user_name = input('Enter the name: ').strip()
purchases_mem, total_spent = member_buy(data, user_name)
print(f'Number of purchases {user_name}: {purchases_mem}')
print(f'Total amount spent {user_name}: {total_spent:.2f}')




