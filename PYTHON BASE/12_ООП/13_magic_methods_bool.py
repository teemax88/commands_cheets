class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        print("call __bool__")
        return self.x != 0 or self.y != 0


a = Point(3, 4)
b = Point(0, 0)
print(bool(a))  # call __bool__ True
print(bool(b))  # call __bool__ False

c = Point(5, 7)
d = Point(0, 0)
if c:
    print('hello')
elif d:
    print('world')

print(bool(c))  # call __bool__ True
print(bool(d))  # call __bool__ False
