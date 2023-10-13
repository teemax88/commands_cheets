```python
Set в Python - это неупорядоченная коллекция уникальных элементов. Каждый элемент уникален и должен быть неизменяемым (хэшируемым), что позволяет выполнять различные операции, такие как объединение, пересечение и разность множеств.


```

### Основные методы и функции множества (set) в Python:

```python
add(элемент)
Добавляет элемент в множество.

my_set = {1, 2}
my_set.add(3)

```

```python
clear()
Удаляет все элементы из множества.

my_set.clear()


```

```python
copy()
Возвращает копию множества.

new_set = my_set.copy()

```

```python
difference(множество)
Возвращает разность множеств.

diff_set = my_set.difference(another_set)

```

```python
difference_update(множество)
Удаляет все элементы из множества, которые присутствуют в указанном множестве.

my_set.difference_update(another_set)

```

```python
discard(элемент)
Удаляет указанный элемент из множества, если он присутствует.

my_set.discard(2)

```

```python
intersection(множество)
Возвращает пересечение множеств.

inter_set = my_set.intersection(another_set)

```

```python
intersection_update(множество)
Обновляет множество пересечением.

my_set.intersection_update(another_set)

```

```python
isdisjoint(множество)
Возвращает True, если множества не имеют общих элементов.

is_disjoint = my_set.isdisjoint(another_set)

```

```python
issubset(множество)
Проверяет, является ли множество подмножеством другого множества.

is_subset = my_set.issubset(another_set)

```

```python
issuperset(множество)
Проверяет, является ли множество надмножеством другого множества.

is_superset = my_set.issuperset(another_set)

```

```python
pop()
Удаляет и возвращает случайный элемент множества.

elem = my_set.pop()

```

```python
remove(элемент)
Удаляет указанный элемент из множества.

my_set.remove(2)

```

```python
symmetric_difference(множество)
Возвращает симметричную разность множеств.

sym_diff = my_set.symmetric_difference(another_set)

```

```python
symmetric_difference_update(множество)
Обновляет множество симметричной разностью.

my_set.symmetric_difference_update(another_set)

```

```python
union(множество)
Возвращает объединение множеств.

uni_set = my_set.union(another_set)

```

```python
update(множество)
Обновляет множество, добавляя элементы из другого множества.

my_set.update(another_set)

```