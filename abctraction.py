""" Абстракция - принцип ООП, в котором  создается пустышка, где задаются название атрибута и методов,
для определение в дочерных классах """

from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty
class A(ABC):
    def metohd1(self):
        print('обычный метод')

    def test(self):
        pass

    # @abstractmethod
    def method2(self):
        print('абстракный метод') # обычно не определяет логику будет обьязательном для переопределение в дочерном классе
        

a = A()

class B(A):
    test = 4
    # def test(self):
    #     method2 = 9
    def method2(self):
        print('переопределили')

# b = B()
# b.metohd1(b.method2)
# a = A() # нельзя создать объект абстракного класса в котором есть абстракный метод


# class AbstractAnimal(ABC):

#     @abstractproperty
#     def pow(self):
#         pass

#     @abstractmethod
#     def voice(self):
#         pass

# class Dog(AbstractAnimal):
#     pow = 4

#     def voice(self):
#         print('гав гав')


# dog = Dog()



class Abct(ABC):
    @abstractmethod
    def get_info(self):
        pass

    def set_info(self):
        pass

class IdenticateMixin:
    def identicate(self, year):
        if int(year) < 2010:
            return 'This is old car'
        return 'This is a new car'

class Auto(Abct , IdenticateMixin):
    def __init__(self, model, year, owner,):
        self.model = model
        self.year = year
        self.__owner = owner
    def get_info(self):
        return f'model: {self.model}\nyear: {self.year}'
    def set_info(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

# auto = Auto('Mersedes-Benz', 2023, 'Ильяс')
# print(auto.get_info())

# print(auto.get_owner())

# auto.set_info('Петр')

# auto.identicate(auto.year)

# class Kamaz(IdenticateMixin, Abct,):
#     get_info = 0
#     set_info = 0

""" должень быть информация метод info -> выводить информацию о студенте getter/setter 

проверка факультета (если it - cool ииначе - not bast)"""

class ABst(ABC):
    @abstractmethod
    def info(self):
        pass
class FacMixin:
    def check(self, faculty):
        if faculty == 'IT':
            print('cool')
        else:
            print('not bad')

class Student:
    def __init__(self, name, last_name, faculty, class_):
        self.name = name
        self.last_name = last_name
        self.faculty = faculty
        self.__class_ = class_
    def info(self):
        print('Инфо студенте')
    @property
    def class_(self):
        return self.__class_
    
    @class_.setter
    def class_(self, new):
        self.__class_ = new
    
a = Student('Adilet', 'Petrov', 'IT', 2)
# a.check(a.faculty)
a.class_ = 3
print(a.class_)


