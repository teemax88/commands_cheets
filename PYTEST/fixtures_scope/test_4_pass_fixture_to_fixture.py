import pytest

"""
Тут играет правило: первый вошел - последним вышел.
Тест ссылается на фикстуру2, а он ссылается на фикстуру1
В итоге запускается: print фикстура1 - yield пауза - print фикстура2 - yield пауза - запуск теста - 
print фикстура2 - print фикстура1
"""


@pytest.fixture
def fixture_one():
    print("\nHey, this is fixture one!")
    yield
    print("\nBye from fixture one!")


@pytest.fixture
def fixture_two(fixture_one):
    print("\nHey, this is fixture two!")
    yield
    print("\nBye from fixture two!")


def test_function(fixture_two):
    print("\nHey, I'm test function!")
