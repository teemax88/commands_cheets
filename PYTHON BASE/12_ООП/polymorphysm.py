"""
Полиморфизм - это возможность обработки разных объектов путем использования одног и того же метода

Полиморфизм позволяет объектам разных классов обладать общим интерфейсом и выполнять одни и те же действия по-разному.
В Python полиморфизм достигается за счет переопределения методов в производных классах.

"""

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Rectangle {self.a}x{self.b}"

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"Square {self.a}x{self.a}"

    def get_area(self):
        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f"Circle radius = {self.r}"

    def get_area(self):
        return 3.14 * self.r ** 2


rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)

sq1 = Square(5)
sq2 = Square(7)

cir1 = Circle(3)
cir2 = Circle(2)

figures = [rect1, rect2, sq1, sq2, cir1, cir2]
for figure in figures:
    print(figure, figure.get_area())
# Вывод
# Rectangle 3x4 12
# Rectangle 12x5 60
# Square 5x5 25
# Square 7x7 49
# Circle radius = 3 28.26
# Circle radius = 2 12.56