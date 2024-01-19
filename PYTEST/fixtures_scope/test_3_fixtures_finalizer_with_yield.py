import pytest

"""
При scope="function" фикстура выведет первый print, потом с помощью yield встанет на паузу, подождет пока выполнится 1-й
тест, а затем выведет второй print. По той же схеме будет отработан 2-й тест. Тут все в рамках функции (теста)

При scope="module" фикстура выведет первый print, потом с помощью yield встанет на паузу, подождет пока выполнятся ОБА 
теста, а затем выведет второй print. Тут все в рамках файла (модуля)
"""


@pytest.fixture(scope="function")
def setup_function_fixture():
    print("\nHello from setup function fixture!\n")
    yield
    print("\nBye bye from setup function fixture!\n")


# @pytest.fixture(scope="module")
# def setup_function_fixture():
#     print("\nHello from setup module fixture!\n")
#     yield
#     print("\nBye bye from setup module fixture!\n")


def test_one(setup_function_fixture):
    print("Hello, i'm test_one")


def test_two(setup_function_fixture):
    print("Hello, i'm test_two")


""" ///////////////************************///////////////////// """

"""
request.addfinalizer(fin) - запускает после теста функцию fin
"""


@pytest.fixture()
def first_fixture_for_request(request):
    def fin():
        print("\nThis is finalizer from first_fixture_for_request ")

    request.addfinalizer(fin)


def test_first(first_fixture_for_request):
    print("\nPrint from 'test_one'")


class TestClass:

    def test_second(self, first_fixture_for_request):
        print("\nPrint from 'test_two'")

    def test_third(self, first_fixture_for_request):
        print("\nPrint from 'test_three'")