import pytest
import random
import requests

# # Параметризация фикстурой
# def test_parametrized_with_fixture(fixture_with_params):
#     print("\nThe value from fixture = ", fixture_with_params)
#     assert fixture_with_params > 0
#
#
# # Параметризация одним параметром
# @pytest.mark.parametrize("test_input", [1, 2, 3])
# def test_parametrize_with_mark_single(test_input):
#     assert test_input < 4


# Использование нескольких параметров
"""ids это:
path_to_test/test_fixtures_parametrization.py::test_parametrize_with_mark_multiple[Three + Five] PASSED 
path_to_test/test_fixtures_parametrization.py::test_parametrize_with_mark_multiple[Two + Four] PASSED 
path_to_test/test_fixtures_parametrization.py::test_parametrize_with_mark_multiple[Six by Nine] FAILED"""


@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)],
                         ids=["Three + Five", "Two + Four", "Six by Nine"])
def test_parametrize_with_mark_multiple(test_input, expected):
    assert eval(test_input) == expected

# # Вложенная параметризация
# # Можно добавить
# @pytest.mark.parametrize("x", [0, 1])
# @pytest.mark.parametrize("y", [2, 3])
# def test_foo(x, y):
#     print(x, y)


# Combine parametrization
# каждый из параметров сравнивается с первым из фикстуры, затем каждый из параметров со вторым из фикстуры, и т.д.
# 1-a, 2-a, 3-a, 1-b, 2-b, 3-b, 1-c, 2-c, 3-c
# @pytest.mark.parametrize("test_input", [1, 2, 3])
# def test_one_2(test_input, fixture_with_params):
#     print(test_input, fixture_with_params)


"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

# Другой пример
@pytest.mark.parametrize('input_id, output_id',
                         [(10000, '10000'),
                          (-1, '-1'),
                          (0, '0')])
@pytest.mark.parametrize('input_title, output_title',
                         [('title', 'title'),
                          ('', ''),
                          (100, '100'),
                          ('&', '&')])
def test_api_post_request(base_url, input_id, output_id, input_title, output_title):
    res = requests.post(
        base_url + "/posts",
        data={'title': input_title, 'body': 'bar', 'userId': input_id})
    res_json = res.json()
    assert res_json['title'] == output_title
    assert res_json['body'] == 'bar'
    assert res_json['userId'] == output_id


# Param filtering users posts by id
# https://jsonplaceholder.typicode.com/posts?userId=1
@pytest.mark.parametrize('userId', [-1, 0, 'a', 11])
def test_api_empty_response(base_url, userId):
    res = requests.get(
        base_url + "/posts",
        params={'userId': userId}
    )
    # Проверяем что на таких данных ответ пустой
    assert res.json() == []


# Param filtering users by id
# https://jsonplaceholder.typicode.com/posts?userId=1
@pytest.mark.parametrize('userId, userId_in_response', [(1, 1), (2, 2), (10, 10)])
def test_api_filtering(base_url, userId, userId_in_response):
    response = requests.get(
        base_url + "/posts",
        params={'userId': userId}
    ).json()
    random_post_number = random.randint(1, 9)
    assert len(response) > 0
    assert response[random_post_number]['userId'] == userId_in_response