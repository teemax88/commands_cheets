"""Моносостояние всех экземпляров"""


class Cat:
    __shared_attr = {
        'breed': 'siam',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr


d = Cat()
g = Cat()
print(d.__dict__)  # {'breed': 'siam', 'color': 'black'}
print(g.__dict__)  # {'breed': 'siam', 'color': 'black'}

d.color = 'white'
print(d.__dict__)  # {'breed': 'siam', 'color': 'white'}
print(g.__dict__)  # {'breed': 'siam', 'color': 'white'}

g.name = 'Tom'
print(d.__dict__)  # {'breed': 'siam', 'color': 'white', 'name': 'Tom'}
print(g.__dict__)  # {'breed': 'siam', 'color': 'white', 'name': 'Tom'}
