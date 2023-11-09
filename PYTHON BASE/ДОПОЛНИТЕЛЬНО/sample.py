""" Вложенные циклы и вложенные генераторы списков """

# a = [(i, j) for i in range(3) for j in range(4)]
# # [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
# print(a)
#
# # С условием
# a = [(i, j) for i in range(3) if i % 3 == 0 for j in range(4) if j % 2 == 0]
# # [(0, 0), (0, 2)]
# print(a)
#
# # Преобразовать двумерный список в одномерный
# matrix = [[0, 1, 2, 3],
#           [10, 11, 12, 13],
#           [20, 21, 22, 23]]
#
# a = [x for row in matrix for x in row]
# # [0, 1, 2, 3, 10, 11, 12, 13, 20, 21, 22, 23]
# print(a)


"""Вложенные генераторы списков"""
# M, N = 3, 4
# matrix = [[a for a in range(M)] for b in range(N)]
# # [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
# # Сначала идет внешний цикл N (то есть 4 раза), потом внутренний M (то есть элементы 0, 1, 2)
# print(matrix)

# lst = ['+7', '+6', '+2', '+5']
#
# d = dict.fromkeys(lst)
# print(d)    # {'+7': None, '+6': None, '+2': None, '+5': None}
#
# d = dict.fromkeys(lst, 'код страны')
# print(d)    # {'+7': 'код страны', '+6': 'код страны', '+2': 'код страны', '+5': 'код страны'}
#
# d.clear()
# print(d)    # {}

# lst = '8 11 -4 5 2 11 4 8'.split()
# s = [i for i in dict.fromkeys(lst)]
# print(*s)   # 8 11 -4 5 2 4


""" Кортежи """
# x, y = (1, 2)  # x=1, y=2 Распаковали кортеж и присвоили каждой переменной свое значение

""" Функции """

# x, y, z = 5, 7, 10


# def get_max(a, b):
#     return a if a > b else b
#
#
# m = get_max(x, get_max(y, z))
# print(m)


# # Декораторы
# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("-----Что-то делаем до вызова функции------")
#         res = func(*args, **kwargs)
#         print("-----Что-то делаем после вызова функции------")
#         return res
#
#     return wrapper
#
#
# def some_func(title, tag):
#     print(f"title = {title}, tag = {tag}")
#     return f"<{tag}>{title}</{tag}>"
#
#
# some_func = func_decorator(some_func)
# st = some_func("Python", "h1")
# print(st)

# -----Что-то делаем до вызова функции------
# title = Python, tag = h1
# -----Что-то делаем после вызова функции------
# <h1>Python</h1>


import requests

# base_url = "https://dev-rest.qform.io/ru/v3"
base_url = "https://uapi.qform.io/api"
endpoint = "/leads/get"
payload = {"per-page": "10"}
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2OTkzMzkyMDEsImV4cCI6MjAxNDY5OTIwMSwic3ViIjoicmVkbGluZTE1MDEiLCJhdXRoIjoiUk9MRV9BRE1JTiJ9.PU7bqazAMC5RLo7CSrVT8g-DIf0vaHasAor_AxqJA6Y",
    "Content-Type": "application/json; charset=UTF-8"
}

response = requests.get(base_url + endpoint, params=payload, headers=headers)
result = response.json()

print("--------Список всех заявок на одной странице---------")
print(result)
print("---------------------------------------------")

print(f"Данные по 1-й заявке --- {result['_embedded']['leadDataDTOList'][0]['fields']}")
print(f"Итого заявок пришло в ответе ---- {len(result['_embedded']['leadDataDTOList'])}")

import time
import datetime

d = datetime.date(2023, 7, 8)
unixtime = int(time.mktime(d.timetuple()))
print(unixtime)
