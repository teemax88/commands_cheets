import pytest
"""
для отдельного теста вывод будет:
    print(f"{request.node}")    # <Function test_one>
    print(f"{request.scope}")   # function
    print(f"{request.cls}")    # None
    print(f"{request.module}")  # <module 'test_1_fixtures_request' from 'path/to/file'>
    
Для теста в классе вывод будет:
    print(f"{request.node}")    # <Function test_two>
    print(f"{request.scope}")   # function
    print(f"{request.cls}")    # <class 'test_1_fixtures_request.TestClass'>
    print(f"{request.module}")  # <module 'test_1_fixtures_request' from 'path/to/file'>
"""


@pytest.fixture()
def first_fixture_for_request(request):
    print("___________________________")
    print(f"{request.node}")    # <Function test_one>
    print(f"{request.scope}")   # function
    print(f"{request.cls}")    # None
    print(f"{request.module}")  # <module 'test_1_fixtures_request' from 'path/to/file'>
    print("___________________________")
    # print("\nRequset object data: ")
    # for el in list(dir(request)):
    #     print(el)


def test_one(first_fixture_for_request):
    print("\nPrint from 'test_one'")


class TestClass:

    def test_two(self, first_fixture_for_request):
        print("\nPrint from 'test_two'")

    def test_three(self, first_fixture_for_request):
        print("\nPrint from 'test_three'")
