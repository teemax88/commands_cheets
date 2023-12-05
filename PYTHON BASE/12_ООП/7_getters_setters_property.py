class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')
        return self.__balance

    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)  # вызываем наши функции как атрибуты


w = BankAccount('Tom', 500)

print(w.get_balance())  # получаем значение при инициализации экземпляра == 500

# w.set_balance(1000)    # устанавливаем новое значение
# print(w.get_balance())  # выводим после переопределения == 1000

w.delete_balance()  # удаляем атрибут
# print(w.get_balance())  # AttributeError: 'BankAccount' object has no attribute '_BankAccount__balance'

w.set_balance(1000)  # снова задаем значение
print(w.get_balance())  # вывод == 1000
