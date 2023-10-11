```python
a = 1  # цикл выполняет от а (1) до 5ти и выводяться 1 2 3 4 5
n = int(input())
while a <= n:  # будет считать от a(1) до n
    print(a)
    a = a + 1

# ввод пароля , пока не введёте правильный пароль программа будет его запрашивать
guess = input('ВВедите пароль')  # ввод пароля с клавы
password = 'asdf'
count = 1
while guess != password:  # проверка соответствует ли введённый и сохранённый пароль
    print('Вы ввели некоректный пароль')
    count = count + 1
    guess = input('ВВедите пароль')  # снова попросим ввести пароль
print("Вы потратили ", count, "попыток")

# удалим индекс 2 со списка
a = [1, 2, 3] * 4
print(a)  # список до while [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
while 2 in a:  # пока есть 3 в переменной а
    a.remove(2)  # удалит первую слева 2-ку
print(a)  # список после while [1, 3, 1, 3, 1, 3, 1, 3]

# вывед буквы и последовательно будем удалять по 1й
s = 'asd9GhJKl3'
while len(s) > 0:  # пока переменная > 0
    buk = s[0]
    if buk >= 'a' and buk <= 'z':
        print(buk, 'small')
    if buk >= 'A' and buk <= 'Z':
        print(buk, 'BIG')
    elif buk.isdigit():  # True если в buk цифры,иначе False(дальше не проходит)
        print(buk, 'digit')
    else:
        print(buk, 'Znak')
    s = s[1:]  # в s записывает со 2й по посленее значение

# a+=1 тоже самое что a = a+1
# print(*a) выводит на печать список а


# Остановка цикла с помощью break
count = 0

while True:  # This condition cannot possibly be false
    print(count)
    count += 1
    if count >= 5:
        break           # Exit loop if count >= 5


zoo = ["lion", "tiger", "elephant", "giraffe", "python"]
while True:                         # This condition cannot possibly be false
    animal = zoo.pop()       # Extract one element from the end of the list
    print(animal)
    # Add the condition to exit the loop
        # Exit the loop

print(zoo)
```