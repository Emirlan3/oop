# """ ООП - Объектно Ориентирование Програмированные """

# # ООП - Способ написание кода. Два основных понятие: классы и объекты

# # Классы - участок кода, который описывает объекты: свойства/атрибуты, методы/функции

# # # Объекты - экзампляры/переменные, которые относится к указаному классу

# # class MyClass:


# # obj = MyClass()

# # num = 10
# # num = int(10)

# class Human:
#     hands = 2
#     leg = 2
#     head = 1
#     eyes = 2
#     hair = 'block'
#     # атрибуты класса

#     def eat(self): # метод - функция внутри класса 
#         print('Human eating')

# human1 = Human()
# print(human1.leg) # 2

# human1.eat()

# human1.eat()
# # одно и тоже
# Human.eat(human1) # одинокавая запись 

# human1.hands = 1
# human1.eyes -= 1
# print(human1.hands)
# print(human1.eyes)

# human1.tail = 1
# print(human1.tail)

# # human1.phone # AttributeError

# class Laptop:
#     keyboard = True
#     touchpad = True

#     def __init__(self, tittle, price, color, ram, ds):
#         # атрибуты экземпляры
#         self.tittle = tittle
#         self.price = price
#         self.color = color
#         self.ram = ram
#         self.display = ds
#         print('__init__ сработал')
#     def set_radio(self):
#         self.radio = True

#     def set_ram(self, value):
#         print(self.ram)
#         self.ram = value
#         print(self.ram)


# # __init__ - метод для создании объектов
        
# l1 = Laptop('Samsung', 21234, 'silver', 512, "13,'5")
# l2 = Laptop('HP', 1234, 'black', 256, "15'6")

# l1.set_radio()
# l1.radio # True 

# l1.price = 500
# l2.price #1234

# l1.keyboard = False
# (l2.keyboard)

# Laptop.touchpad = False
# print(l1.touchpad)

# l2.set_ram(516)
# Laptop.set_ram(self = l2, value = 516)



# class Phone:
#     phone_counter = 0

# def __init__(self):
#     print(f"Сейчас{Phone.phone_counter}объектов")


# p1 = Phone()
# p2 = Phone()
# p3 = Phone()

# # Классы бывают:
# # Функциональные классы - 
# # Датаклассы - для храненные данных (свойств/атрибутов)


# class Car:
#     def __init__(
#             self,
#             color: str,
#             marka: str,
#             model: str,
#             engine: bool = True
#     ):
#         self.color = color
#         self.color = color
#         self.color = color


# from dataclasses import dataclasses
# @dataclasses
# class Car:
#     model: str
#     engine: bool = True
#     marka: str
#     color: str

# car = Car('BYD', True, 'e50', 'white')
# car.color 

# # dict_car = {
# #     'marka':
# #     'color':
# # }

# class Mebel:
#     __slots__ = ('heidht', 'width', 'color')

#     def __init__(self, height, widh, color):
#         self.height = height
#         self.width = widh
#         self.color = color

# stol = Mebel(20, 30, 'white')
# stol.tail = True

# isinstance(stol, Mebel) # True
# isinstance('string', int) # False

# """ 
# Наследование
# Инскапсуляция
# Полиморфизм

# Абстракция
# Ассосиация (Агрессия, Композиция)
#  """

class A(object):
    b = 2 # атрибут класса
    def __init__(self, r, t):  # атрибуты объекта (экзампляра класса)
        self.c = r
        self.d = t

# a = A(3, 4)
# a.e = 5
# print(a)
# a1 = A(5, 6)
# print(A.b)


class Salary:
    nalog = 15

    def __init__(self, zp, staj):
        self.zp = zp
        self.staj = staj

    def sum_nalog(self):
        """ найти сумму уплаченного налога, за все время работы """
        a = self.zp * self.staj * 12 * self.nalog / 100
        print(a)

salary_obj = Salary(10000, 2)
salary_obj.sum_nalog

class Car:
    def __int__(self,  model, year, mileg = 0, is_going = False):