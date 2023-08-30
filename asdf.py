# class Dog:
#     def __init__(self, name, age):
#        self.name = name
#        self.age = age
#     def bark(self):
#        print("gav gav!")
#     def doginfo(self):
#        print(self.name + " is " + str(self.age) + " is(s) years.")
# ak_tosh = Dog("Ak-Tosh", 2)
# rex = Dog("Rex", 12)
# bobik = Dog("Bobik", 8)
# ak_tosh.doginfo()
# rex.doginfo()
# bobik.doginfo()

# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# class M:
#     pass

# c = C()
# print(isinstance(c,M))
    
# class Polygon:
#     sides = 4

#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs
#         print(self.args)
#         print(self.kwargs)
#     def get_perimeters(self):
#         if self.args:
#             return sum(self.args)
#         else:
#             return sum(self.kwargs.values())

# class Regtangle(Polygon): 
#     def get__init__(self, a, b):
#       self.a = a
#       self.b = b
#     def get_perimeter(self):
#         return (self.a + self.b) * 2

# regtangle = Regtangle(1, 2)
# print(regtangle.sides)
# print(regtangle.get_perimeter())

# # polygon = Polygon(a = 2, b = 4, m = 5, c = 6)
# # print(polygon.get_perimeters())
# # print(polygon.sides)

# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return self.pi * (self.radius ** 2)


# circle  = Circle(123)
# circle.color = 'yellow'
# print(circle.color)
# print(circle.get_area())

# class BankAccount:
#     balance = 0
#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f'Ваш баланс: {self.balance} сом')
#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance} сом')

# account = BankAccount()
# account.deposit(1000) 
# account.withdraw(500) 



# class Taxi: 
#     def __init__(self, name, cost, cost_km): 
#         self.name = name 
#         self.cost = cost 
#         self.cost_km = cost_km 
#     def get_total_cost(self, km): 
#         self.cost = self.cost_km * km + self.cost 
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом' 
# taxi1 = Taxi(name='Namba',cost=29, cost_km=15) 
# taxi2 = Taxi(name='Yandex',cost=25, cost_km=17) 
# taxi3 = Taxi(name='Jorgo',cost=28, cost_km=15) 
# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))
# # class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
#     def get_total_cost(self, km):
#         self.cost_km * km + self.cost_km
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом'
# taxi1 = Taxi(name = 'Namba', cost = 29, cost_km = 15) 
# taxi2 = Taxi(name = 'Yandex', cost = 20, cost_km = 11)
# taxi3 = Taxi(name = 'Jorgo', cost = 19, cost_km = 14)
# print(taxi1.get_total_cost(5))
# print(taxi2.get_total_cost(6))
# print(taxi3.get_total_cost(7))

# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')
# contact = Phone('John', 'Snow', '+996707707707')
# contact.get_info()

# class Salary: 
#     percent = 8 
#     def __init__(self, salary, experience): 
#         self.salary = salary 
#         self.experience = experience 
#     def count_percent(self): 
#         return self.salary * self.percent / 100 * self.experience 
# obj = Salary(1000, 8) 
# print(obj.count_percent())
""" 

Напишите класс Nobel, который будет принимать аттрибуты category, yearи winner. 
Создайте метод get_year(), который будет выводить сколько лет назад была получена премия в виде 'выиграл {кол-во лет} лет назад'.

    Дату сколько лет назад была получена премия в методе get_year() не вписывать вручную, а высчитывать используя datetime
 """

import datetime 
class Nobel(): 
    def __init__(self, category, year, winner) -> None: 
        self.category = category 
        self.year = year 
        self.winner = winner 
    def get_year(self): 
        a = datetime.datetime.now() 
        res = a.year - self.year 
        return f'Выиграл {res} лет назад' 

winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
print(winner1.category, winner1.year, winner1.winner) 
print(winner1.get_year()) 
winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
print(winner2.category, winner2.year, winner2.winner) 
print(winner2.get_year())
        
