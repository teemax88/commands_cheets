class Person:  # parent
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Person {self.name} {self.surname}"

    def breathe(self):
        print('Человек дышит')


class Doctor(Person):  # subclass
    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f"Doctor {self.name} {self.surname}"


p = Person('Ivan', 'Ivanov')
d = Doctor('Petr', 'Petrov', 25)
print(p.name, p.surname)
print(d.name, d.surname, d.age)


# Вывод:
# Ivan Ivanov
# Petr Petrov 25

# //////////////////************************************/////////////////////////

class Cat:
    favorite_food = []

    def __init__(self, name):
        self.name = name

    def add_food(self, food):  # Method modifying the class variable
        self.favorite_food.append(food)


kitty = Cat('Kitty')
barsik = Cat('Barsik')
kitty.add_food('salmon')
print(barsik.favorite_food)  # ['salmon']
print(kitty.favorite_food)  # ['salmon']
