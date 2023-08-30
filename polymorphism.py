""" Основные принципы ООП: Пoлиморфизм """

""" 
разное поведение одного и тоже метода в разных классах """

# + 
# 4 + 5
# 'str' + 'test'
# [1, 2, 3] + [4, 5, 6]

# len()
# len('string')
# len[(1, 2, 3)]
# ...

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f'it is a dog\nname: {self.name}')
    def make_sound(self):
        print('vav')

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print('It is a cat\nname: {self.name}')
    
    def make_sound(self):
        if self.name == 'Muhtar':
            print('gav')
        else:
            print('wow')

animals = [Dog('Muhtar', 2), Dog('Bos', 1), Cat('Murka', 4), Cat('Barsik', 2)]
for i in animals:
    i.info()
    i.make_sound()


from math import pi

class Snape:
    def __init__(self, name):
        self.name = name

    def ger_area(self):
        pass
    def fact(self):
        print('Я фигура дмерной плоскости')
    def __str__(self):
        return self.name
    
class Square(Snape):
    def __init__(self, length):
        super().__init__('Square')
        self.length = length
    def get_area(self):
        return self.length ** 2
    
    def fact(self):
        return 'У квадрата все стороны равны'
    
class Circle(Snape):
    def __init__(self, radius):
        super().__init__('Circle')
        self.radius = radius

    def get_area(self):
        return pi + self.radius ** 2

shapes = [Square(4), Square(8), Circle(4), Circle(6)]    

for snape in shapes:
    print(snape.fact())
    print(snape.get_area())


# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, 
# краткой информации об установленной ОС. 
# Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность зарядить батарею.


# class Phone:
#     def __init__(self, imei, os,):
#         self.__imei = imei
#         self.os = os
#         self.__b_level = 100
#     def check_battery_level(self, b_l):
#             raise Exception(
#                 'Низкий уроыен')

#     @property
#     def battery_level(self):
#         if self.__b_level <= 0.5:
#             raise Exception(
#                 'пихкий уровень заряда'
#             )
#         self.__b_level -= 0.5
#         print(f'os: {self.os}\IMEI: {self.__imei}')

#     def play_music(self):
#         if self.__self.__b_level <= 5:
#             raise Exception(
#                 'Низкий уроыень заряда'
#             )
#     def play_video(self):
#         if self.__b_level <= 7:
#             raise Exception(
#                 'Низкий уровень заряда'
#             )
#         self.__b_level -= 7
#         print('Смотрим папины дочки')

#     def charge_battery(self, sec):
#         from datetime import datetime, timedelta
#         from time import sleep

#         now = datetime.now
#         end_time = (now() + timedelta(second = sec)).strftime('%M:%S')

#         while now().strftime('%M:%S') != end_time:
#             sleep(1)
#             if self.__b_level < 100:
#                 self.__b_level += 1
#             print(f'Идет зарядка батареи идет! зарядка батереи{self.battery_level}')

# phone = Phone('171-23-35-32', 'IOS 16')
# print(phone.__b_level)
# print(phone.get_info)
# phone.play_music()
# phone.play_video()
# phone.play_music()

# phone.charge_battery()
    

# from datetime import datetime
# print(datetime.now().strftime)



class ContactList(list):
    def search_by_name(self, name):
        list_ = []
        for i in self:
            if name in i:
                list_.append(i)
        return list_


all_contact_list = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan', 'Olya', 'Ivan'])
print(all_contact_list.search_by_name('Olya'))


# class Person:
#     def __init__(self, name, last_name , age, email):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#         self.email = email
#     def 

class Dog:
    def voice(self):
        print('Гав')    
class cat:
    def voice(self):
        print('Мяу')

barsik = Cat()
resk = Dog()

def to_pet(self):
    self.voice()
to_pet(barsik)
to_pet(resk)

        
        