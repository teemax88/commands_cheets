"""
Полезные ссылки:
https://www.tutorialsteacher.com/python/magic-methods-in-python
https://rszalski.github.io/magicmethods/
https://habr.com/ru/post/186608/
"""

import time
import sys

## Методы __init__, __del__, __call__
class Bomb:

    def __init__(self, time: int):
        self.timer = time
        print(f"The bomb is inited with: {self.timer}")

    def __call__(self):
        print("Timer is activated!")
        for _ in range(1, self.timer):
            time.sleep(1)
            self.timer = self.timer - 1
            print(self.timer)
        self.detonate()

    def detonate(self):
        print("BABAXXX!!!")

    def __del__(self):
        print("The bomb is utilized!")

## Методы __str__, __repr__
class Beauty:

    def __str__(self):
        return "I'm Beauty!"

    def __repr__(self):
        return "*Beauty*"

# beauty = Beauty()
# beauty2 = Beauty()
# beauty3 = Beauty()
# print(beauty)
# print([beauty, beauty2, beauty3])


## Просто для примера, не делайте так __dir__, __sizeof__
class Fake(object):

    def __sizeof__(self):
        return 999999

    def __dir__(self):
        return ['what', 'where', 'when']

# f = Fake()
# print(sys.getsizeof(f))
# print(dir(f))
