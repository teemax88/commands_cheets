""""
Магические методы __str__ и __repr__
__repr__ отвечает за то, как данные класса будут видны в системе, как их будут видеть разработчики
__str__ отвечает за то, как данные класса будут видны пользователям
"""


class Lion:
    def __init__(self, name):
        self.name = name

    # def __repr__(self):
    #     return f"The object Lion - {self.name}"

    def __str__(self):
        return f"Lion - {self.name}"


q = Lion("Bob")
print(q)  # без repr вывод будет таким: <__main__.Lion object at 0x00000198E2DE05D0>
print(str(q))  # без repr вывод будет таким: <__main__.Lion object at 0x00000198E2DE05D0>

w = Lion("Simba")
print(w)  # вывод с методом repr будет таким: The object Lion - Simba
print(str(w))   # вывод с методом repr будет таким: The object Lion - Simba

q = Lion("Tim")
print(q)  # вывод с методом repr будет таким: Lion - Tim
print(str(q))   # вывод с методом repr будет таким: Lion - Tim