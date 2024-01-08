class Person:  # parent
    def __init__(self, name):
        # print('init Person')
        self.name = name

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек идет')

    def sleep(self):
        print('Человек спит')

    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()

    def __str__(self):
        return f"Person {self.name}"


class Doctor(Person):  # subclass
    def breathe(self):
        print('Доктор дышит')

    def __str__(self):
        return f"Doctor {self.name}"


d = Doctor('John')
p = Person('Adam')
# print(p, d)
# Вывод
# init Person
# init Person
# Person Adam Doctor John
p.combo()
# Вывод
# Человек дышит
# Человек идет
# Человек спит
d.combo()
# Вывод
# Доктор дышит
# Человек идет
# Человек спит