"""
Factory Method: Позволяет создавать объекты без указания конкретного класса, делегируя создание подклассам.
"""

class Button(object):
   html = ""
   def get_html(self):
      return self.html

class Image(Button):
   html = "<img></img>"

class Input(Button):
   html = "<input></input>"

class Flash(Button):
   html = "<obj></obj>"

class ButtonFactory():
   def create_button(self, _type):
      # targetclass = typ.capitalize()
      # return globals()[targetclass]()
      return _type()

button_obj = ButtonFactory()
button = [Button, Input, Flash]
for b in button:
   print(button_obj.create_button(b).get_html())

# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_factory.htm

# ///////////////**************///////////////

from abc import ABC, abstractmethod

class Factory(ABC):
    @abstractmethod
    def create_product(self):
        pass

class FactoryA(Factory):
    def create_product(self):
        return ProductA()

class FactoryB(Factory):
    def create_product(self):
        return ProductB()

class Product(ABC):
    @abstractmethod
    def description(self):
        pass

class ProductA(Product):
    def description(self):
        return "Product A"

class ProductB(Product):
    def description(self):
        return "Product B"

# Usage
factory1 = FactoryA()
product1 = factory1.create_product()
print(product1.description())

factory2 = FactoryB()
product2 = factory2.create_product()
print(product2.description())