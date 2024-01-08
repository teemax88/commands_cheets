class Doctor:
    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print("Ура, я отучился на доктора")

    def can_build(self):
        print("Я доктор, я тоже умею строить, но не очень хорошо")


class Builder:
    def __init__(self, rank):
        self.rank = rank

    def can_build(self):
        print("Я строитель, я умею строить")

    def graduate(self):
        print("Ура, я отучился на строителя")


class Person(Doctor, Builder):
    pass


class Person2(Builder, Doctor):
    pass


class Person3(Doctor, Builder):
    def graduate(self):
        print("Посмотрим кем я стал")
        super().graduate()
        Builder.graduate(self)

class Person4(Builder, Doctor):
    def __init__(self, degree, rank):
        super().__init__(rank)
        Doctor.__init__(self, degree)

    def __str__(self):
        return f"Person {self.degree} {self.rank}"

# s = Person()
# s.can_build()  # Я доктор, я тоже умею строить, но не очень хорошо
#
# s2 = Person2()
# s2.can_build()  # Я строитель, я умею строить
# Порядок имеет значение. Поиск метод идет по тому порядку, что задан внутри подкласса.
# То есть, если метод не найден внутри Person, то поиск начнется с первого класса родителя который указан в скобках
# Порядок исполнения называется MRO (method resolution order). Посмотреть его можно так:
# print(Person.__mro__)  # (<class '__main__.Person'>, <class '__main__.Doctor'>, <class '__main__.Builder'>, <class 'object'>)
# print(Person2.__mro__)  # (<class '__main__.Person2'>, <class '__main__.Builder'>, <class '__main__.Doctor'>, <class 'object'>)
#
# s3 = Person3()
# s3.graduate()
# Вывод
# Посмотрим кем я стал
# Ура, я отучился на доктора
# Ура, я отучился на строителя


s4 = Person4(5, 'spec')
print(s4)   # Person 5 spec