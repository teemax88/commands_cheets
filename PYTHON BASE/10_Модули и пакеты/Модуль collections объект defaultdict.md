```python
"""
defaultdict позволяет создавать словарь с дефолтными значениями у ключей
"""
from collections import defaultdict

r = defaultdict(int)
r['s']  # создал ключ, defaultdict создал к нему значение по умолчанию(0 поскольку int)
print(r)  # defaultdict(<class 'int'>, {'s': 0})
r.default_factory = lambda: 12  # создаст то что будет добавляться по умолчанию(через lambda)
r['qwe']
print(r)  # defaultdict(<function <lambda> at 0x0000027BF55FFD00>, {'s': 0, 'qwe': 12})

q = defaultdict(list)
q['asd']  # создал ключ, defaultdict создал к нему значение по умолчанию([] поскольку list)
print(q)  # defaultdict(<class 'list'>, {'asd': []})
q.default_factory = lambda: [1, 2, 3]  # создаст то что будет добавляться по умолчанию(через lambda)
q['ANDREY']
q[4]
print(q)  # defaultdict(<function <lambda> at 0x00000253DA9B3E20>, {'asd': [], 'ANDREY': [1, 2, 3], 4: [1, 2, 3]})

# создали словарь в который добавили в качестве ключа имя, и сложили все оценки которые он получил
data = [
    ('ivanov', 2),
    ('petrov', 3),
    ('sidirof', 5),
    ('ivanov', 5),
    ('ivanov', 2),
    ('petrov', 4),
    ('petrov', 1),
    ('sidirof', 4)
]
marks = defaultdict(int)  # создали переменную в которую будем добавлять (все оценки складывая)
marks_list = defaultdict(list)  # создали переменную в которую будем добавлять (все оценки в список)
marks_qnic = defaultdict(set)  # создали переменную в которую будем добавлять (уникальные оценки в множество)

for surname, mark in data:  # разложили кортеж на фамилию и оценку
    marks[surname] += mark  # добавили в marks в качестве ключа имя, и сложили все оценки которые он получил
    marks_list[surname].append(mark)  # добавили в mars_list с ключом surname его оценку в список
    marks_qnic[surname].add(mark)  # добавили в mars_qnic с ключом surname уникальные оценки в множество
print(marks)  # defaultdict(<class 'int'>, {'ivanov': 9, 'petrov': 8, 'sidirof': 9})
print(marks_list)  # defaultdict(<class 'list'>, {'ivanov': [2, 5, 2], 'petrov': [3, 4, 1], 'sidirof': [5, 4]})
print(marks_qnic)  # defaultdict(<class 'set'>, {'ivanov': {2, 5}, 'petrov': {1, 3, 4}, 'sidirof': {4, 5}})

```