
````text
isinstance - встроенная функция python.
isinstance позволяет проверить какому типу объекта принадлежит значение.
````

*Синтаксис isinstance():*
```python
isinstance(obj, classinfo)
```
```doctest
obj - объект, который нужно проверить.
classinfo - класс или кортеж классов (или типов), которым может принадлежать obj.
```

```python
a = [5, 3, {'Kris': 37}, 'hello', [3, 4], 'world', [5], 10.5, {'Andrey': 38}]  # список из разных типов
for item in a:
    if isinstance(item, int):
        print(f"{item} - это целое число")
    elif isinstance(item, str):
        print(f'"{item}" - это строка')
    elif isinstance(item, float):
        print(f"{item} - это число с плавающей запятой")
    elif isinstance(item, bool):
        print(f"{item} - это логическое значение")
    elif isinstance(item, dict):
        print(f"{item} - это словарь")
    else:
        print(f"{item} - это неизвестный тип данных")
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