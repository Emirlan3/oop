class A:
    def __init__(self , name, age):
        self.name = name
        self.age = age
    def func(self):
        return 'вывод'

obj2 = A('qwerty1', '123')
print(obj2.name)
print(obj2.age)
class B(A):
    def __init__(self, password, name):
        super().__init__(self, name)
        self.password = password

obj = B('qwerty', 'asdf')
print(obj.name)
