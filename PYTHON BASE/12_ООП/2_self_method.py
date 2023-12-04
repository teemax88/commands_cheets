""""Методы экземпляра. Параметр self"""


# class Cat:
#     def hello(*args):
#         print("Hello world from kitty. ARGS function hello() == ", args)
#
#
# jim = Cat()
# jim.hello()  # Hello world from kitty. ARGS function hello() ==  (<__main__.Cat object at 0x000001B34F810950>,)
# # 0x000001B34F810950 - это адрес памяти, где находится объект. В другом экземпляре адрес будет другим, так как это будут 2 разных объекта


class Cat:
    breed = 'pers'

    def hello(*args):
        print("Hello world from kitty. ARGS function hello() == ", args)

    def show_breed(instance):
        print(f"My breed is {instance.breed}")

    def show_name(instance):
        if hasattr(instance, 'name'):
            print(f"My name is {instance.name}")
        else:
            print('NOTHING')

    def set_value(cat, value, age=0):
        cat.name = value
        cat.age = age


walt = Cat()
walt.show_breed()  # My breed is pers
print(walt.__dict__)  # {}
walt.breed = 'siam'
walt.show_breed()  # My breed is siam
print(
    walt.__dict__)  # {'breed': 'siam'} - после переопределения, атрибут создается внутри экземпляра. Если создать другой экз-р, то у него будет старое значение атрибута

mari = Cat()
mari.show_name()  # NOTHING, так как атрибута name у нас нету
mari.name = "Mary"  # задали и создали атрибут name
mari.show_name()  # My name is Mary

tom = Cat()
tom.show_name()  # NOTHING
tom.set_value('Tom')
print(tom.name)  # Tom
tom.show_name()  # My name is Tom
