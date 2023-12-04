# ВВЕДЕНИЕ В КЛАССЫ
class Person:
    name = 'Ivan'
    age = 20


print(Person.__dict__)
# mappingproxy({'__module__': '__main__', 'name': 'Ivan', 'age': 20, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None, '__annotations__': {}})

print(getattr(Person, 'name'))  # Ivan
print(getattr(Person, 'x', 100))  # 100 - значение по умолчанию, если обратиться к отсутствующему атрибуту

setattr(Person, 'name', 'Oleg')
print(Person.__dict__)  # в списке будет переопределенный атрибут name со значением 'Oleg'
p = Person()
print(p.name)  # Oleg

# переопределить можно и так:
Person.name = 'Misha'
print(Person.__dict__)

# если пытаться заменить несуществующий атрибут, то Python автоматически его создаст
Person.x = 100
print(Person.__dict__)

# удаление атрибута
del Person.x
print(Person.__dict__)  # атрибута Х уже не будет

delattr(Person, 'age')
print(Person.__dict__)  # атрибута age уже не будет


# Атрибуты класса
class Car:
    model = 'BMW'
    engine = 1.6


a1 = Car()
a2 = Car()

# хоть мы и получили доступ к содержимому класса, сами экземпляры пустые (у них нет атрибутов)
print(a1.__dict__)  # {}
print(a2.__dict__)  # {}

# атрибуты появятся, если их создать в экземпляре (и применяться только к нему)
a1.seat = 4
print(a1.seat)  # 4
print(a1.__dict__)  # {'seat': 4}

# также атрибут появится в экземпляре, если перезаписать имеющийся в классе атрибут
a1.model = "Lada"
print(a1.model)  # Lada
print(a1.__dict__)  # {'seat': 4, 'model': 'Lada'}


# функции в классах
class Car:
    model = 'BMW'
    engine = 1.6

    def drive():
        print("Let's GO")


Car.drive()  # Let's GO
print(Car.__dict__)  # среди методом будет 'drive': <function Car.drive at 0x0000023555525C60>

a = Car()
print(a.drive)  # если без вызова, то будет показано что это <bound method Car.drive of <__main__.Car object at 0x000001DC926D1190>>

# если с вызовом, то появится ошибка
print(a.drive())  # TypeError: Car.drive() takes 0 positional arguments but 1 was given
# чтобы не было ошибки, нужно либо указать у функции параметр self, либо вставить над ней декоратор @staticmethod
