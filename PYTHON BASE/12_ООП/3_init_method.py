class Cat:
    def __init__(self, name, breed, age=3, color='black'):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


tom = Cat('Tom', 'siam')
print(tom.__dict__)  # {'name': 'Tom', 'breed': 'siam', 'age': 3, 'color': 'black'}

walt = Cat('Walt', 'pers', 1, 'white')
print(walt.__dict__)  # {'name': 'Walt', 'breed': 'pers', 'age': 1, 'color': 'white'}
