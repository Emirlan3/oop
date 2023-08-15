class Dog:
    def __init__(self, name, age):
       self.name = name
       self.age = age
    def bark(self):
       print("gav gav!")
    def doginfo(self):
       print(self.name + " is " + str(self.age) + " is(s) years.")
ak_tosh = Dog("Ak-Tosh", 2)
rex = Dog("Rex", 12)
bobik = Dog("Bobik", 8)
ak_tosh.doginfo()
rex.doginfo()
bobik.doginfo()