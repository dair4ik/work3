class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        self.length = float(input("Enter the length: "))

    def area(self):
        return self.length ** 2

shape = Shape()
print("Area:", shape.area())  

square = Square()
print("Area of square:", square.area())  
