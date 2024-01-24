class O: ...

class A(O): ...
class B(O): ...
class C(O): ...
class D(O): ...
class E(O): ...

class K1(C, A, B): ...
class K2(A, D): ...
class K3(B, D, E): ...

class Z(K1, K2, K3): ...


print(Z.mro())
print(Z.__mro__)


def get_mro(cls):
    print(*[c.__name__ for c in cls.mro()], sep=' -> ')

get_mro(Z)  # Z -> K1 -> C -> K2 -> A -> K3 -> B -> D -> E -> O -> object


class Music(object): pass
class Rock(Music): pass
class Gothic(Music): pass
class Metal(Rock): pass
class GothicRock(Rock, Gothic): pass
class GothicMetal(Metal, Gothic): pass
class The69Eyes(GothicRock, GothicMetal): pass

print(The69Eyes.mro())

def get_mro(cls):
    print(*[c.__name__ for c in cls.mro()], sep=' -> ')

get_mro(The69Eyes)  # The69Eyes -> GothicRock -> GothicMetal -> Metal -> Rock -> Gothic -> Music -> object



class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!