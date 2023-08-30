# """
# Основные принципы ООП Наследование
#   """
# # Наследование - принцип ООпб в которым мы можем унаследовать в дочерном классе все атрибуты и методы родительского класса
# # Создаем новый класс на основе уже существующего 
# # class Родительский_класс:
# #     методы и атрибуты_Родительского класса

# # class Дочерный_класс(Родительский_класс):
# #     методы и атрибуты Дочерного класса

# class Animal:
#     def say(delf):
#         print("i'm animal")

# class Croco(Animal):
#     pass

# # croco = Croco()
# # # croco.say()
# # print(dir(Croco))


# class A:
#     name = 'B'
#     def method(self):
#         print('Метод в классе А')

# class B:
#     def method_b(self):
#         print('Hello PY30')

# class C(A):
#     pass

# b = B()
# b.method_b()
# c = C()
# c.method()

# # mro -> (Method resolution order) порядок поиска атрибутов и методов

# print(B.__mro__)
# print(B.mro())

# """ Виды наследование """
# # 1. одиночное наследоваие (когда наследуемся только от 1го родителья)
# # 2. иерархическое наследование (когда у одного родителья много дочерных классов)
# # 3. многоуровенное наследование ()
# # 4. множественное наследование(когда у одного дочерного класса несколько родительских классов))
# # 5. гибридное наследование 

# class Person:
#     def __init__(self, name, age, last_name):
#         self.name = name
#         self.age = age
#         self.last_name = last_name
#     def display_info(self):
#         print(f'Name: {self.name}')
#         /nLast_name: {self.name}nAge:
#         {self.age}


# # class Employee(Person):
# #     def work(self):
# #         print(f'')

# def __init__(self, name, last_name, age, faculty):
#     Person.__init__(self, name, age, last_name, faculty)
#     self.faculty = faculty
# class super():
#     def _init__(self, name, last_name, age, faculty):
#         super().__init__(name, age, last_name,)
#         self.faculty = faculty
# from typing_extensions import SupportsIndex


# class A:
#     def my_range(self, n):
#         list(range(n+1))
#         #[i for i in range(n+1)]

# new_list = A()
# print(new_list.my_range(10))

# class B(A):
#     def my_range(self, n):
#         super().my_range(n)
#         print('hello')

# b = B()
# b.my_range(10)

# # issubclass(first_class, second_class, ) ->
# # проверяет является first_class дочерным классам second_class 

# # print(issublass(B, A))
# # print(issubclass(A, B))
# # print(issublass(A, onj))

# # class Mystring(str):
# #     pass

# # print(dir(Mystring))

# class Mystring(str):
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return f'{self.value}'
    
#     def append(self, str_):
#         self.Hello += str_

#     def pop(self):
#         last = self.value[-1]
#         self.Hello = self.value[:-1]
#         return last
    

# # a = Mystring('hello')
# # a.append('world')
# # print(a.pop())
# # print(a)

# # b = str('test')
# # print(b)


# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password
#     def describe_user(self):
#         print(f'{self.user} -> {self.email}')

#     def greet_user(self):
#         print(f'Welcome {self.username}')

# class adminuser(User):
#     def __init(self, username, email, password):
#         super().__init__(username, email, password)
#         self.privilages = []

#     def __str__(self):
#         return 'admmin'

#     def add_privilages(self, privil):
#         self.privilages.append(privil)

# def show_privilages(self):
#     print(self.privileges)

# admin = adminuser('admin', 'admin@gmailcom,' '1')

# admin.add_privilages('delete other user')
"""  Создайте класс Class1 с 2 методами - first и second.

Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе Class2 ещё 2 метода - third и fourth.

Создайте экземпляр obj от класса Class2 и вызовите у него все четыре метода. """
class Class1:
    def first(self):
        pass

    def second(self):
        pass

class Class2(Class1):
    def third(self):
        print('third')

    def fourth(self):
        pass
obj = Class2()

obj.first()
obj.second()
obj.third()
obj.fourth()


""" Создайте класс A и определите в нём метод method1, который будет печатать строку

Основной функционал

Затем создайте второй класс B, который наследуется от класса A.

Внутри класса B переопределите method1 таким образом, чтобы он помимо строки "Основной функционал", также печатал строку

Дополнительный функционал

Объявите экземпляр класса B в переменной obj и вызовите метод method1. Результат в терминале должен быть:

Основной функционал 
Дополнительный функционал 
 """

class A:
    def method1(self):
        print('Основной функционал')

class B(A):
    def method1(self):
        super().method1()
        print('Дополнительный функционал')

obj = B()
obj.method1()



"""Создайте класс MyString, который будет наследоваться от str.

Определите 2 своих метода:

    append, который будет принимать строку и добавлять её в конец исходной

    pop, который удаляет из строки последний элемент и возвращает его.

Затем, создайте экземпляр example от класса MyString со значением String. Добавьте к example строку 'hello' методом append, затем примените метод pop. """

