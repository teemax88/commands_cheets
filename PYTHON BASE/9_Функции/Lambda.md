```python
# lambda аргумент1, аргумент2,... : выражение
# Lambda функции называют анонимными функциями или функциями без имени.

r = lambda x: x ** 2  # функция возводит х в квадр
print(r(7))  # 49
```

```python
# найдем периметр
z = lambda x, x1, x2: x + x1 + x2
print(z(2, 3, 5))  # 10
```

```python
w = lambda: 'Hello'  # функция выведет надпись без аргументов на входе
print(w())  # Hello
```

```python
s = lambda x: 'Positive' if x > 0 else 'Negative'
print(s(-2))  # Negative
```

*Анонимные функции могут использоваться внутри других функций, таких как map, filter, и sorted.
 Например, используем lambda для сортировки списка строк по их длине:*
```python
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Вывод: ['date', 'apple', 'banana', 'cherry']
```

```python
# отсортируем наш список по заданным параметрам в key
a = [12, 346346, 22, 80, 133, 567, 123, 56]
a.sort(key=lambda x: x % 10)  # ключом будет функция lambda которая запишет в результат последнюю цифру
print(a)  # [80, 12, 22, 133, 123, 346346, 56, 567] сортировка по последней цифре

b = [12, 346346, 22, 80, 133, 567, 123, 56]
b.sort(key=lambda x: x // 10 % 10)  # ключом будет функция lambda которая запишет в результат предпоследнюю цифру
print(b)  # [12, 22, 123, 133, 346346, 56, 567, 80]
```

```python
# напишем функцию которая считает линейное уравнение y = k*x + b
def linear(k, b):
    return lambda x: k * x + b  # вернёт результат, но будет ждать x для решения

grafic1 = linear(2, 5)
print(grafic1(3))  # 11 (посчитает подставив вместо x = 3)
grafic2 = linear(-3, 16)
print(grafic2(5))  # 1 (посчитает подставив вместо x = 5)
```

```python
# функция узнает начинается ли наша строка с W
starts_with = lambda x: True if x[0] == 'W' else False
print(starts_with('Pas'))  # False
```

*Анонимные функции также могут быть переданы в качестве аргументов для более сложных операций.
 Например, при использовании map для умножения каждого элемента списка на 2:*
```python
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  # Вывод: [2, 4, 6, 8, 10]
```

*Анонимные функции могут также использоваться для создания более сложных условий в filter.
 Например, фильтрация списка, чтобы оставить только четные числа:*
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Вывод: [2, 4, 6, 8, 10]
```