## Операции и методы
```python
# Создание словаря
d = {
    'moskva': 495,
    'piter': 812,
    'penza': 8412
}  # {'moskva': 495, 'piter': 812, 'penza': 8412}

r = dict(moskva=495, piter=812, penza=8412)  # # {'moskva': 495, 'piter': 812, 'penza': 8412}
a = [['moskva', 495], ['piter', 812], ['penza', 8412]]
r1 = dict(a)  # {'moskva': 495, 'piter': 812, 'penza': 8412}
q = dict.fromkeys(['a', 'b', 'c'], 100)  # {'a': 100, 'b': 100, 'c': 100}
v = {}  # создаст пустой словарь или v = dict()
```

```python
if 'Kharkov' in d:  # если в словере d есть ключ 'Kharkov' то выведем его на печать
    print(d['Kharkov'])
else:  # если нет то добавим его в словарь
    d['Kharkov'] = 572
print(d)  # {'moskva': 495, 'piter': 812, 'penza': 8412, 'Kharkov': 572}
for key in d:
    print(key, d[key])  # вывод ключ и его значение moskva 495 и т.д.
```

## Методы словаря
```python
d.clear()  # очистит словарь до {}
rez = {}
rez.update(d)  # добавит в список rez данные со списка d
rez = dict(a)  # добавит в список rez данные со списка a (dict() копирует первые элементы словаря в новый словарь,
# а затем выполняет метод update(), чтобы обновить новый словарь вторым элементом словаря
rez2 = {**d, **rez}  # если будет * то добавяться только ключи, ** добавятся ключи и значения в новый словарь
print(d.get('moskva'))  # 495 выведет значение ключа
print(d['moskva'])  # 495 выведет значение ключа (тоже самое)
print(d.get('asd', 'Такого ключа нет'))  # выведет значение ключа (если его нет, то выведет надпись
# можно вывести что угодно вместо 'Такого ключа нет' например 100 или [1, 2, 3]
# a[i] = a.get(i, 0) + 1 добавит ключ [i] в словарь а и при первом назначении добавит значание 1 ,потом +1 к каждому
d.setdefault('Kyiv', 44)  # если ключа нет то добавит его в словарь , если уже есть то ничего не сделает
print(d)  # {'moskva': 495, 'piter': 812, 'penza': 8412, 'Kharkov': 572, 'Kyiv': 44}
print(d.pop('penza'))  # выведет значение ключа 'penza' но удалит его из списка 8412
print(d)  # {'moskva': 495, 'piter': 812, 'Kharkov': 572, 'Kyiv': 44}
print(d.popitem())  # выведет последнее значение ключа и значения но удалит его из списка ('Kyiv', 44)
print(d)  # {'moskva': 495, 'piter': 812, 'Kharkov': 572}
print(d.keys())  # dict_keys(['moskva', 'piter', 'Kharkov']) вывод всех ключей в словаре
print(d.values())  # dict_values([495, 812, 572]) вывод всех значений в словаре
for i in d.values():
    print(i)  # вывод только элементов из списка d (пройти можно его элементы или ключи если d.keys() ) 495 812 572
print(d.items())  # dict_items([('moskva', 495), ('piter', 812), ('Kharkov', 572)]) вывод всех пар
for i in d.items():
    print(i)  # вывод только пар из списка d ('moskva', 495) ('piter', 812) ('Kharkov', 572)
    print(i[0], i[1])  # вывод отдельно элементов из списка d moskva 495  piter 812  Kharkov 572

for key, value in d.items():  # в key будет ключ , в value будет значение со словаря d
    print(key, value)  # moskva 495  piter 812  Kharkov 572
```

```python
d1 = {
    1: 'one',
    'two': 2,
    3: [3, 3, 3],
}
d1[44] = 'forty'  # добавит к словарю d1 ключ 44 и значение в него 'forty'
print(d1)  # {1: 'one', 'two': 2, 3: [3, 3, 3], 44: 'forty'} вывод всего словаря
print(d1['two'])  # 2 выведет только значение ключа
d1[1] = 'один'  # изменит значение ключа 1 на новое 'один'
del d1['two']  # удалит ключ 'two' в словаре d1
print(d1)  # {1: 'один', 3: [3, 3, 3], 44: 'forty'}
```

