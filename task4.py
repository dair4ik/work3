import math

class Point:
    def __init__(self):
        self.x = float(input("Input x coordinate: "))
        self.y = float(input("Input y coordinate: "))

    def show(self):
        print(f"Coordinates of point: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


p1 = Point()
p2 = Point()

p1.show()
p2.show()

print("Distance:", p1.dist(p2))


new_x = float(input("Enter new x for p1: "))
new_y = float(input("Enter new y for p1: "))
p1.move(new_x, new_y)
p1.show()
