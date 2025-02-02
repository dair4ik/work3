class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.length = float(input("Length: "))
        self.width = float(input("Width: "))

    def area(self):
        return self.length * self.width

rectangle = Rectangle()
print("Area of the rectangle:", rectangle.area())  
