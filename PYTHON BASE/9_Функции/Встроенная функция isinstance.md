```python
"""
Функция isinstance
isinstance - встроенная функция python.
isinstance позволяет проверить какому типу объекта принадлежит значение.

"""
a = [5, 3, {'Kris': 37}, 'hello', [3, 4], 'world', [5], 10.5, {'Andrey': 38}]  # список из разных типов
sum_srok = ''
sum_list = []
sum_numbers = 0
sum_dict = {}
for i in a:
    if isinstance(i, str):  # проверит если i строка, то ...
        sum_srok += i
    elif isinstance(i, list):  # если i список, то добавим эти элементы(если оставить вложенность то sum_list.append(i)
        sum_list += i
    elif isinstance(i, (int, float)):  # если i int или float то ...(добавим кортеж в скобках через запятую)
        # elif isinstance(i,int) or isinstance(i,float): # тоже самое что вверху
        sum_numbers += i
    elif isinstance(i, dict):
        for key, value in i.items():
            sum_dict[key] = value
print(sum_srok)  # helloworld вывод строк в переменной а
print(sum_list)  # [3, 4, 5] вывод списков в переменной а
print(sum_numbers)  # 18.5 вывод суммы всех int и float в переменной а
print(sum_dict)  # {'Kris': 37, 'Andrey': 38} вывод итогового словаря в переменной а

```