```python
# ззанесём данные из строки в словарь
s = 'Asmolovskiy Andrey Kharkov HIIT 5 4 5 5 4 3 5'
s = s.split()  # ['Asmolovskiy', 'Andrey', 'Kharkov', 'HIIT', '5', '4', '5', '5', '4', '3', '5']
person = {}
person['Last name'] = s[0]  # внесли в ключ 'Last name' значение из списка s[0] 'Asmolovskiy' и т.д.
person['First name'] = s[1]
person['City'] = s[2]
person['University'] = s[3]
person['marks'] = []  # создали ключ 'mаrks' с пустым списком в значении
for i in s[4:]:  # прошли в цикле от 4го индекса до конца и добавили в список 'marks' значения с s преобразовав их в int
    person['marks'].append(int(i))
print(person)
# {'Last name': 'Asmolovskiy', 'First name': 'Andrey', 'City': 'Kharkov', 'University': 'HIIT', 'marks': [5, 4, 5, 5, 4, 3, 5]}
```


## Сортировка по ключу

```python
# Аргумент key - встроенная функция:

a = [4, -10, 43, -300, 54, 289, -34, -8, 749]
print(sorted(a))  # [-300, -34, -10, -8, 4, 43, 54, 289, 749] стандартная сортировка
print(sorted(a, key=abs))  # [4, -8, -10, -34, 43, 54, 289, -300, 749] сортировка элементов по модулю

b = []  # записал в b отсортированный список а по модулю
for i in range(len(a)):
    b.append(abs(a[i]))
b.sort()
print(b)  # [4, 8, 10, 34, 43, 54, 289, 300, 749]

def last(x):  # функция вернёт последнюю цифру от числа
    return x % 10, x // 10 % 10


# если сделать return -(x % 10), то сортировка в 34-й строке будет по убыванию, сначала выполнит возврат последней цифры
# x % 10 и если результат будет одинаковый, то возврат будет по предпоследней x // 10 % 10

print(sorted(b, key=last))  # [10, 300, 43, 4, 34, 54, 8, 289, 749] сортировка по последней цифре при return x % 10
print(sorted(b, key=last))  # [300, 10, 43, 4, 34, 54, 8, 749, 289]по последн.и предпоследн.return x % 10, x // 10 % 10
```

```python
# Аргумент key - встроенные методы объектов:

f = ['ZZZ', 'aaa', 'eee', 'DDD', 'BBB', 'www']
print(sorted(f))  # ['BBB', 'DDD', 'ZZZ', 'aaa', 'eee', 'www'] сортировка сначала заглавные, потом маленькие
print(sorted(f, key=str.lower))  # ['aaa', 'BBB', 'DDD', 'eee', 'www', 'ZZZ'] перед сравнением все буквы станут мален.
```

```python
# Аргумент key - анонимная функция lambda:

q = ['ZZZ 800', 'aaa 45', 'eee 43', 'DDD 800', 'BBB 43', 'www 14']
print(sorted(q, key=lambda x: int(x.split()[1])))  # ['www 14', 'eee 43', 'BBB 43', 'aaa 45', 'ZZZ 800', 'DDD 800']
# split разобьёт на 'ZZZ' и '79' возьмём[1] т.е. число '79' и представим чтобы сравнить как int
print(sorted(q, key=lambda x: (int(x.split()[1]), x.split()[0].lower())))
# ['www 14', 'BBB 43', 'eee 43', 'aaa 45', 'DDD 800', 'ZZZ 800']
# split разобьёт на 'ZZZ' и '79' возьмём[1] т.е. число '79' и представим чтобы сравнить как int
# затем если по числам они равны, то применим 2-е условие - сравним [0] элементы(слова с мален.)всё должно быть в
# скобках поскольку lambda принимает только один аргумент (мы его представили как кортеж) и lower тоже со скобками

# если (-int(x.split()[1]) , то числа отсортируются по убыванию

# если числа по возрастанию, а буквы по убыванию, то нужно дважды создать сортировку
w = ['ZZZ 800', 'aaa 45', 'eee 43', 'AaA 800', 'BBB 43', 'AAA 14']
w_1 = sorted(w, key=lambda x: (int(x.split()[1])))
print(sorted(w_1, key=lambda x: (x.split()[0].lower()), reverse=True))
# ['ZZZ 800', 'eee 43', 'BBB 43', 'AAA 14', 'aaa 45', 'AaA 800']

print(sorted(q, key=lambda x: (int(x.split()[1]), x.split()[0].lower()), reverse=True))
# ['ZZZ 800', 'DDD 800', 'aaa 45', 'eee 43', 'BBB 43', 'www 14'] сортировка чисел и слов по убыванию
```

