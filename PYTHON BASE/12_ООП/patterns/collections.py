from typing import List, Dict, Tuple


class Foo:
    pass


list_of_foo: List[Foo] = [Foo(), Foo(), Foo(), Foo()]
print(list_of_foo)  # [<__main__.Foo object at 0x0000026CC114CF90>, <__main__.Foo object at 0x0000026CC114CFD0>, ...]

list_of_foo_error: List[Foo] = [1, 2, 3, 4, 5]
print(list_of_foo_error)  # [1, 2, 3, 4, 5]

typed_dict: Dict[str, int] = {"bar": 1}
print(typed_dict)  # {'bar': 1}

typed_dict_error: Dict[str, int] = {1: 1}
print(typed_dict_error)  # {1: 1}

tuple_of_foo: Tuple[Foo, Foo, list] = (Foo(), Foo(), [])
print(tuple_of_foo)  # (<__main__.Foo object at 0x0000026CC114D210>, <__main__.Foo object at 0x0000026CC114D250>, [])
