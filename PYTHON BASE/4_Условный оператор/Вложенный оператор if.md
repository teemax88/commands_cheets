```python
a = 35  # в программе очень важны отступы , тогда видно к какому блоку относится if и else и как работает программа
if a % 5 == 0:
    if a > 9 and a < 100:
        print(1)
    else:
        print(2)
else:
    if a % 2 == 0:
        print(3)
    else:
        print(4)
print('END')

a, b, c = int(input()), int(input()), int(input())  # программа находит минимальное из 3-х чисел
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)

x, y = int(input()), int(input())  # введём 2 координаты точки и поймём в какой четверти она находится
if x > 0:  # тогда это 1я или 4я четверть
    if y > 0:  # тогда это 1я четверть
        print(1)
    else:
        print(4)
else:  # тогда это 2я или 3я четверть
    if y > 0:
        print(2)  # тогда это 2я
    else:
        print(3)  # тогда это 3я

a = int(input())  # программа проверяет какой остаток от деления на 4
if a % 4 == 0:
    print(0)
else:
    if a % 4 == 1:
        print(1)
    else:
        if a % 4 == 2:
            print(2)
        else:
            print(3)

```