class Example:
    # def hello():
    #     print('Hello')  # Ошибка. При вызове из экземпляра класса функция ожидала 1 аргумент, но получила 0

    def instance_hello(self):
        print(f'instance_hello {self}')  # instance_hello <__main__.Example object at 0x000002163B5D0E10>

    # обычный вызов из экземпляра класса. вызов НЕдоступен из самого класса, то есть Example.instance_hello() - ошибка

    @staticmethod
    def static_hello():
        print(f'static_hello')  # static_hello

    # вызов доступен как из экземпляра класса, так и из самого класса, то есть Example.static_hello() - успешно

    @classmethod
    def class_hello(cls):
        print(f'class_hello {cls}')  # class_hello <class '__main__.Example'>
    # вызов доступен как из экземпляра класса, так и из самого класса, то есть Example.static_hello() - успешно
    # но из экземпляра все равно будет связь с классом. Этот метод лучше применять для обработки данных внутри класса


q = Example()

q.instance_hello()  # instance_hello <__main__.Example object at 0x0000026808630E10>

Example.static_hello()  # static_hello
q.static_hello()  # static_hello

q.class_hello()  # class_hello <class '__main__.Example'>
Example.class_hello()  # class_hello <class '__main__.Example'>
