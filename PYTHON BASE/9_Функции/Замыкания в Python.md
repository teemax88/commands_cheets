```python
# В данном уроке поговорим о том, что такое замыкания (closures)
# Для создания замыкания нам понадобиться создать вложенную функцию, которая будет использовать переменную,
# объявленную за ее пределами
# если Return нет в функции, то по умолчанию return = None

def main_func():
    def in_function():
        print('Печать со встроенной функции in_function ')

    in_function()


main_func()  # Печать со встроенной функции in_function


def main_func1(name):
    # name = 'Андрей'
    def in_function():
        print('Привет мой друг', name)  # использовали замыкание (переменную name не внутри функции)

    return in_function


b = main_func1('Andrey')  # в переменную b присвоили результат функции (b стала функцией)
b()  # Привет мой друг Андрей или Привет мой друг Andrey (если нет 17-й строки)


# вложенная функция которая прибавляет значения с 2-х переменных
def adder(value):
    def inner(invalue):
        print(value + invalue)

    return inner


r = adder(3)  # в переменную(функцию) r записали value=3
r(5)  # 8 ответ поскольку invalue=5 подставили в функцию adder
r(2)  # 5 ответ поскольку invalue=2 подставили в функцию adder
z = adder(12)
z(7)  # 19 ответ поскольку invalue=7 подставили в функцию adder
z(3)  # 15 ответ поскольку invalue=3 подставили в функцию adder


# функция счётчик (сколько раз вызывалась эта функция)
def counter():
    count = 0

    def incounter():
        nonlocal count  # покажет что пользоваться нужно переменной в 46-й строке и изменять её
        count += 1
        return count

    return incounter


w = counter()
print(w())  # вызов 1 раз
print(w())  # вызов 2 раза
y = counter()  # при присвоении в новую переменную счётчик сброситься
print(y())  # вызов 1 раз

```

```python
# В данном уроке поговорим о том, что такое замыкания (closures)
# Для создания замыкания нам понадобиться создать вложенную функцию, которая будет использовать переменную,
# объявленную за ее пределами

# функция будет считать среднее-арифметическое
def sr_arifm():
    sp_numbers = []  # создали пустой список в который будем добавлять числа

    def num(number):
        sp_numbers.append(number)
        print(sp_numbers)
        return sum(sp_numbers) / len(sp_numbers)

    return num


a = sr_arifm()
print(a(3))  # [3] 3.0
print(a(12))  # [3, 12] 7.5
# если вызовем функцию sr_arifm() ещё раз то будет опять новый список
b = sr_arifm()
print(b(34))  # [34]  34.0


# можно написать такую же функцию, но брать мы будем переменные а не список
# функция будет считать среднее-арифметическое
def sr_arifm1():
    summa = 0
    count = 0

    def num1(number1):
        nonlocal summa, count  # если не поставить, то переменные не смогут записывать во внешние области
        summa += number1
        count += 1
        return summa / count

    return num1


q1 = sr_arifm1()
print(q1(23))  # 23.0
print(q1(4))  # 13.5

# напишем функцию которая будет считать сколько времени прошло между вызовами функции
from datetime import datetime  # показывает текущее время


def data():
    start = datetime.now()

    def timer():
        return datetime.now() - start

    return timer


e = data()
e()  # в консоли datetime.timedelta(seconds=18, microseconds=389034) разница между вызовом в первый раз и е()


# подставим в значения функции 1-ю функцию и веведем текст который будет считать сколько раз мы её вызвали
def plus(a, b):
    return a + b


def umnogenie(a, b, c):
    return a * b * c


def counter(value):
    count = 0

    def inner(*args, **kwargs):  # можно только *args поскольку нам поступали только кортежи
        nonlocal count
        count += 1
        print(f"Функция {value.__name__} вызывалась {count} раз")  # .__name__ нужно чтобы вывести название функции
        return value(*args, **kwargs  # можно только *args поскольку нам поступали только кортежи

    return inner


t = counter(plus)
print(t(12, 5))  # Функция plus вызывалась 1 раз  17 (12 и 5 подставяться вместо a,b)
u = counter(umnogenie)
print(u(3, 5, 7))  # Функция umnogenie вызывалась 1 раз 105 (3, 5 , 7 подставяться вместо a,b,c)

```