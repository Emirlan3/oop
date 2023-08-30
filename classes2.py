# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#     def show_title(self):
#         print(f'Названии этой песни {self.title}')
#     def show_author(self):
#         print(f'Автор этой песни {self.author}')
#     def show_year(self):
#         print(f'Это песня вышла в {self.year} году')

# song = Song('Happy', 'Pharrel Williams', '2013')
# song.show_title()
# song.show_author()
# song.show_year()


# class A:
#     pass
# a = A()
# print(isinstance(a, A))


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
#     class Student:
#         ...
#     obj_student = Student('Rick', 21, 'science') 
#     print(obj_student.display()) 

# class Auto:
#     def __init__(self, ride):
#         self.ride = ride
#     def self.ride():
#     print(f'ridding on a ground{self.ride}')

# a = Auto('car')
# print(self.ride())
    
    
# class Polygon:
#     width = 0
#     height = 0
#     def set_values( self, width, height):
#         Polygon.width = width
#         Polygon.height = height

# class Rectangle(Polygon):
#     def area(self):
#         return self.width * self.height

# class Triangle(Polygon):
#     def area(self):
#         return(self.width * self.height) / 2

# rect = Rectangle()
# trey = Triangle()

# rect.set_values(4, 5)
# trey.set_values(4, 5)


# class Car:
#     def __init__(self, BMW, mersedes, audi):
#         self.BMW = BMW
#         self.mersedes = mersedes
#         self.audi = audi
#     def cars_BMW(self):
#         print(f'это немецкая машина {self.BMW}')
#     def cars_mersedes(self):
#         print(f'марка этой машины {self.mersedes}')
#     def cars_audi(self):
#         print(f'это машина называется {self.audi}')


# carsing = Car('BMW', 'mersedes', 'audi')
# carsing.cars_BMW()
# carsing.cars_mersedes()
# carsing.cars_audi()

# class Auto:
#     def ride(self):
#         print(f'riding on a ground')

# class Boat:
#     def swim(self):
#         print(f'floating on water')

# class Amphibian(Auto, Boat):
#     pass
# obj = Amphibian()
# obj.ride()
# obj.swim()


