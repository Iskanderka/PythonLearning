# class Person:
#     pass  # Пустой блок
#
#
# p = Person()
# print(p)


# class Person:
#     def say_hi(self):  # обязательно нужен дополнительный параметр в начале, он отвечает за принадлежность классу
#         print('Привет! Как дела?')
#
#
# p = Person()
# p.say_hi()


# class Person:
#     def __init__(self, name):  # тупа конструктор класса, можно передать ему данные при создании объекта
#         self.name = name  # обязон писать self через точку
#
#     def say_hi(self):
#         print('Привет! Меня зовут', self.name)
#
#
# p = Person('Swaroop')
# p.say_hi()

# class Robot:
#     """Представляет робота с именем."""
#     population = 0  # Переменная класса, содержащая количество роботов
#
#     def __init__(self, name):
#         """Инициализация данных."""
#         self.name = name
#         print('(Инициализация {0})'.format(self.name))
#
#         # При создании этой личности, робот добавляется к переменной 'population'
#         Robot.population += 1
#
#     def __del__(self):
#         """Я умираю."""
#         print('{0} уничтожается!'.format(self.name))
#
#         Robot.population -= 1
#
#         if Robot.population == 0:
#             print('{0} был последним.'.format(self.name))
#         else:
#             print('Осталось {0:d} работающих роботов.'.format(Robot.population))
#
#     def say_hi(self):
#         """Приветствие робота. Да, они это могут."""
#         print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))
#
#     # @staticmethod  # можно применить декоратор вместо функции staticmethod
#     def how_many():  # метод класса, не объекта
#         """Выводит численность роботов."""
#         print('У нас {0:d} роботов.'.format(Robot.population))  # d - для целых
#
#     how_many = staticmethod(how_many)  # вот ето вполне можно заменить декоратором
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# Robot.how_many()
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# Robot.how_many()
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
#
# print("Роботы закончили свою работу. Давайте уничтожим их.")
# del droid1
# del droid2
#
# Robot.how_many()


# class SchoolMember:
#     """Представляет любого человека в школе."""
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('(Создан SchoolMember: {0})'.format(self.name))
#
#     def tell(self):
#         """Вывести информацию."""
#         print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")
#
#
# class Teacher(SchoolMember):  # при создании наследника указываем его родителей в виде кортежа
#     """Представляет преподавателя."""
#
#     def __init__(self, name, age, salary):
#         SchoolMember.__init__(self, name, age)  # комструктор базоваго класса нужно вызывать самому
#         self.salary = salary
#         print('(Создан Teacher: {0})'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Зарплата: "{0:d}"'.format(self.salary))
#
#
# class Student(SchoolMember):
#     """Представляет студента."""
#
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print('(Создан Student: {0})'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Оценки: "{0:d}"'.format(self.marks))
#
#
# t = Teacher('Mrs. Shrividya', 40, 30000)
# s = Student('Swaroop', 25, 75)
# z = SchoolMember("Valera", 54)
# print()  # печатает пустую строку
# members = [t, s, z]
# for member in members:
#     member.tell()  # работает как для преподавателя, так и для студента


# from abc import *  # модуль для работы с абстракциями
#
#
# class SchoolMember(metaclass=ABCMeta):  # всё, теперь он абстрактный и использоваться не может
#     """Представляет любого человека в школе."""
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('(Создан SchoolMember: {0})'.format(self.name))
#
#     @abstractmethod  # опять же абстракция, метод обязательно должен быть переопределён в наследнике
#     def tell(self):
#         """Вывести информацию."""
#         print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")
#
#
# class Teacher(SchoolMember):
#     """Представляет преподавателя."""
#
#     def __init__(self, name, age, salary):
#         SchoolMember.__init__(self, name, age)
#         self.salary = salary
#         print('(Создан Teacher: {0})'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Зарплата: "{0:d}"'.format(self.salary))
#
#
# class Student(SchoolMember):
#     """Представляет студента."""
#
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print('(Создан Student: {0})'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Оценки: "{0:d}"'.format(self.marks))
#
#
# t = Teacher('Mrs. Shrividya', 40, 30000)
# s = Student('Swaroop', 25, 75)
#
# # m = SchoolMember('abc', 10)
# # Это приведёт к ошибке: "TypeError: Can't instantiate abstract class
# # SchoolMember with abstract methods tell"
#
#
# print()  # печатает пустую строку
# members = [t, s]
# for member in members:
#     member.tell()  # работает как для преподавателя, так и для студента
