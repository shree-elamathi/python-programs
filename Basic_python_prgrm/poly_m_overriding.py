class square:
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length*self.length
class rectangle(square):
    def __init__(self,length,width):
        super().__init__(length)
        self.width=width
    def area (self):
        return self.length*self.width

#main program
s=square(10)
print("s.area=",s.area())
s=rectangle(10,20)
print("s.area=",s.area())
