from typing import Any


class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_password(self, username):
        if self.username == username:
            return self.__password
        else:
            return "NO!!!"
    
    def set_password(self, old_password, new_password):
        if self.__password == old_password:
            self.password = new_password
        else:
            return "NO!!!"
        


    def __get_info(self):
        print(f"Username, {self.username}, password {self.__password}")

user1 = User(username = 'makers', password = 'makers123')
print(user1.username)
print(user1.get_password(username = 'makers'))
user1.set_password(old_password = 'makers123',
                   new_password='emirlan777')
print(user1.get_password(username='makers'))
print(user1.get_password(username='makers'))



class Divider:
    def __init__(self):
        self.__divide_num = 1
    
    def divide(self, value):
        return value / self.__divide_num
    

obj = Divider()
# obj.divide_num = 0
print(obj.divide(7))
# print(obj.divide_num)
print(obj._Divider__divide_num)



class Person:
    def __init__(self, name, password):
        self.name = name
        self.__password = password
    def get_password(self, name):
        if self.name == name:
            return self.__password
        
    def set_password(self, new_password, old_password):
        if self.__password == old_password:
            self.__password == new_password
        else:
            return 'NO'
    
    def get_info(self):
        print(f"Username {self.name}, password {self.__password}")
        
person1 = Person(name = 'emirlan', password = 'makers23' )
print(person1.name)
print(person1.get_password(name = 'emirlan'))
person1.set_password(old_password = 'makers23',
                     new_password= 'bootcamp')
print(person1.get_password(name = 'emirlan'))
print(person1.get_password(name = 'emirlan'))





# class Car:
#     def __init__(self, model):
#         self.__model = model

#     @property
#     def get __model()
    
#     model = property(lambda self: self.__model)

# car = Car('Toyota')
# print(car.model)


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        print('getter')
        return self.__radius
    
    def set_radius(self, value):
        print('setter')
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            return ValueError(
                'Invalid value, must be, an int or float object'
            )
        
        self.__radius = value

    def del_redous(self):
        print('deletter')
        del self.__radius

    radius = property(get_radius, set_radius, del_redous, doc = 'The private radius property')


circle = Circle(5)
print(circle.radius)
circle.radius = 0
del circle.radius


class Car:
    def __init__(self, model, age):
        self.model = model
        self.__age = age
     
    def cars(self):
        print(f'Марка машины {self.model}, год выпуска {self.__age}')

car = Car('Mersedes', '2010')
print(car.cars())



"""
1.Создайте класс PrivateProject. Внутри этого класса есть атрибуты класса: github_link и developers.
В github_link хранится ссылка на проект (любая), а в developers хранится список с юзернеймами, у которых есть доступ к этой ссылке (атрибуту github_link).
Создайте объект класса PrivateProject, при создании необходимо передать в качестве аргумента username.
Далее, попытайтесь через созданный объект класса получить атрибут github_link. При этом, если данный username есть в списке developers, ему открыт доступ к ссылке.
В противном случае выводится сообщение: Forbidden. Список developers должен быть скрыт.
"""

class PrivateProject:
    def __init__(self, github_link, developers):
        self.github_link = github_link
        self.__developers = developers
    def github(self):
        print({self.github_link}, url = 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg')
    def __developers(self):
        self.github_link == self.__developers

class PrivateProject:
    __github_link = 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg'
    __developers = ['test', 'admin']
    
    def __init__(self, username):
        self.username = username

    
    @property
    def github_link(self):
        if self.username in self.__developers:
            print(self.__github_link) 
        else:
            print('Forbidden')   

pp = PrivateProject('test')
pp.github_link



        

"""
2.Создайте класс User. В этом классе есть защищенный метод _create_user, который принимает email и password. 
Этот метод вызывается в публичных методах create_user и create_superuser. 
Оба метода отличаются друг от друга тем, что в методе create_user атрибут is_superuser имеет значение False, 
а в методе create_superuser - True.
Также в классе есть метод admin_login, который принимает password.
Создайте два объекта от класса User. К первому объекту примените метод create_superuser, а ко второму - create_user. Далее у обоих объектов вызовите метод admin_login, передав правильные пароли.
У первого объекта должно выдаваться сообщение Successfully logged in, а у второго - Forbidden, так как поле is_superuser у второго объекта имеет значение False. Также если даже is_superuser у первого объекта True, ему не удасться залогиниться, если он передал неправильный пароль password в метод admin_login и ему выдается сообщение: Invalid password.
"""

# class User:
#     def _cteate_user(self, email, password):
#         self.email = email
#         self.__password = password
#     def create_user(self, email, password):
#         self.email = email
#         self.__password = password
    
#     def create_superuser(self, email, password):



class ValidateMixin:
    def validate_password(self, password):
        if len(password) < 4:
            raise Exception(
                'Too short password, at least 4 symbols'
            )
        if password.isdigit() or password.isalpha():
            raise Exception(
                'Password must contain numbers and integers'
            )
        return password
    def validate_email(self, email):
        if '@' in email:
            raise Exception(
                'It is not email'
            )
        return email

    



# class Coordinateerror(Exception):
#     pass




