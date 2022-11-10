#Coordinate system is (0,0) is upper left corner

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, top_left, width, height):
        self.top_left = top_left
        self.width = width
        self.height = height

    def compute_area(self):
        return self.width * self.height

    def print_coordinates(self):
        top_right = self.top_left.x + self.width
        bottom_left = self.top_left.y + self.height
        print('Starting Point (X)): ' + str(self.top_left.x))
        print('Starting Point (Y)): ' + str(self.top_left.y))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_example_rectangle():
    rectangle_origin = Point(50, 100)
    rectangle = Rectangle(rectangle_origin, 90, 10)

    return rectangle


rectangle = build_example_rectangle()

print(rectangle.compute_area())
rectangle.print_coordinates()



