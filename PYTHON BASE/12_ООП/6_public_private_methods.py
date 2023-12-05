class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_public_data(self):
        self.__print_private_data()

    # def print_protected_data(self):
    #     print(self._name, self._balance, self._passport)

    def __print_private_data(self):  # приватным можно делать и саму функцию (метод). Тогда она будет доступна только внутри класса
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 100000, 456789456)
# account1.print_public_data()
# account1.print_protected_data() # Bob 100000 456789456
# print(account1._name)   # Bob
# print(account1._balance)    # 100000
# print(account1._passport)   # 456789456

# account1.print_private_data()  # Bob 100000 456789456 (инкапсуляция. Мы даем возможность получить данные объекта через метод, но не отдельным вызовом)
# print(account1.__name)   # AttributeError
# print(account1.__balance)    # AttributeError
# print(account1.__passport)   # AttributeError

# account1.print_public_data()  # Bob 100000 456789456
print(dir(account1))  # ['_BankAccount__balance', '_BankAccount__name', '_BankAccount__passport', и так далее
account1._BankAccount__print_private_data()  # Bob 100000 456789456
