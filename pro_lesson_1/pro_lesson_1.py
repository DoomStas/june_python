# Task 1

class Product:
    def __init__(self, product_name, description_product, price_product):
        self.product_name = product_name
        self.description_product = description_product
        self.price_product = float(price_product)

    def __str__(self):
        return f'{self.product_name} - {self.description_product}: ${self.price_product:.2f}'


class Cart:

    def __init__(self, title):
        self.title = title
        self.products = {}

    def add_product(self,product: Product, quantity=1):
        if isinstance(product, Product):
            if product in self.products:
                self.products[product] += quantity
            else:
                self.products[product] = quantity

    def cost(self):
        return sum(product.price_product * quantity for product, quantity in self.products.items())

    def __str__(self):
        cart_content = [f'{product} x {quantity}' for product, quantity in self.products.items()]
        total = f'Total cost: ${self.cost():.2f}'
        return '\n'.join(cart_content) + '\n' + total



you_cart = Cart('Cart')
while input('Do you want to add a product? (y/n) ').lower().strip() == 'y':
    product_name = input('Enter product name: ').strip().title()
    description_product = input('Enter description product: ').strip().title()
    price_product = float(input('Enter price product: ').strip())
    quantity = int(input('Enter quantity: ').strip())
    product = Product(product_name, description_product, price_product)
    you_cart.add_product(product, quantity)

print(you_cart)




# # Klass work
#
# class Student:
#     def __init__(self, first_name, last_name, date_of_birth=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.date_of_birth = date_of_birth
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
#
#
# class Group:
#
#     def __init__(self, title):
#         self.title = title
#         self.__students = []
#
#     def add_student(self, student: Student):
#         if isinstance(student, Student) and student not in self.__students:
#             self.__students.append(student)
#
#     def __str__(self):
#         return '\n'.join(map(str, self.__students))
#
#
# gr_1 = Group('Group 1')
# while answer := input('Do you want to add a student? (y/n) ').lower().strip() == 'y':
#     first_name = input('Enter first name: ').strip().title()
#     last_name = input('Enter last name: ').strip().title()
#     st = Student(first_name, last_name)
#     gr_1.add_student(st)
#
# print(gr_1)
