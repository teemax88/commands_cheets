
```python
# Функция all проверяет, все ли указанные элементы внутри коллекции принимают значение «истина».
# Функция any проверяет, есть ли среди указанных элементов коллекции хотя бы один, принимающий значение «истина».

a = ['asd', 3, (1, 2, 3)]
b = ['', 23, 'gello']
c = ['', 0, ()]

print(all(a))  # True (все значения не пустые)
print(all(b))  # False (хоть одно значение пустое, значит False)
print(all(c))  # False (хоть одно значение пустое, значит False)

print(any(a))  # True (хоть одно значение не пустое)
print(any(b))  # True (хоть одно значение не пустое)
print(any(c))  # False (нет ни одного не пустого значения)

d = 9
condition_1 = d % 2 == 0
condition_2 = d > 5
condition_3 = d ** 2 < 1000
# при передаче нескольких переменных нужно их взять в []список или в ()кортеж, поскольку all и any проверяет множество
print(all([condition_1, condition_2, condition_3]))  # False
print(any((condition_1, condition_2, condition_3)))  # True
print(condition_1, condition_2, condition_3)  # False True True

numbers = [2, 4, 6, 8, 10]
result = all(x % 2 == 0 for x in numbers)  # True, так как все числа четные

numbers = [1, 3, 5, 6, 7]
result = any(x % 2 == 0 for x in numbers)  # # Выведет True, так как есть хотя бы одно четное число (6)
```