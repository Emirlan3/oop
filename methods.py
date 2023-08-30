""" 
Методы  """

# методы эксемпляры (instance methods)
# методы класса (class methods)
# 3. статистика методы (static method)

# методы экскемпляра (оюъекта)
# обячные методы, который принимают первым аргументам self(для работы с атрибами)

# Методды -> принимают первым аргументам ссылку на класс (cls). Нужны для создании объекта , изменение атрибута класса,
# Lkz cjplfybb bpgjkmpetncz ltrthfnjh @classmethod (вызыватеся и через объект, и через класс)
class A:
    def __init__(self, a):
        self.a = a

    def instance_method(self):
        print('Метод объекта')

a = A(1)
a.instance_method()
A.instance_method(a)
# A.a
# a.a

# Методы классы
class B:
    @classmethod
    def class_method(cls):
        print('Метод класса')
        print(cls)
obj = B()
obj.class_method()
B.class_method()
# a.a

# A.a
# a.a

# Методы классы
class B:
    @classmethod
    def class_method(cls):
        print('Метод класса')
        print(cls)
obj = B()
obj.class_method()
B.class_method()
# # a.a

# class Car:

#     color = 'red'

    # @classmethod
    # def change_color(cls, new_color):
    #     cls.color = new_color

#     def change_color(self, new_color):
# #         self.color = new_color
# lada = Car()
# bmw = Car()
# # lada.change_color('black')
# print(lada.color, bmw.color)

# Car.change_color(bmw, 'grey')
# print(lada.color, bmw.color)
# print(Car.color)

class Counter:
    c = 0
    counter = 0

    def __init__(self):
        self._increase()
    def __del__(self):
        self._decrease()
        del self

    @classmethod
    def _increase(cls):
        cls.counter += 1
    @classmethod
    def _decrease(cls):
        cls.c -= 1

# obj = Counter()
# obj2 = Counter()
# obj3 = Counter()
# del obj
# del obj2
# del obj3

# print(Counter.c)

class Pizza:
    def __init__(self, radius, *ingredients):
        self.radius = radius
        self.incredients = ingredients

    def cook(self):
        print(f'готовится пицца размером{self.radius * 2} см')
        print(f'ингредиенты: {self.incredients}')

    @classmethod
    def chili(cls, r):
        pizza = cls(r, 'перец', 'фарш','сыр Массарелла', 'Острый перец', 'Голландский сыр')
        return pizza
# pizza1 = Pizza(15, 'Помидоры', 'Сыр')
# pizza1.cook()

# pizza_chilli = Pizza.chili(20)
# print(pizza_chilli)
# pizza_chilli.cook()

# # Статичиескме методы -> они принимают в себе ссылку на класс и на объект , просто функции внутри класса 
# (которые не взаимодействует с классам объектом) Изполбзуется только внутри класса
# # Для создании @staticmethod (изменение типы данных, расчеты и тд)
# class C:
#     @staticmethod
#     def static_method(x, y):
#         print(x + y)

# C.static_method(5, 6)
# c = C()
# c.static_method(6, 7)


class Cylinder:
    def __init__(self, d, h):
        self.diametr = d
        self.height = h
        self.area = self.get_area(d, h)

    @staticmethod
    def get_area(d, h):
        from math import pi
        circle = pi * d ** 2 / 4
        side = pi * d * h
        area = circle * 2 + side
        return round(area, 2)
    
# print(Cylinder.get_area(5, 3))
# cylinder = Cylinder(2, 8)
# print(cylinder.area)

class Home:
    count_people = 0
    def __init__(self, name, last_name, count_people2):
        self.name = name
        self.last_name = last_name
        self.count_people2 = count_people2
        Home.count_people += count_people2
    def info(self):
        print(self.name, self.last_name)

    @classmethod
    def f(cls):
        print(cls.count_people)

    @staticmethod
    def about_home():
        print('Лучший дом, покупайте кватиры! НЕ ДОРОГО!!!')

# kv1 = Home('Петр', 'Стельмах', 13)
# kv2 = Home('Айкол', 'Сергекбеков', 2)
# print(kv1.count_people)
# kv1.f()
# kv2.about_home()


class Iphone14:
    cost = 120000
    def __init__(self, money, name):

        if money < Iphone14.cost:
            a = self.get_money(money, Iphone14.cost)
            Exception(
            f'Вам не хватило {a} сом')
        self.owner = name
    @classmethod
    def change_cost(cls, new_cost):
        cls.cost = new_cost
    @staticmethod
    def get_money(money, cost):
        return cost - money
    

i = Iphone14(140000, 'test')
i.change_cost(80000)
print(Iphone14.cost)
