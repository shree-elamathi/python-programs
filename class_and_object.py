class rectangle():
    def __init__(self,l,w):
        self.length =l
        self.width =w
    def area(self):
        return self.length*self.width
class circle:
    def __init__(self,r):
        self.radius =r
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return 2*self.radius*3.14
newRectangle=rectangle(12,10)
print("Area of rectangle",newRectangle.area())
newcircle=circle(8)
print("Area of circle is",newcircle.area())
print("Perimeter of circle is",newcircle.perimeter())
