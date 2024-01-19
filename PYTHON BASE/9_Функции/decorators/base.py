# Функция с переменным количеством аргументов

def foo_with_args(*args, **kwargs):
    print(args)
    print(kwargs)
    return "--------------"


print(foo_with_args())
# ()
# {}

print(foo_with_args(1, 2, "Booo", {}))
# (1, 2, 'Booo', {})
# {}

print(foo_with_args(one=1, two=2, string="Booo", dicctionary={}))
# ()
# {'one': 1, 'two': 2, 'string': 'Booo', 'dicctionary': {}}

print(foo_with_args(1, 2, "Booo", {}, one=1, two=2, string="Booo", dicctionary={}))
# (1, 2, 'Booo', {})
# {'one': 1, 'two': 2, 'string': 'Booo', 'dicctionary': {}}

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""


# Функция как переменная
def make_hello(name: str):
    return f'Hello, {name}'


# Записали функцию в переменную
some_variable = make_hello

# Вызвали функцию из переменной
print(some_variable('Vasiliy'))  # Hello, Vasiliy

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""


# Функция внутри функции

def cool_hello(name: str):
    def make_hello(some_name):
        return f'Hello, {some_name}'

    return f"[ * ===> {make_hello(name)} <=== * ]"


# Смотрим что получилось
print(cool_hello('Vasiliy'))  # [ * ===> Hello, Vasiliy <=== * ]

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""


# Функция как параметр

def make_hello(name: str):
    return f'Hello, {name}'


def make_bye_bye(name: str):
    return f'Bye Bye, {name}'


# Делаем функцию, которая вызывает внутри себя функцию
def vasiliy_passer(func):
    name = "Vasiliy"
    return func(name)


print(vasiliy_passer(make_hello))  # Hello, Vasiliy
# вместо func внутри vasiliy_passer встает функция make_hello.
# И далее где return возвращается результат функции make_hello с переданным именем

print(vasiliy_passer(make_bye_bye))  # Bye Bye, Vasiliy
# по такой же аналогии, но только возвращается результат функции make_bye_bye

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""


# Функция возвращает функцию

def function_return_function():
    def inner_function():
        print("Hi, I'm inner function!")

    return inner_function


# Сохраняем функцию в переменную
some_variable = function_return_function()

some_variable()  # Hi, I'm inner function!

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""


# Замыкание

def comp_great_function(name):
    def inner_function():
        return f"Hello, {name}"

    return inner_function


great_vasiliy = comp_great_function("Vasiliy")

print(great_vasiliy())  # Hello, Vasiliy

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""


# Базовый декоратор

def hello_function(name):
    return f"Hello, {name}"


def make_cool(func):
    def wrapper(name):
        return f"[ * ==> {func(name).replace('Hello', 'Hey')} <== *]"

    return wrapper


cool_hello = make_cool(hello_function)

print(hello_function("Vasiliy!"))  # Hello, Vasiliy!
print(cool_hello("Vasiliy"))  # [ * ==> Hey, Vasiliy <== *]
# func становится hello_function, а ей нужно передать имя. Это имя передается при вызове
# make_cool содержит результат вызова hello_function, то есть Hello, Vasiliy!
# А уже wrapper принимает значение Hello, Vasiliy! в качестве аргумента
# И далее внутри себя меняет слово Hello на слово Hey
# По итогу return wrapper возвращает измененное значение Hey, Vasiliy

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

# Синтаксический сахар для декораторов

def make_cool(func):
    print("i'm make_cool")

    def wrapper(name):
        print("i'm wrapper")
        return f"[ * ==> {func(name).replace('Hello', 'Hey')} <== *]"

    return wrapper


@make_cool
def hello_function(name):
    print("i'm hello_function")
    return f"Hello, {name}"


print(hello_function("Vasiliy!"))  # [ * ==> Hey, Vasiliy! <== *]
# тут все происходит аналогично верхнему примеру, но вместо того чтобы записывать функцию в переменную и затем ее вызывать,
# мы вешаем декоратор @make_cool над основной функцией
# Очереденость выполнения:
# 1. make_cool()
# 2. wrapper()
# 3. hello_function()

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

# Мульти декораторы

def add_brackets(func):
    def wrapper(name):
        print("i'm add_brackets")
        return f"[ {func(name)} ]"

    return wrapper


def add_arrows(func):
    def wrapper(name):
        print("i'm add_arrows")
        return f" ==> {func(name)} <== "

    return wrapper


def add_stars(func):
    def wrapper(name):
        print("i'm add_stars")
        return f" * {func(name)} * "

    return wrapper


def make_hawaii(func):
    def wrapper(name):
        print("i'm make_hawaii")
        return f"{func(name).replace('Hello', 'Aloha')}"

    return wrapper


@make_hawaii
@add_stars
@add_arrows
@add_brackets
def hello_function(name):
    print("i'm hello_function")
    return f"Hello, {name}"


print(hello_function("Vasiliy"))  # *  ==> [ Aloha, Vasiliy ] <==  *

# Очереденость выполнения:
# i'm make_hawaii
# i'm add_stars
# i'm add_arrows
# i'm add_brackets
# i'm hello_function

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

# Параметры декораторов
def localization(region):
    if region == "Italy":
        ln_hello = "Ciao"
    elif region == "Russia":
        ln_hello = "Privet"
    elif region == "Hawaii":
        ln_hello = "Aloha"
    else:
        raise Exception("Region is not supported!")

    def decorator(func):
        def wrapper(name):
            return f"{func(name).replace('Hello', ln_hello)}"

        return wrapper

    return decorator


@localization("Italy")
def hello_function(name):
    return f"Hello, {name}"


print(hello_function("Vasiliy"))  # Ciao, Vasiliy


@localization("Russia")  # Privet, Vasiliy
def hello_function(name):
    return f"Hello, {name}"


print(hello_function("Vasiliy"))


@localization("Hawaii")  # Aloha, Vasiliy
def hello_function(name):
    return f"Hello, {name}"


print(hello_function("Vasiliy"))

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

# Второй пример, почти как в pytest

def numbers(*args, **kwargs):
    def decorator(func):
        for item in args:
            func(item)
        # for key, value in enumerate(kwargs):
        #     print(key, value)

    return decorator


@numbers(1, 2, 3, 4, 5, 6, 7)
def equality_test(n, target=3):
    try:
        assert n > target
        print(f"Correct: {n} is greater than {target}")
    except AssertionError:
        print(f"Wrong: {n} is less than {target}")

# Вывод:
# Wrong: 1 is less than 3
# Wrong: 2 is less than 3
# Wrong: 3 is less than 3
# Correct: 4 is greater than 3
# Correct: 5 is greater than 3
# Correct: 6 is greater than 3
# Correct: 7 is greater than 3

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
