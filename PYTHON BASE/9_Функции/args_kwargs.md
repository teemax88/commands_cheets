```python
# * может использоваться в присвоении переменных (если * есть, то будет присвоен список из значений)

a, b, c = 5, 8, 'asd'
print((a, b, c))    # (5, 8, 'asd')

a, b, c = [12, True, 'dfg']
print((a, b, c))    # (12, True, 'dfg')

a, b, c = [True, 7, 12, 2.23, 'wer', 3]
print((a, b, c))  # ошибка поскольку переменных 3, а значений 6

a, *b, c = [True, 7, 12, 2.23, 'wer', 3]
print((a, b, c))    # (True, [7, 12, 2.23, 'wer'], 3)

a, b, *c = [True, 7, 12, 2.23, 'wer', 3]
print((a, b, c))    # (True, 7, [12, 2.23, 'wer', 3])

*a, b, c = (5, 8)
print((a, b, c))    # ([], 5, 8) в а запись пустого списка

# * помогает распаковать списки, кортежи и т.д.
w = [1, 2, 45]
print(*w)  # 1 2 45 распаковал список при выводе

s = [4, 10]
print(list(range(1, 5)))  # [1, 2, 3, 4] вывод списка от 1го до 4-х

print(list(range(s))) # TypeError поскольку программа не может распаковать наш список s и подставить значения
print(list(range(*s)))  # [4, 5, 6, 7, 8, 9] вывод списка от 4-х до 9-ти
```

````python
def fun(a, b, c, d):
    print(a, b, c, d)

fun(1, 2, 3, 4)  # 1 2 3 4
a = ('asd', True, 78, [3, 4, 5])
# fun(a) # ТypeError поскольку программа не может распаковать наш кортеж а и подставить значения
fun(*a)  # asd True 78 [3, 4, 5]
````

````python
# * в функции поможет из полученных элементов создать кортеж tuple (*args)

def cort(*args):
    print(args, type(args))
    # посчитает сумму кортежа
    s = 0
    for i in args:
        s += i
    return s

cort(1, 34, 5, 7, 89)  # (1, 34, 5, 7, 89) <class 'tuple'>
print(cort(1, 34, 5, 7, 89))  # 136 сумма кортежа
````

````python
# ** в функции поможет из полученных элементов создать словарь (**kwargs)

def dict_1(**kwargs):
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

dict_1(a=23, b=12)  # {'a': 23, 'b': 12} <class 'dict'> создаст словарь и потом выведет а 23  b 12
````

### Пример использования

````python
def random_dialogue(place, *args, **kwargs):
    print("-- Do you know how to get to the", place, "?")
    print("-- I'm sorry, I am not from here, no idea about the", place)
    for arg in args:
        print(arg)
    print("-" * 40)
    for kw in kwargs:
        print(kw, ":", kwargs[kw])
    print('\n')

random_dialogue("Library", "Do you at least have a cigar, sir?",  # Call 1
                "Sure, help yourself.",
                lost_person="old banker",
                other_guy="street clown",
                scene="in a park")

dic = {"lost_person": "old banker", "other_guy": "street_clown", "scene": "in a park"}
lst = ["Do you at least have a cigar, sir?", "Sure, help yourself."]
random_dialogue("Library", *lst, **dic)  # Call 2 - the exact same output
````

````python
def cat(food, *args, state='still hungry', action='meow', breed='Siamese'):
    print(f"-- This cat would {action}", end=' ')
    print(f"if you gave it {food}")
    print(f"-- Lovely fur, the {breed}")
    print(f"-- It's {state}!")
    for arg in args:
        print(arg.upper())

# Add a list of phrases that will be capitalized.
phrases = # Declare the phrases following the output, like in the task description
# Add a dict of keyword arguments.
keywords = # Declare the keywords to insert into the narrative. The keys should match the named arguments of the cat()
# Call the cat() function like in example above to print the required output.
# invoke cat with some food, phrases and keywords
````