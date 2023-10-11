```python
# В данном уроке мы поговорим о JSON (JavaScript Object Notation) - текстовом формате обмена данными.
# JSON популярный формат предназначенный для обмена данными между сервером и клиентов либо сервером и другими серверами
# JSON хранит данные в структурированном виде, походим на словарь.
# В Python есть стандартный модуль по работе с json. Название модуля - json
# Для импортирования модулей применяются инструкции import и import from.
# Собственные модули импортируются как и стандартные модули python.
# Всего-то надо написать инструкцию import И указать название модуля
# load - когда мы считываем файл JSON
# loads - когда мы считываем строку в формате JSON
# dump - создаёт файл
# dumps - создаёт строку в виде JSON

import json
from random import randint

str_json = """
{
"response": {
    "count": 5961878,
    "items": [{
        "first_name": "Елизавета",
        "id": 620471795,
        "last_name": "Сопова"
    },{
        "first_name": "Роман",
        "id": 614752515,
        "last_name": "Малышев"
}]
}
}"""

data = json.loads(str_json)  # присвоили в переменную data уже словарь str_json
# print(type(data)) # <class 'dict'>
# print(data["response"]) # вывели все значения ключа response(в нём есть 2-а ключа)

# print(data["response"]['count']) # вывели 5961878

# print(data["response"]['items']) # вывели [{'first_name': 'Елизавета', 'id': 620471795, 'last_name': 'Сопова'},
# # {'first_name': 'Роман', 'id': 614752515, 'last_name': 'Малышев'}] и поскол. items это список пройдём по нему циклом

for item in data["response"]['items']:  # вывод в виде словаря
    # print(item) # {'first_name': 'Елизавета', 'id': 620471795, 'last_name': 'Сопова'}
    #             # {'first_name': 'Роман', 'id': 614752515, 'last_name': 'Малышев'}

    # print(item['first_name'], item['last_name']) # Елизавета Сопова  вывод нужных нам ключей
    #                                              # Роман Малышев

    del item['id']  # удалит ненужный нам ключ
    item['likes'] = randint(100, 200)  # создали новый ключ с рандомным значением от 100 до 200
    item['date'] = datetime.now().strftime(
        '%d.%m.%y')  # создали ключ с датой, strftime('%d.%m.%y') для понимания в json

# print(data['response']['items'])  # вывод нового словаря
# [{'first_name': 'Елизавета', 'last_name': 'Сопова', 'likes': 174, "date": "22.04.22"},
## {'first_name': 'Роман', 'last_name': 'Малышев', 'likes': 183, "date": "22.04.22"}]

# new_json = json.dumps(data, indent=3, ensure_ascii=False)  # создали переменную new_json(формат json) .
# # indent - кол-во отступов для комфортного просмотра , ensure_ascii=False - для того чтобы русские буквы читались
# print(new_json)

# для того чтобы из нашего словаря data создать новый файл воспользуемся инструкцией ниже
with open('../Уроки/my.json', 'w') as file:  # создали файл my.json с параметром запись (откроем в качестве имени file)
    json.dump(data, file, indent=3, ensure_ascii=False)
    # первый параметр объект с кого мы будем записывать, второй во что будем записывать, indent, ensure выше пояснение

# для загрузки данных из файла в переменную new_data
with open("../Уроки/my.json", 'r') as file:  # откроем файл с параметром чтение как file
    new_data = json.load(file)  # запишем в переменную new_data данные с файла my.json

print(new_data)  # выведет вновь полученную переменную new_data

```