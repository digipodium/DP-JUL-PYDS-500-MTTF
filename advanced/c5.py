class Shape:

    def __init__(self, side):
        self.side = side

    def info(self):
        return f'shape with {self.side} sides'

    
class Rectangle(Shape):

    def __init__(self, l, w):
        super().__init__(l)
        self.w = w

    def area(self):
        return self.side * self.w # side is taken as length 

    # overidden function
    def info(self):
        return f'rectangle with l = {self.side} & w = {self.w}'

ob1 = Shape(4)
print(ob1.info())

ob2 = Rectangle(4,5)
print(ob2.area())
print(ob2.info())


