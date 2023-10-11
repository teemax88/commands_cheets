```python
# встроенные функции
a = abs(-7)
print(a)  # 7
b = max(4, 6, 8, abs(-13), min(10, 20))
print(b)  # 13 во встроенные функции можем вкладывать внутрь другие функции


def Sqare_old(x):
    print(x ** 2)
    # return None по умоланию если самому ничего не возвращать


a = Sqare_old(5)
print(a)  # выведет 25  None, т.е. вывод 25 будет поскольку в функции он есть,а в результат самой функции запишет None


def Sqare(x):
    return x ** 2


a = Sqare(7)
print(a)  # выведет 49, т.е. 49 запишет в результат самой функции
a = Sqare(Sqare(3))
print(a)  # вывод 81 , сделает сначала 3**2= 9, потом 9**2 = 81


def example():  # напишем чтобы понять что return работает как выход из функции с записью что будет в результате фун-ии
    print(1)
    print(2)
    return 'hello'
    print(3)


example()  # вывод 1 2 , т.е. до команды return
a = example()
print(a)  # вывод 1 2 hello так как в фукции выполниться два вывода, потом запись результата


def even(x):  # функция проверяет на чётность
    if x % 2 == 0:
        return 'Чётное'
    # else:
    #     return 'Нечётное'
    return 'Нечётное'  # сделали тоже самое что в 2-х строках выше
    # return x % 2 == 0 можно сделать только этой строкой и запись в return будет True или False


for i in range(1, 11):
    print(i, even(i))  # выведет значения от 1 до 10-ти и чёт или нечет


# найдём вывод условия сочетания = n1 / k!*(n-k)!
def factorial(x):  # функция определения факториала
    pr = 1
    for i in range(2, x + 1):
        pr = pr * i
    return pr


def sochetanie(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))  # знаменатель в скобках


for i in range(1, 11):  # вывод значения и его факториала от 1 до 10
    print(i, factorial(i))  # вывод 1 1  2 2  3 6  4 24  5 120 6 720 и т.д.

print(sochetanie(5, 3))  # вывод нашей функции 10.0


# функция будет считать площадь и периметр возвращая 2-а значения в кортеже
def Sqare_Perimetr(a, b):
    # mas = [] можно добавить значения в список mas
    # mas.append(a * b)
    # mas.append((a + b) * 2)
    # return mas
    return a * b, (a + b) * 2


print(Sqare_Perimetr(3, 7))  # вывод (21, 20) площади и переметра в формате кортеж
square, perimetr = Sqare_Perimetr(4, 9)  # присвоим в каждую переменную значения с кортежа
print(square, perimetr)  # вывод 36 26

```