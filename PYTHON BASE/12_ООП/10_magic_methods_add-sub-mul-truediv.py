""""
Магические методы __add__, __sub__, __mul__, __truediv__
__add__ для операции сложения
__sub__ для операции вычитания
__mul__ для операции умножения
__truediv__ для операции деления
"""


class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.second = seconds

    def get_time(self):
        s = self.second % 60
        m = (self.second // 60) % 60
        h = (self.second // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other: int):
        if not isinstance(other, int):
            raise ArithmeticError("Правый операнд должен быть целым числом")
        return Clock(self.second + other)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть целым числом или Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.second

        self.second += sc
        return self


"""Процесс метода __add__
когда мы сделали c1 = Clock(100), то получилось second=1000
а когда c1 = c1 + 100, то получилось c1.__add__(100) и следовательно Clock(c1.second + 100), что равно second=1000 
НО - если поменять местами и сделать: c1 = 100 + c1, то будет ошибка. Избежать это помогут доп методы radd и iadd
"""

# c1 = Clock(1000)
# print(c1.get_time())  # 00:16:40
# c1 = c1 + 100
# print(c1.get_time())  # 00:18:20
#
# c1 = 100 + c1
# print(c1.get_time())  # 00:20:00 - тут срабатывает radd
#
# c1 += 100
# print(c1.get_time())  # 00:21:40 - тут срабатывает __iadd__

"""Пример использования методов с другого занятия
"""


class Vector:
    def __init__(self, *args):
        t = []
        for i in args:
            if isinstance(i, int):
                t.append(i)
        self.values = sorted(t)

    def __str__(self):
        if self.values:
            b = [str(i) for i in self.values]
            return f"Вектор ({','.join(b)})"
        else:
            return "Пустой вектор"

    def __add__(self, other):
        if isinstance(other, int):
            g = [i + other for i in self.values]
            return Vector(*g)
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                z = [i for i in zip(self.values, other.values)]
                print(*z)  # пример вывода zip(). Поступают значения (1,2,5) и (2,5,7). Вывод: (1, 2) (2, 5) (5, 7)
                m = [sum(i) for i in zip(self.values, other.values)]
                return Vector(*m)
            else:
                return "Сложение векторов разной длины недопустимо"
        else:
            return f"Вектор нельзя сложить с {other}"

    def __mul__(self, other):
        if isinstance(other, int):
            g = [i * other for i in self.values]
            return Vector(*g)
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                z = [i for i in zip(self.values, other.values)]
                print(*z)  # пример вывода zip(). Поступают значения (1,2,5) и (2,5,7). Вывод: (1, 2) (2, 5) (5, 7)
                m = [i[0]*i[1] for i in zip(self.values, other.values)]
                return Vector(*m)
            else:
                return "Умножение векторов разной длины недопустимо"
        else:
            return f"Вектор нельзя умножать с {other}"

a = Vector(5, 2, 1)
print(a)  # Вектор (1,2,5)

b = Vector(2, 5, 7)
print(b)  # Вектор (2,5,7)

print(a + b)  # Вектор (3,7,12)
print(a + 5.0)  # Вектор нельзя сложить с 5.0

print(a * b)  # Вектор (2,10,35)
print(a * 5.0)  # Вектор нельзя умножать с 5.0

c = Vector(6, 8, 4, 2)
print(a * c)  # Умножение векторов разной длины недопустимо

v = Vector()
print(v)  # Пустой вектор
