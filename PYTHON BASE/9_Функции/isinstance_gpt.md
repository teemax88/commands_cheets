```text
Функция isinstance() в Python используется для проверки принадлежности объекта к определенному классу или типу данных. Она возвращает True, если объект принадлежит указанному классу или типу, и False в противном случае. Это полезно при обработке разных типов данных или при валидации входных данных.
```

*Синтаксис isinstance():*
```python
isinstance(obj, classinfo)
```
```doctest
obj - объект, который нужно проверить.
classinfo - класс или кортеж классов (или типов), которым может принадлежать obj.
```

### Примеры использования isinstance():
*Проверка, является ли объект целым числом (int):*
```python
x = 5
if isinstance(x, int):
    print("x - это целое число")
else:
    print("x не является целым числом")
```

*Проверка, принадлежит ли объект определенному классу:*
```python
class Dog:
    pass

dog = Dog()
if isinstance(dog, Dog):
    print("dog - это экземпляр класса Dog")
else:
    print("dog не является экземпляром класса Dog")
```

*Проверка, является ли объект одним из нескольких классов:*
```python
class Cat:
    pass

class Dog:
    pass

pet = Dog()
if isinstance(pet, (Cat, Dog)):
    print("pet - это или экземпляр класса Cat, или экземпляр класса Dog")
else:
    print("pet не является ни Cat, ни Dog")
```

*Проверка типа данных в списке:*
```python
data = [1, "hello", 3.14, True]

for item in data:
    if isinstance(item, int):
        print(f"{item} - это целое число")
    elif isinstance(item, str):
        print(f'"{item}" - это строка')
    elif isinstance(item, float):
        print(f"{item} - это число с плавающей запятой")
    elif isinstance(item, bool):
        print(f"{item} - это логическое значение")
    else:
        print(f"{item} - это неизвестный тип данных")
```