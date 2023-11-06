import pytest


# @pytest.mark.parametrize("test_input", [1, 2, 3])
# def test_one_2(test_input):
#     print(test_input)


@pytest.mark.parametrize("test_input", [1, 2, 3])
class TestClassParametrized:

    # Все функци должны использовать аргумент
    def test_one(self, test_input):
        pass

    def test_two(self, test_input):
        pass


# Parametrize with fixture
# Каждый параметр будет взят из фикстуры и проверен отдедльно
# def test_one_1(fixture_with_params):
#     print(fixture_with_params)
#
# Combine parametrization
# каждый из параметров сравнивается с первым из фикстуры, затем каждый из параметров со вторым из фикстуры, и т.д.
# 1-a, 2-a, 3-a, 1-b, 2-b, 3-b, 1-c, 2-c, 3-c
# @pytest.mark.parametrize("test_input", [1, 2, 3])
# def test_one_2(test_input, fixture_with_params):
#     print(test_input, fixture_with_params)
