
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