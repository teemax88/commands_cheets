class Example:

    counter = 0
    example_value = 10

    @staticmethod
    def hello():
        print("I AM HERE TO ROCK!")
        pass

    @classmethod
    def class_mod(cls):
        cls.counter += 1

    @property
    def property(self):
        return self.example_value + 1

# e = Example()
# e1 = Example()
# e2 = Example()
# e3 = Example()
# 
# print(e.counter)
# e2.class_mod()
# e1.class_mod()
# e2.class_mod()
# print(e.counter)
# 
# e4 = Example()
# print(e4.counter)
