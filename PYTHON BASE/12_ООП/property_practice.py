from string import digits


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = 'abracadabra'

    @property
    def secret(self):
        s = input('Введите ваш пароль: ')
        if s == self.password:
            return self.__secret
        else:
            raise ValueError('Доступ закрыт')

    @property
    def password(self):
        print('getter called')
        return self.__password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) < 4:
            raise ValueError('Длина пароля слишком мала, должно быть минимум 4 символа')
        if len(value) > 12:
            raise ValueError('Длина пароля слишком велика, должно быть максимум 12 символов')
        if not User.is_include_number(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        self.__password = value


a = User('awa', "12dwce")
print(a.password)
print(a.secret)