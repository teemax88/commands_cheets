"""
Singleton: Гарантирует, что у класса есть только один экземпляр, и предоставляет глобальную точку доступа к нему.
"""


class Singleton:
    foo = 1
    bar = 2


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class MyClass:
    pass


class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class MyClassSecond(Singleton):
    pass


# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

# ////////////**************************/////////////////

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Usage
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True, так как это один и тот же экземпляр (instance)