## Сортировка словаря
```python
heroes = {
    'Andrey': 38,
    'Kristina': 37,
    'Mother': 60,
    'Artur': 14,
    'Father': 65,
    'Moska': 14,
    'Aleksey': 38
}
# для сортировки словаря(неупорядоченной коллекции) по ключам достаточно обойти его в цикле отсортировав по ключам
for i in sorted(heroes):  # если не указывать, то сортировка по ключу
    print(i, heroes[i])
# Aleksey 38
# Andrey 38
# Artur 14
# Father 65
# Kristina 37
# Moska 14
# Mother 60

# или оставить его в кортеже и отсортивать по чему захочется
for i in sorted(heroes.items(), key=lambda para: (para[1], para[0])):  # сначала по значению,если одинак.то по ключу
    print(*i)
# Artur 14
# Moska 14
# Kristina 37
# Aleksey 38
# Andrey 38
# Mother 60
# Father 65

# Как вариант, по значениям можно отсортировать sorted(heroes, key=heroes.get)

for i in heroes: # выведет ответ по ключам
    print(i) # Andrey Kristina Mother Artur Father
    print(i, heroes[i]) # Andrey 38 Kristina 37 Mother 60 Artur 14 Father 65

for i in sorted(heroes):  # вывод отсортированного списка по ключам (но значения в хаотичном порядке)
    print(i, heroes[i])  # Andrey 38 Artur 14 Father 65 Kristina 37 Mother 60

# сортировка по значениям , ключ lambda в котором будет сначала учитываться значение(para[1]) а потом сортировка по
# ключу (para[0]) , т.е. словарь отсортирует вывод по значениям, если значения совпадают то по ключу
for i in sorted(heroes.items(), key=lambda para: (para[1], para[0])):
    print(i)  # ('Artur', 14) ('Kristina', 37) ('Andrey', 38) ('Mother', 60) ('Father', 65)
```

## Генераторы словарей
```python
# создадим словари через генератор словарей (в нём ключ:значение)
a = {i: i ** 2 for i in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} словарь в котором ключ i и его значение i**2

a1 = {}
for i in range(1, 6):
    a1[i] = i**2  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```python
a1 = {word: len(word) for word in ['hello', 'world', 'www']}  # {'hello': 5, 'world': 5, 'www': 3}
# содзали словарь а1 в котором ключом будет слово со списка, значением его длинна
```

```python
data = {  # сделаем с помощью генератора Имя Фамилия начин.с большой буквы,остальные мален.,значение int
    'джЕфф Безос': '177',
    'Илон МаСк': '126',
    'бернар АрнО': '150',
    'БиЛл ГейтС': '124',
}
data1 = {key.title(): int(value) for key, value in data.items()}  # 'Джефф Безос': 177
# items() возьмёт пары и присвоит key, value ключ и значение, title() сделает первую большую,а остальные маленькие

data2 = {}
for key, value in data.items():
    data2[key.title()] = int(value)
```

```python
# создадим словарь из вложенного списка чтобы можно было обратиться по ключу
users = [
    [0, 'Bob', 'password'],
    [1, 'code', 'python'],
    [2, 'Stack', 'overflow'],
    [51, 'Andrey', '1234']
]
print(users[3])  # [51, 'Andrey', '1234'] а нам нужно найти его по 51 (создадим ключ в словаре)
usersslov = {person[0]: person[1:] for person in
             users}  # создаст словарь с ключом 1-е значение в списке,знач. остальное
print(usersslov)
```