# class Mystring:
#     def method1(self):
#         print('method1')

#     def method2()
        
""" Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод get() таким образом, чтобы при попытке получения несуществующего ключа, по умолчанию он возвращал, вместо None, строку: """
class MyDict(dict):
    def get(self, k, v = 'Are you kidding?'):
        return super().get(k, v)

            
obj_dict = MyDict({'sum': 1})
print(obj_dict.get('sum'))
print(obj_dict.get('some'))

""" Создайте класс Person который будет описывать человека, а точнее его имя - name и возраст - age. Добавьте к классу метод display(), который будет выводить данные об этом человеке.

Создайте второй класс Student, который будет наследоваться от класса Person.

Объекты от класса Student должны иметь все атрибуты, которые были определены в родительском классе и еще один дополнительный атрибут - faculty, который будет описывать факультет, где учится студент.

Создайте метод display_student(), который будет выводить данные об этом студенте.

Создайте от класса Student объект в перемнной obj_student, и выведите данные о нём, как о человеке, затем как о студенте.

Например, применим методы к объекту obj_student: """

# class Person:
#     def __init__(self, name, age,):
#         self.name = name
#         self.age = age
#     def display():
#         print()

#         class Person: 
#             def __init__(self,name, age): 
#                 self.name = name 
#                 self.age = age 
#             def display(self): 
#                 return f'name:{self.name}, age:{self.age}' 
# class Student(Person): 
#     def __init__(self, name, age, faculty): 
#         super().__init__(name, age) 
#         self.faculty = faculty 
#     def display_student(self): 
#         info = super().display() 
#         info += f', faculty:{self.faculty}' 
#         return info 
# obj_student = Student('Rick', 21, 'science') 
# print(obj_student.display()) 
# # print(obj_student.display_student())

# class Person: 
#     def __init__(self, name, age): 
#         self.name = name 
#         self.age = age 
#     def display(self): 
#         return f'name:{self.name}, age:{self.age}' 
# class Student(Person): 
#     def __init__(self, name, age, faculty): 
#         super().__init__(name, age) 
#         self.faculty = faculty 
#     def display_student(self): 
#         info = super().display() 
#         info += f', faculty:{self.faculty}' 
#         return info 
#     obj_student = Student('Rick', 21, 'science') 
#     print(obj_student.display()) 
#     print(obj_student.display_student())

""" множественное наследование """

# class Lion:
#     color = 'black'

# class Lioness:
#     color = 'brown'

# class Child(Lion, Lioness):
#     pass

# obj = Child()
# print(obj.color)

# print(Child.__mro__)
# # mro

# class Grandpa:
#     def sleep(self):
#         print("I m sleeping")

# class Grandma:
#     def cook(self):
#         print("I m cooking")

# class Father:
#     last_name = 'Parker'

#     def work(self):
#         print("I m working")

# class Mother(Grandpa, Grandma):
#     last_name = 'Smith'

# class Child(Father, Grandma):
#     pass

# # print(Child.__mro__)
# c = Child()
# print(c.last_name)
# print(dir(c))

""" проблемы множественного наследование  """
# проблема Рамбо - решение при помощи mro

class A:
    pass

class B(A):
    ...

class C(A):
    ...

class D(B, C):
    ...

# D B A C A - > раньше (в один класс заходили два раза)
# D B C A -> сецчас(блпгодаря mro)

""" 
проблема перекресного (скращенного) 
наследование НЕ РЕШЕНА!"""

# class A:
#     ...

# class B:
#     ...

# class C(A, B):
#     ...

# class D(B, A):
#     ...

# class M(C, D):
# #     ...

# class Graph:
#     def __init__(self, pos_x, pos_y, size_x, size_y):
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.size_x = size_x
#         self.size_y = size_x
    
# class MoviMixin:
#     def move(self, pos_x, pos_y):
#         if type(pos_y) and type(pos_x) not in (int, float):
#             raise ValueError(
#                 'Координаты должны быть числом'
#             )

#         self.pos_x = pos_x
#         self.pos_y = pos_y
#     def move(self, pos_x, pos_y)
#         self.pos_x = pos_x
#         self.pos_y = pos_y

#     def resize(self, pos_x, pos_y):
#         self.pos_x = pos_x
#         self.pos_y = pos_y
    
#     def valuidate_values(self, x, y):
#         if type(y) and type(x) not in (int)

# class Triangle(MoviMixin):


""" Mixin -> классы которве изпользуется только для наследования  
Не изпользуется для наследование создание объекта"""


# классы - примеси

# Работа с Миксинами:
# 1. принято давать имена заканчивается на Mixin 
# 2. не принято создавть объекты !!1
# 3. нужно для расширение функционала др класса

class MoveMixin:
    def move(self):
        print('I m move')

