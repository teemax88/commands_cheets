import json

# Парсинг данных из строки
data = '{"key1": 1, "key2": "2", "key3": [1, 2, 3]}'

parsed_data = json.loads(data)

# Данные парсятся согласно типам данных
print(type(parsed_data))    # <class 'dict'>
print(parsed_data['key1'] + 1)  # 2
print(type(parsed_data['key3']))    # <class 'list'>



# Преобразование данных в строку
data_dict = {'key': 1, 1: 'one', 'list': [1, 2, 3]}
parsed_to_string_data = json.dumps(data_dict)

print(parsed_to_string_data)    # {"key": 1, "1": "one", "list": [1, 2, 3]}
print(type(parsed_to_string_data))  # <class 'str'>
