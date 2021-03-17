# 1.10.1
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'x: {self.x} \ny: {self.y} \nwidth: {self.width} \nheight: {self.height}'


figure = Rectangle(5, 10, 50, 100)
print(figure)

# 1.10.2
class Rectangle_2D:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return f"2D_Rectangle {self.width} {self.height} {self.width * self.height}"


figure = Rectangle_2D = Rectangle_2D(5, 10)
print(Rectangle_2D.get_area())
