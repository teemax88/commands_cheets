```python
class countdown(object):
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return countdown_iter(self.start)

class countdown_iter(object):
    def __init__(self, count):
        self.count = count

    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r

c = countdown(5)
for i in c:
    print(i, end=" ")   # 5 4 3 2 1 
```

````python
class Test:
    def __init__(self, limit):
        self.limit = limit

    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        # Else increment and return old value
        self.x = x + 1
        return x
````