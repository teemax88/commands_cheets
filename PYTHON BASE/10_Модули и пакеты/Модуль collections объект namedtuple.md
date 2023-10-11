```python
"""
namedtuple позволяет создавать именованные кортежи и дает возможность обращаться к элементам кортежа по имени
"""
from typing import NamedTuple
from collections import namedtuple
from datetime import datetime

Human = namedtuple('Person', 'name surname birthday city')  # создали класс Person с атрибутами к которым можем обращ.
# (атрибуты через пробел) и всё это присвоили в переменную Human
z = Human('Asmolovskii', 'Andrey', '1983-06-30', 'Kharkov')  # добавили переменную z в класс Human
print(z)  # Person(name='Asmolovskii', surname='Andrey', birthday='1983-06-30', city='Kharkov')
print(z._asdict())  # представит z в виде словаря
# {'name': 'Asmolovskii', 'surname': 'Andrey', 'birthday': '1983-06-30', 'city': 'Kharkov'}
print(z.surname)  # Andrey вызов параметра
# чтобы в кортеже изменить параметр можно сделать
z = z._replace(surname='Kris')  # заменит атрибут surname (можно изменить на любой тип данных (123 например))
print(z)  # Person(name='Asmolovskii', surname='Kris', birthday='1983-06-30', city='Kharkov')


# можно в классе сделать какой тип данных будет приниматься в параметрах
class People(NamedTuple):
    name: str
    surname: str
    date: str
    country: str
p = People('Megan', 'Jones', '1998:07:16', 'Bolivia')
print(p) # People(name='Megan', surname='Jones', date='1998:07:16', country='Bolivia')

# Класс collections.namedtuple позволяет создать тип данных, ведущий себя как кортеж, с тем дополнением,
# что каждому элементу присваивается имя, по которому можно в дальнейшем получать доступ:
#
# >>> Point = namedtuple('Point', ['x', 'y'])
# >>> p = Point(x=1, y=2)
# >>> p
# Point(x=1, y=2)
# >>> p.x
# 1
# >>> p[0]
# 1
```