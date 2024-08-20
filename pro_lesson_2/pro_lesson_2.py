#
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
#
#

# Klas work

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()

    def __str__(self):
        return f'{self.last_name} {self.first_name[0]}.'


class Student(Person):
    def __init__(self, first_name, last_name, date_of_birth=None):
        super().__init__(first_name, last_name)
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f'{super().__str__()}; {self.date_of_birth}'


class Teacher(Person):
    def __init__(self, first_name, last_name, main_language=None):
        super().__init__(first_name, last_name)
        self.main_language = main_language

    def __str__(self):
        return f'{super().__str__()}; {self.main_language}'


class Group:

    def __init__(self, title, teacher=None):
        self.title = title
        self.teacher = teacher
        self.__students = []

    def add_student(self, student: Student):
        if isinstance(student, Student) and student not in self.__students:
            self.__students.append(student)

    def __str__(self):
        return '\n'.join(map(str, self.__students))


teacher = Teacher('John', 'Doe', 'English')
gr_1 = Group('Group 1', teacher)

while answer := input('Do you want to add a student? (y/n) ').lower().strip() == 'y':
    first_name = input('Enter first name: ').strip().title()
    last_name = input('Enter last name: ').strip().title()
    st = Student(first_name, last_name)
    gr_1.add_student(st)

print(gr_1)


#klass work

class Animal:
    def speak(self):
        return None


class Dog(Animal):
    def speak(self):
        return "woof"


class Cat(Animal):
    def speak(self):
        return "meow"

class Fish(Animal):
    def speak(self):
        return "blub"


def animal_sound(animal: Animal):
    if not isinstance(animal, Animal):
        return 'This is not an animal!'
    return animal.speak()

x_1 = Dog()
x_2 = Cat()
x_3 = Fish()

print(animal_sound(x_1))
print(animal_sound(x_2))
print(animal_sound(x_3))



################


try:
    a = int(input('a='))
    b = int(input('b='))
    res = a/b

    print(res)

except ValueError as error:
    print("Try again", error)
except ZeroDivisionError as error:
    print('b must not be zero', error)


####################


class Box:

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def __mul__(self, other: int):
        if isinstance(other, int):
            return Box(self.length * other, self.width * other, self.height * other)
        return NotImplemented

    def __imul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self.length *= other
        self.width *= other
        self.height *= other
        return self

    def __rmul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return self.__mul__(other)

    def volume(self):
        return self.length * self.width * self.height

    def __eq__(self, other):
        return self.volume() == other.volume()

    def __ne__(self, other):
        return self.volume() != other.volume()

    def __lt__(self, other):
        return self.volume() < other.volume()

    def __le__(self, other):
        return self.volume() <= other.volume()

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __ge__(self, other):
        return self.volume() >= other.volume()

    def __str__(self):
        return f'{self.length} x {self.width} x {self.height}'


import random
x = [Box(random.randint(1, 25), random.randint(1, 25), random.randint(1, 25)) for _ in range(10)]
print('\n'.join(map(str, x)))
# print(min(x))
# print(max(x))
x.sort(reverse=True)
print('*' * 20)
print('\n'.join(map(str, x)))



##########################

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name: {self.name}"


class Group:
    def __init__(self):
        self.students = []

    def __iadd__(self, other: Student):
        self.students.append(other)
        return self

    def __len__(self):
        return len(self.students)

    def __getitem__(self, index):
        if isinstance(index, slice):
            group = Group()
            group.students = self.students[index]
            return group
        if isinstance(index, int):
            return self.students[index]
        raise TypeError("Index must be int or slice")


group = Group()
group += Student("Alice")
group += Student("Bob")
group += Student("Charlie")

group += Student("Alice 1")
group += Student("Bob 1")
group += Student("Charlie 1")

group += Student("Alice 2")
group += Student("Bob 2")
group += Student("Charlie 2")


x = group[::2]

for i in x:
    print(i)





































