class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x,y)
        self.radius=radius
        
    def printArea(self):
        print("원의면적:", 3.14 * (self.radius ** 2))
        
class Rectangle(Shape):
    def __init__(self, x, y, base, height):
        super().__init__(x,y)
        self.base = base
        self.height = height
        
    def printArea(self):
        print("사각형 면적 = ", self.base * self.height)
        
        
if __name__ == "__main__":
    c1 = Circle(5,6,10)
    c1.printArea()
    r1=Rectangle(100,200,5,6)
    r1.printArea()