import math


class Circle:
    def __init__(self, radius=0):
        self.radius = radius
        
    def getArea(self):
        return math.pi * self.radius * self.radius
    
    def getPerimeter(self):
        return 2 * math.pi * self.radius
    
    def setRadius(self, radius):
        self.radius = radius
        
    def showRadius(self):
        return self.radius
    
    
circle1 = Circle(5)
print("원의 반지름 : ", circle1.showRadius())
print("원의 면적 : ", circle1.getArea())
print("원의 둘레 : ", circle1.getPerimeter())

print("====== \n")

circle1.setRadius(3)
print("원의 반지름 : ", circle1.showRadius())
print("원의 면적 : ", circle1.getArea())
print("원의 둘레 : ", circle1.getPerimeter())

circle2 = Circle()
circle2.setRadius(5)
print("원의 반지름 : ", circle2.showRadius())
print("원의 면적 : ", circle2.getArea())
print("원의 둘레 : ", circle2.getPerimeter())

