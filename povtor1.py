# class GameCharagter:
#     def __init__(self, name, hearth, level):
#         self.name = name
#         self.hearth = hearth
#         self.level = level
#     def speak(self):
#         print(f'Hi, My name is{self.name}')

# class Villain(GameCharagter):

#     def speak(self):
#         super().speak()
#         print(f'Hi, my name is{self.name} and I will kill you')
    
#     def kill(obj, health):
#         obj.health = health
#         print('Bang-bang, now you\'re dead')
        

# obj = GameCharagter('Peter', 100, 23)
# obj.speak()

# obj2 = Villain('Peter', 99, 34)
# obj3 = speak()
# obj = kill(obj)
# print(obj.health)
# 

# import json
# FILE = 'user.json'
# class RegisterMixin:

#     def validate_password(self, password, password_confirm):
#         if password != password_confirm:
#             raise ValueError(
#                'пароли не совпадают'
#             )
#         if len(password) < 8:
#             raise ValueError(
#                 'пароль слишком короткий'
#             )
#         if password.isdigit() or password.isalpha():
#             raise ValueError(
#                 'пароль должень состаятся из сифр'
#             )
    
# #     def register(self, username, password, password_confirm):
# #         self.validate_password(password, password_confirm)

# #         with open(FILE, 'r+') as file:
# #             try:
# #                 data = json.load(file)
# #                 id = data[-1]['id'] + 1
# #             except(IndexError, ValueError):
# #                 id = 1
# #                 data = []

# #             if data:
# #                 ...
# #             else:
# #                 data.append({'id': id, 'username': username, 'password': password})
# #                 json.dump(data, file)
# #                 return {'status': 201, 'msg': 'Аккаунт успешно создан'}
            




# class User:
#     pass




# with open(FILE, 'w') as file:
#     id = 1
#     data = []
#     data.append({'id': id, 
#     'username': username,
#     'password': password})
#     json.dump(data, file)

# class User(RegisterMixin):
#     pass

# user1 = User()
# user2 = User()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f'его имя {self.name}')
#         print(f'его возраст {self.age}')
# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
#     def display_student(self):
#         info = super().display()
#         return info

# obj_student = Student('Rick', 21, 'science')
# print(obj_student())
# # print(obj_student.display_student())

# a = [1, 2, 3, 5, 7, ]
# b = [4, 6, 7, 8, 9]
# print(a + b)



class City:
    def __init__(self, Bishkek, Moscow, Astana):
        self.Bishkek = Bishkek
        self.Moscow = Moscow
        self.Astana = Astana
    def Capital(self):
        print(f'{self.Bishkek} столица Кыргызстана')
        print(f'{self.Moscow} столица Росcии')
        print(f'{self.Astana} столица Казакстана')

citys = City('Бишкек', 'Москва', 'Астана')
print(citys.Capital())

class Continent(City):
    def __init__(self, Korea):
        self.Korea = Korea
    def polina(self):
        super 