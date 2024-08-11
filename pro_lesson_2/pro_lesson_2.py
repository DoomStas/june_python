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











































































