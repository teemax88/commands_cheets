"""

Инкапсуляция позволяет скрыть детали реализации класса от внешнего мира и обеспечить доступ к атрибутам и методам только через интерфейс класса.
В Python инкапсуляция часто реализуется с помощью атрибутов и методов, имеющих префиксы одного или двух подчеркиваний.

"""


class Cat:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age


cat = Cat("Whiskers", 3)
print(cat.get_age())  # Accessing private attribute using a getter method
cat.set_age(4)  # Modifying private attribute using a setter method
print(cat.get_age())  # Output: 4
