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
    def __init__(self,  owner: str, model: str, year: int):
        self.owner = owner
        self.model = model
        self.year = year
        self.mileag = 0
        self.is_going = False

    def go(self, km):
        print('Who')
        self.mileag += km
        self.mileag += km
        # self.mileag = self.mileag + km
        self.is_going = True

new_car = Car('Эмирлан', 'Мерс 500', 2023)
print(new_car.mileag, new_car.is_going)
new_car.go(100)
new_car.go(15)
print(new_car.mileag, new_car.is_going)

class Selfbank:
    total = 0 
    def add_sum(self, zp):
        self.total += zp
    """ учет дохода """
    def get_total_sum(self,):
        print(self.total)
    """ просмотр текщего баланса """
    def sub_sum(self, sum_):
        if self.total < sum_:
            raise Exception( 'Не достаточно средств')
        self.total = sum_
    """ учет расходов """
    # Примечание: сумма расхода не должна превышать сумму текщего баланса

jonn = Selfbank()
jonn.get_total_sum()
jonn.add_sum(1000)
jonn.sub_sum(500)
jonn.sub_sum(800)

""" объявите класс Student с атрибутами экзампляра класса  name, last_name, books = [], 
knowlage = 0, is_ready_to_work = False = [], Languages = []

метод read_books -> добавляет и увеличивает knowlage на 100 

метод do_home_work -> увеличивает знание на 200

метод learn_new_language -> добавляет новый язык и уровень владение им, 
увеличивает знание на 20 languages = {язык: 100}
метод add_points -> увеличивает знание и проверяет готовность к работе
"""

class Student:
    def __init__(self, name, last_name, books):
        self.last_name = name
        self.name = last_name
        self.books = []
        self.knowlage = 0
        self.is_ready_to_work = False
        self.languages = {}

    def read_book(self, book):
        self.books.append(book)
        self.add_points(100)
    
    def do_home_work(self):
        self.add_points(30)

    def do_real_project(self):
        self.add_points(200)

    def learn_languages(self):
        self.languages


    def add_points(self, point):
        self.knowlage += point
        if self.knowlage >= 1000:
            print(f'{self.name} is ready to work')
            self.is_ready_to_work = True

sam = Student('Sam', 'Brown')
sam.do_real_project()
sam.read_book('testing')
sam.read_book('грокаем алгоритмы')
sam.do_home_work
sam.do_home_work
sam.do_home_work
sam.do_home_work
sam.do_home_work
sam.do_home_work
sam.do_home_work
sam.do_home_work
sam.learn_languages('python', 100)
sam.learn_languages('java', 40)
sam.learn_languages('c++', 30)
sam.do_real_project()
sam.do_real_project()
print(sam)

class Song:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def show_title(self):
        print('Название этой песнии{self.title}')
    def show_author(self):
        print('Автор этой песнии {author}')

    def show_year(self):
        print('Это песня вышла {year}')

song = Song('Happy', 'Eminem', 1998)
song.show_title()
song.show_author()
song.show_year()
print(song)



class Polygon:
    width = 0
    height = 0
    def set_values( self, width, height):
        Polygon.width = width
        Polygon.height = height

class Rectangle(Polygon):
    def area(self):
        return self.width * self.height

class Triangle(Polygon):
    def area(self):
        return(self.width * self.height) / 2

rect = Rectangle()
trey = Triangle()

rect.set_values(4, 5)
trey.set_values(4, 5)

    



