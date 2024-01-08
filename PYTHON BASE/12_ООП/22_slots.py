"""
Slots - это ограничение атрибутов.
Объекты занимают меньше места в памяти, так как словарь атрибутов __dict__ уже встроен внутрь
А также операции с объектами где есть slots выполняются быстрее
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(3, 4)
print(p1.__dict__)  # {'x': 3, 'y': 4}
print(p1.x)  # 3
print(p1.y)  # 4

p2 = PointSlots(7, 9)
# print(p2.__dict__)  # AttributeError: 'PointSlots' object has no attribute '__dict__'{'x': 3, 'y': 4}
print(p2.x)  # 7
print(p2.y)  # 9

p2.y = 50
print(p2.y)  # 50

del p2.y
# print(p2.y)  # AttributeError: 'PointSlots' object has no attribute 'y'

p2.y = 100
print(p2.y)  # 100

print('===' * 10)



