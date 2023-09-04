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

# import datetime 
# class Nobel(): 
#     def __init__(self, category, year, winner) -> None: 
#         self.category = category 
#         self.year = year 
#         self.winner = winner 
#     def get_year(self): 
#         a = datetime.datetime.now() 
#         res = a.year - self.year 
#         return f'Выиграл {res} лет назад' 

# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year()) 
# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())
        

# class ContactList(list): 
#     def __init__(self, list_): 
#         self.list_ = list_ 
#     def search_by_name(self, name): 
#         a = [] 
#         for i in self.list_: 
#             if name in i: 
#                 a.append(i) 
#         return a 
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya')) 


# class SmartPhones: 
#     def __init__(self, name, color, memory): 
#         self.name = name 
#         self.color = color 
#         self.memory = memory 
#         self.battery = 0 
#     def __str__(self): 
#         return f"{self.name} {self.memory}" 
#     def charge(self, number): self.battery += number 

# class Iphone(SmartPhones): 
#     def __init__(self, name, color, memory, ios): 
#         super().__init__(name, color, memory) 
#         self.ios = ios 
#     def send_imessage(self, string): 
#         return f"sending {string} from {self.name} {self.memory}" 

# class Samsung(SmartPhones): 
#     def __init__(self, name, color, memory, android): 
#         super().__init__(name, color, memory) 
#         self.android = android 
#     def show_time(self): 
#         import datetime 
#         return datetime.datetime.now().time() 
    
# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7) 
# print(iphone7.send_imessage('hello')) 
# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time()) """

""" 
Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). В этом классе реализуйте метод show_my_drink(), 
выводящий на печать Газировка и {ДОБАВКА} в случае наличия добавки, а иначе отобразится следующая фраза: Обычная газировка """
class Soda:
    def __init__(self, drink):
        self.drink = drink
    def show_my_drink(self):
        print(f'газировка и  {self.drink}')
    


    """ Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. Для этого он решил создать класс TriangleChecker, принимающий только положительные числа. С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать. """


class TiangleChecker:
    def __init__(self, num1, num2, num3):
        self.num1 = num1 
        self.num2 = num2
        self.num3 = num3
    def is_triangle(self):
        if self.num1 or self.num2 or self.num3:
            print()
        else:
            