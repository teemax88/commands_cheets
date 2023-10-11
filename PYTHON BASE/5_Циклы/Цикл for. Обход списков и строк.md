```python
a = [12, 34, 56, 7, 23]
count = 0
for i in a:  # цикл будет поочерёдно присваивать переменной i значение индекса а
    print(i)  # выведем все элементы списка а поочерёдно
    count += 1
    print(count, 'проход')  # вывод прохода
    input()  # цикл будет продолжиться только после нажатия ENTER

a = [2, 34, 57, 32, 56]
# for i in a:  # обход по значениям
#     print(i, a.index(i)) если встретиться 2 раза одно число то передаст первое(левое)
for i in range(len(a)):  # обход по индексам
    print(i, a[i])  # покажет номер прохода , затем сам элемент списка
    a[i] += 5  # увеличит каждый элемент индекса на 5
print(a)  # [7, 39, 62, 37, 61]

a = [1, 2, 4, 5, 2, 3, 4]  # необходимо удалить дубли
b = []
for i in a:  # обход по значениям
    if not i in b:  # если элемента i нет в b
        b.append(i)  # добавим в b элемент i
print(b)  # распечатаем список без повторов

a = [1, 2, 4, 5, 2, 3, 4]  # необходимо разбить чётный и нечётный список
ch = []
nech = []
for i in a:  # обход по значениям
    if i % 2 == 0:
        ch.append(i)
    else:
        nech.append(i)
print(ch, 'чётный список')
print(nech, 'нечётный список')

a = [1, 2, 4, 5, 2, 3, 4]  # необходимо разбить чётный и нечётный список (список по индексу)
ch = []
nech = []
for i in range(len(a)):  # обход по индексам
    if a[i] % 2 == 0:  # если a[i]й элемент чётный то...
        ch.append(i + 1)  # +1 чтобы запись списка была не с 0 а с 1
    else:
        nech.append(i + 1)
print(ch, 'индекс чётных  в списке')
print(nech, 'индекс нечётных  в списке')

s = 'HeLlo 1&/'  # разобьём строку на буквы с их определением
for i in s:  # обход по значениям
    if i >= 'a' and i <= 'z':
        print(i, "small")
    elif 'A' <= i <= 'Z':
        print(i, 'BIG')
    elif '0' <= i <= '9':
        print(i, "Number")
    else:
        print(i, "Symbol")
vowels = 'aeiouy'  # нужно вывести пары гласных vowels=(a,e,i,o,u,y) если они стоят в паре
s = 'aousddfeiveamui'
n = len(s)
for i in range(n - 1):  # длинна -1 поскольку нужно проверить не до последнего иначе будет ошибка
    if s[i] in vowels and s[i + 1] in vowels:  # если например 0 и 1 индекс равен гласным то дальше их вывод
        print(s[i], s[i + 1])


# Оператор continue
for i in range(5):
    if i == 3:
        continue   # Skip the rest of the code inside loop for current i value
    print(i)

for x in range(10):
    # Add a condition
        # Add a keyword to skip print(x) for this loop
    print(x)
```