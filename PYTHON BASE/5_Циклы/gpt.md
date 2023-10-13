```python
Цикл For:
Цикл for используется для итерации по последовательности (список, кортеж, строка) или другим объектам итерации.

for i in range(5):
    print(i)

```

```python
Цикл While:
Цикл while повторяет блок кода, пока условие цикла истинно.

i = 0
while i < 5:
    print(i)
    i += 1

```

```python
Вложенные циклы:
Цикл внутри другого цикла называется вложенным циклом.

for i in range(3):
    for j in range(3):
        print(i, j)

```

```python

Метод подсчета:
Метод подсчета используется для подсчета количества вхождений каждого элемента в список.

numbers = [1, 2, 3, 2, 1, 3, 2]
count = [0] * (max(numbers) + 1)

for num in numbers:
    count[num] += 1

print(count)

```

```python
Сортировка подсчетом:
Сортировка подсчетом подходит для сортировки целых чисел из определенного диапазона.

Сортировка подсчетом:
Сортировка подсчетом подходит для сортировки целых чисел из определенного диапазона.

def counting_sort(array):
    count = [0] * (max(array) + 1)
    for num in array:
        count[num] += 1
    
    sorted_array = []
    for i, cnt in enumerate(count):
        sorted_array.extend([i] * cnt)
    
    return sorted_array

array = [4, 2, 2, 8, 3, 3, 1]
sorted_array = counting_sort(array)
print(sorted_array)

```

```python
Обход всех цифр числа:
Мы можем обойти все цифры числа, используя цикл и операции деления и взятия остатка.

number = 12345
while number > 0:
    digit = number % 10
    print(digit)
    number = number // 10

```

```python

Построение матрицы из цифр с помощью циклов:
Мы можем использовать вложенные циклы для создания матрицы.

rows = 3
cols = 3

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * j)
    matrix.append(row)

for row in matrix:
    print(row)

```
