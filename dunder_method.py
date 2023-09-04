""" 
Магтческие методы. (dunder -> double underscore) """


# __init__, __str__

#  # __new__() -> конструктор класса, отвечает создание

#2 __init__()
#3 __del__() -> деструктор, отвечает за удаление объекта

# class Point:
#     def __new__(cls, *args, **kwargs):
#         print('Вызов метода new')
#         return super().__new__(cls,)
#     def __init__(self, x, y):
#         print('init')
#         self.x = x
#         self.y = y

    # def __del__(self):
    #     print('удаление экземпляра' + str(self))

# a = Point(4, 5)
# # print(a)

# class Word(str):
#     # pass
#     def __new__(cls, *args, **kwargs):
#         string = args[0].replace(' ', '')
#         return str.__new__(cls, string)
    
#     # def __str__(self):
#     #     return 


# string = Word('he  llo', 'a s d ')
# # str2 = Word('a s d f')
# print(string)



class User:
    def __new__(cls, name, age):
        if age < 18:
            raise ValueError(
                "Вы слишком молоды"
            )         
        return object.__new__(cls)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

# admin = User('Adilet', 18)
# print(admin)

import datetime
from typing import Any

# print(repr(datetime.date.today()))
# print(datetime.date.today())
c = repr(datetime.date.today())
print(c)
print(eval(c))
print(eval(c))



class MyNumber(int):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return f'Это сложение и результат равен: {self.value + other}'
    def __sub__(self, other):
        return f'Это вычитание и  равен: {self.value - other}'
    def __mul__(self, other): # *
        return f'Это умножение и результат равен: {self.value * other}'
    def __truediv__(self, other):
        return f'Это деление и результат равен: {self.value // other}'
    def __pow__(self, other):
        return f'результат: {self.value ** other}'
    def __mod__(self, other):
        return f'остаток: {self.value % other}'


# int_obj = MyNumber(9)
# print(pow(int_obj, 3))
# # print(int_obj + 7)
# # print(int_obj - 9)
# # print(int_obj * 2)
# print(int_obj ** 2)

# == -> __eq__(self, other) equel - равно
# != -> __ne__(self, other) not equal -> неравно
# > -> __gt__(self, other) greater than -> больше
# <= _> __le__(self, other)
# <= -> __le__(self, other)

# class Base:
#     def __init__(self, string):
#         self.string = string
#     def __invert__(self): #~
#         return self.string[::-1]
#     def __str__(self):
#         return self.string
# i = Base('hello world')
# res = ~i
# print(res)

# __getattribute__(self, item(атрибут, к которому идет обращение)) #-> автоматичкский вызыывается приобращение к атрибуту


# string = 'hello'
# print(string.lower)
# print(string.__getattribute__('lower'))
# __getarr__ #->  вызывается автоматичесуй не существующему атрибуту

# __setattr__ # -> вызывается автоматический при присвание артибуту нового значение
# __delattr__ #-> выхывается автоматический прои удвление атрибута

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, name):
        print('__getatttribute__')
        if name == 'x':
            raise Exception(
                'Доступ запрещен'
            )
        
        return super().__getattribute__(name)
    def __setattr__(self, name, value):
        print('__setattr__')
        super().__setattr__(name, value)
    
    def __getattribute__(self, name):
        print('__getattr__')
        raise AttributeError(
            'no such attribute'
        )
    def __delattr__(self, name):
        print('__delattr__')
        super().__delattr__(name)
    
p = Point(8, 0)
del p.x
# p.z = 9
# p.x = 9
# p.x

# __getitem__ -> по ключу, по индексу или делает срез
# __setitem__ -> создает ключ с каким то значением
# __delitem__ -> удааляет

""" Ассоциация -> принцип, в котором два класса связаны с друг другом  """

# агрегация -> слаба связь
# композиция -> сильная связь

# class A: # Компонент
#     pass

# class B: # составной
#     """  содержить оюъект от класса A """
#     pass

# class Engine:
#     pass
# class Wheel:
#     pass
# class Elocnka:
#     pass


# class Car:
#     def __init__(self, elochka):
#         self.elochka = elochka
#         self.engine = Engine()
#         self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]

# # freesheher = Elocnka()

# # car = Car(freesheher)
# """ Агрегация """
# class Salary:
#     def __init__(self, pay):
#         self.pay = pay
    
#     def get_total(self):
#         return self.pay * 12

# salary = Salary(30000)

# class Employe:
#     def __init__(self, pay, bonus: int):
#         self.pay = Salary(pay)
#         self.bonus = bonus
    
#     def annualSalary(self):
#         print(f'total: {self.pay.get_total() + self.bonus}')

# emp = Employe(30000, 10000)
# emp.annualSalary()

# """ Композиция  """


# class Battery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100

# class Iphone:
#     def __init__(self, color, storage):
#         self.color = color
#         self.storage = storage
#         self.battery = Battery()


# class Nokia:
#     def __init__(self, battery: Battery, color: str = 'синий'):
#         self.battery = battery
#         self.color = color
#         self.storage = 8

# battery = Battery()
# i = Iphone('purple', 512)
# nokia = Nokia(battery)

# i.battery._power = 50
# i.battery.charge()
# print(i.battery._power)

# class Employe:
#     def __init__(self, name, last_name,):
#         self.name = name
#         self.last_name = last_name
    
#     def lecture(self):
#         print('Провожу лекцию группе')
#     def interactive(self):
#             print('Провожу интерактив группе')


# class Student:
#     def __init__(self, name, last_name, age, kpi):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#         self.kpi = 0
#     def study(self):
#         print('просматриваю видео лекцию')
#     def do_tastks(self):
#         print('Решаем таски')


#         self.kpi += 10
#     def pass_test(self):
#         self.kpi += 15

# class Group:
#     def __init__(self, name, count_students):
#         self.name = name
#         self.count_students = count_students
#         self.curator = Employe('Aigerim', 'Taalaybekova')
# junPYback = Group('junPYback', 17)
# pitHUB = Group('pitHUB', 15)
# class CaBinet:
#     def __init__(self, number, seats, group1, group2 = None):
#         self.number = number
#         self.seats = seats
#         self.group = [group1, group2]


# cab_9 = CaBinet(9, 35, junPYback, pitHUB)
# print(cab_9.group[0].curator.name)

# class Maker:
#     def __init__(self, cab_count: int, *employees):
#         self.employes = [employees]
#         self.cabinets = cab_count


# class APL:
#     def __init__(self, Liverpool, Manchester_city, Arsenal):
#         self.Liverpool = Liverpool
#         self.Machester_city = Manchester_city
#         self.Arsenal = Arsenal
#     def ligue(self):
#         print(f'{self.Liverpool}, {self.Machester_city}, {self.Arsenal} это английские клубы')

# a = APL('Ливерпуль', 'Манчестер сити', 'Арсенал')
# print(a.ligue())
              


class ContactList(list): 
    def __init__(self, list_): 
        self.list_ = list_ 
    def search_by_name(self, name): 
        a = [] 
        for i in self.list_: 
            if name in i: a.append(i) 
            return a 
all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya')) 





class User:
    def __new__(cls, name, age):
        if age < 18:
            raise ValueError(
                "Вы слишком молоды"
            )         
        return object.__new__(cls)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def homan(self):
        if self.age < 18:
            raise Exception('Вы слишком молоды!')
        else:
            return f'Вам доступно'

obj2 = ('Emirlan', '17')
print(obj2.homan('emirlan'))