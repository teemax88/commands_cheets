class Point:
    def __init__(self, coord_x=0, coord_y=0):
        self.x = coord_x
        self.y = coord_y

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.x = 0
        self.y = 0


p = Point()
print(p.__dict__)  # {'x': 0, 'y': 0}

p2 = Point(10, 20)
print(p2.__dict__)  # {'x': 10, 'y': 20}
p2.move_to(30, 40)
print(p2.__dict__)  # {'x': 30, 'y': 40}


"""Опитимизация класса выше по принципу DRY"""


class Point:
    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)


p3 = Point()
print(p3.__dict__)  # {'x': 0, 'y': 0}
p3.move_to(5, 5)
print(p3.__dict__)  # {'x': 5, 'y': 5}
p3.go_home()
print(p3.__dict__)  # {'x': 0, 'y': 0}
