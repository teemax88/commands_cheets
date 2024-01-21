import os

"""
- База данных инициализируется размером и не может его превышать.
- Размер базы данных не может быть меньше 1, иначе выбрасывается ValueError
- Каждый новый элемент добавляется в начало базы
- При добавлении элемента в полную базу последний элемент удаляется
- База данных добавляет только положительные числа и не пустые строки
- Размер базы данных можно изменить с потерей данных в начале базы
- Обо всех изменениях база пишет данные в кэш-файл *.cache
"""


class Database:

    def __init__(self, size):
        if size < 1:
            raise ValueError("Database cant be value less than 1")
        self._max_size = size
        self.data = []
        self.cache_name = f"file{id(self)}.cache"
        self.cache = open(self.cache_name, "w")
        self.action_number = 1

    def set_size(self, new_size):
        self._max_size = new_size
        if new_size < self.size:
            to_remove = self.size - new_size
            self.data = self.data[to_remove:]
            self.cache.write(f"{self.action_number} {self.data}\n")
            self.action_number += 1

    def add(self, value):
        if (type(value) == int and value > 0) or (type(value) == str and value):
            self.data.insert(0, value)
            self.data = self.data[:self._max_size]
            self.cache.write(f"{self.action_number} {self.data}\n")
            self.action_number += 1

    @property
    def size(self):
        return len(self.data)

    @property
    def free_size(self):
        return self._max_size - len(self.data)

    def clear(self):
        self.data = []

    def rm_cache(self):
        os.remove(self.cache_name)

    def __del__(self):
        self.cache.close()

    def __repr__(self):
        return str(self.data)


if __name__ == "__main__":
    db = Database(3)
    print(db.cache_name)