class StopMixin:
    def stop(self):
        print('im staying')

class Person(MoveMixin, StopMixin):
    pass

class Car(MoveMixin, StopMixin):
    pass

class River(MoveMixin):
    pass

for obj in [Car(), Car(), Person(), River(), ]:
    obj.move()

class PersonInitMixin:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

# class IncreaseAgeMixin:
#     ...
# class Emplose(PersonInitMixin, IncreaseAgeMixin):
#     ...

# class Emplose(PersonInitMixin, IncreaseAgeMixin):
#     ...

# p = Person('alice', 'Watson', 23)
# p.add_year()
# print(p.age)

# class WriteToFileMixin:
#     def write(self):
#         ...
# class ToDo:
#     def create(self):
#         ...
#     def update(self):
#         ...
#     def delete(self):
#         ...
#     def read(self):
#         ...

# class CreateMixin:
#     def create(self, todo, key):
#         if key in self.todos:
#             return 'Задача под ключом уже сузествует'
#         if todo in self.todos.value():
#             return 'Зфдфча уже сущестыутет'
#         self.todos[key] = todo
#         return self.todos
# class DeleteMixin:
#     def delete(self):
#         if key in self.todos:
#             deleted = self.todos.pop(key)
#             return deleted
#         return 'такой задачи нет'

# class UpdateMixin:
#     def update(self, key, new_todo):
#         self.todos[key] = new_todo
    
# class ReadMixin:
#     def read(self):
#         print(sorted(self.todos.items()))


# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}

# task = ToDo()
# task.create('go shopping', 2)
# task.create('do n/w', 1)
# task.delete(9)
# task.update(1, 'read book')
# task.update(3, 'task a sleep')
# task.read()
# # print(task.todos)

# print()
# print(task.create('do h/w', 2))
    


# class ToDo:
#     todos = {}



# class Car:
#     def __init__(self, BMW, mersedes, audi):
#         self.BMW = BMW
#         self.mersedes = mersedes
#         self.audi = audi
#     def cars(self):
#         print(f'"это немецкая машина"{self.BMW}')

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f'его имя {self.name}, его возраст {self.age}')

a = Human('Jhon', 18)     
print(a.display()) 


import json

FILE = 'user.json'

class RegisterMixin:

    def validate_password(self, password: str, password_confirm):
        if password != password_confirm:
            raise ValueError(
                'Пароли не совпадают'
            )
        elif len(password) < 8:
            raise ValueError(
                'пароль слишком короткий'
            )
        elif password.isdigit() or password.isalpha():
            raise ValueError(
                'Пароль должен состоять тз букв и цифр!'
            )



    def register(self, username, password, password_confirm):
        self.validate_password(password, password_confirm)

        with open(FILE, 'r') as file:
            try:
                data = json.load(file)
                id = data[-1]['id'] + 1
                # print(data)
            except:
                id = 1
                data = []

        with open(FILE, 'w') as file:
            if data:
                is_username_used = any([x['username']==username for x in data])
                if is_username_used:
                        # json.dump(data, file)
                    raise ValueError('Такой username уже существует')
                else:
                    
                    data.append({'id': id, 'username': username, 'password': password})
                    json.dump(data, file)
                    print('Аккаунт успешно создан')

                


            else:
                    data.append({'id': id, 'username': username, 'password': password})
                    json.dump(data, file)
                    print('Аккаунт успешно создан')

class LoginMixin:
    def login(self, username , password):
        with open(FILE, 'r') as file:
            data = json.load(file)
            is_registered = any([x['username'] == username for x in data])
            if not is_registered:
                raise Exception(
                    'Пользователь не найден!Пройтите регистрацию'
                )
            user_data = list(filter(lambda x: ['username'] == username, data))[0]
            print(user_data)
            if user_data['password'] != password:
                raise Exception(
                    'неверный пароль'
                )
            print('Вы успешно вошли в свой аккаунт')

class ChangePasswordmoxon:
    def change_password(self, username, old_password, new_password):
        with open(FILE, 'r') as file:
            data = json.load(file)
            is_registered = any([x['username'] == username for x in data])
            if not is_registered:
                raise Exception(
                    'Пользователь не найден!Пройтите регистрацию'
                )
            user_data = list(filter(lambda x: x['username'] == username, data))[0]
            print(user_data)
            if user_data['password'] != old_password:
                raise Exception(
                    'неверный пароль'
                )
            data.remove(user_data)
            user_data['password'] = new_password
            data.append(user_data)
            with open(FILE, 'w') as file:
                json.dump(data, file)
            print('Пароль успешно изменен')




class User(RegisterMixin, LoginMixin, ChangePasswordmoxon):
    pass

user1 = User()
user2 = User()
# user2.register('test3', '1234567k', '1234567k')
# user1.register('test2', '1234567k', '1234567k')
user1.change_password('test3', '1234567k', 'junPYpack30')

















