"""
Observer: Позволяет одному объекту (наблюдателю) следить и реагировать на изменения в других объектах (субъектах).
"""


class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def update(self, message):
        print(f"Received message: {message}")


# Usage
observable = Observable()
observer1 = Observer()
observer2 = Observer()

observable.add_observer(observer1)
observable.add_observer(observer2)

observable.notify("New message")
