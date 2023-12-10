""""
Магические методы __len__ и __abs__
__len__ возвращает длину строки
__abs__ возвращает модуль числа
"""


# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __len__(self):
#         return len(self.name + self.surname)
#
#
# w = Person('ecew', 'ceww')
# print(len(w))  # 8

"""Используем пример с числами"""


# class Otrezok:
#     def __init__(self, point1, point2):
#         self.x1 = point1
#         self.x2 = point2
#
#     def __len__(self):
#         return self.x2 - self.x1
#
#
# t = Otrezok(5, 9)
# print(len(t))  # 4 - хорошо если получается положительное число. Если будет отрицательное, то возникнет ошибка

"""Преобразуем наш пример с числами"""


class Otrezok:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self)    # вызовет self.__abs__()

    def __abs__(self):
        return abs(self.x2 - self.x1)


t = Otrezok(5, 9)
print(len(t))  # 4 - вывод нормальный даже если x2-x1 получится отрицательным значением
