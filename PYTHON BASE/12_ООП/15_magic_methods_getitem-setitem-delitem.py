class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 < item < len(self.values):
            print("__getitem__ call")
            return self.values[item]
        else:
            raise IndexError("Индекс за границей нашей коллекции")

    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            print("__setitem__ call")
            self.values[key] = value
        else:
            raise IndexError("Индекс за границей нашей коллекции")

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            print("__delitem__ call")
            del self.values[key]
        else:
            raise IndexError("Индекс за границей нашей коллекции")


v = Vector(5, 4, 3, 7, 1)
print(v[2])  # __getitem__ call # 3
# print(v[9])    # IndexError: Индекс за границей нашей коллекции

v[0] = 1  # __setitem__ call
print(v.values)  # [1, 4, 3, 7, 1]

del v[0]  # __delitem__ call
print(v.values)  # [4, 3, 7, 1]
