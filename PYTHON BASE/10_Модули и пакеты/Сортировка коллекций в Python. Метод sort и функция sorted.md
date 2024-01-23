```python
"""
Методы sort - метод списков и sorted - встроенная функция(всегда возвратит список)
"""
a = [4, 12, -7, 500, -34]  # список list
b = 'hello world'  # строка str
c = ('hi', 'zero', 'abracadabra', 'pikachu')  # кортеж tuple
a.sort()
print(a)  # [-34, -7, 4, 12, 500] вывод отсортированного списка(метод подходит только к спискам)

# sorted(a,key=function , reverse=True/False ) с такими параматрами можно вызвать функцию
# sorted не изменяет последовательность а только покажет результат, если нужно сохранить изменнённую последовательность
# то нужно сделать например a = sorted(a). Эта функция подойдёт ко всем итерабельным последовательностям
print(sorted(a))  # [-34, -7, 4, 12, 500]
print(sorted(b))  # [' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
print(sorted(c))  # ['abracadabra', 'hi', 'pikachu', 'zero'] отсортирует по возрастанию (reverse=False (по умолчанию)
print(sorted(c, reverse=True))  # ['zero', 'pikachu', 'hi', 'abracadabra'] отсортирует по убыванию (reverse=True)
print(c)  # ('hi', 'zero', 'abracadabra', 'pikachu')

```