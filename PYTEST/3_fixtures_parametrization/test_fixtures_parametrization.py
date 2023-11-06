import pytest

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
