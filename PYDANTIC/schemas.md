
*Установка Pydantic*
```python
pip install pydantic
```

*Импортирование необходимых классов и модулей*
```python
from pydantic import BaseModel
```

*Создание класса BasicModel*
```python
class BasicModel(BaseModel):
    id: int
    name: str
    email: str
```

В этом примере мы создали класс BasicModel, который наследуется от BaseModel. Затем мы определили три поля: id, name и email, каждое из которых имеет свой тип (целое число, строка). Эти поля являются обязательными по умолчанию, но Pydantic позволяет определять различные параметры валидации, такие как допустимые значения, минимальная и максимальная длина и другие.

*Проверка данных:*

Допустим, у нас есть данные, которые мы получили с сервера, и мы хотим проверить их на соответствие схеме BasicModel. Мы можем использовать метод validate:
```python
data = {
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@test_data.com"
}

try:
    validated_data = BasicModel(**data)
    print("Данные валидны:")
    print(validated_data)
except Exception as e:
    print("Ошибка валидации данных:")
    print(e)
```
