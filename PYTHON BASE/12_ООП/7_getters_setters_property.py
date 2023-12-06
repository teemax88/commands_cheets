class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('get balance')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    @my_balance.deleter
    def del_balance(self):
        print('delete balance')
        del self.__balance

    """1 вариант работы с property"""
    # balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)  # вызываем наши функции как атрибуты

    """2 вариант работы с property"""
    # my_balance = property(my_balance)
    # my_balance = my_balance.setter(set_balance)
    # my_balance = my_balance.deleter(delete_balance)


# w = BankAccount('Tom', 500)

"""1 вариант работы с property"""
# print(w.get_balance())  # получаем значение при инициализации экземпляра == 500
#
# # w.set_balance(1000)    # устанавливаем новое значение
# # print(w.get_balance())  # выводим после переопределения == 1000
#
# w.delete_balance()  # удаляем атрибут
# # print(w.get_balance())  # AttributeError: 'BankAccount' object has no attribute '_BankAccount__balance'
#
# w.set_balance(1000)  # снова задаем значение
# print(w.get_balance())  # вывод == 1000


"""2 вариант работы с property"""
# print(w.my_balance)
#
# w.set_balance(1000)  # устанавливаем новое значение
# print(w.get_balance())  # вывод == 1000
#
# w.delete_balance()  # удаляем атрибут
# # print(w.get_balance())  # AttributeError: 'BankAccount' object has no attribute '_BankAccount__balance'
#
# w.set_balance(2000)  # снова задаем значение
# print(w.get_balance())  # вывод == 2000


"""3 вариант работы с property через декоратор"""
# print(w.my_balance)
#
# w.my_balance = 800  # устанавливаем новое значение
# print(w.my_balance)  # вывод == 1000
#
# w.del_balance  # удаляем атрибут
# # print(w.my_balance)  # AttributeError: 'BankAccount' object has no attribute '_BankAccount__balance'
#
# w.my_balance = 1500  # снова задаем значение
# print(w.my_balance)  # вывод == 2000


"""Вычисляемые property"""


class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            print('calculate')
            self.__area = self.__side ** 2
        return self.__area


d = Square(6)
print(d.area)  # calculate 36
print(d.area)  # 36 (свойство заново не вызывается, а считывает прошлое значение, тем самым ускорили код)

d.side = 3
print(d.area)  # # calculate 9 (задав новое значение, мы обнулили прошлое значение в area и запустили расчет снова)
