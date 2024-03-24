import pytest

from src.baseclasses.response import Response
from src.pydantic_schemas.user import User

from src.pydantic_schemas.computer import Computer
from examples import computer


# Для allure первый запуск тестов и создание папки для хранения результатов
# allureress - это название папки (может быть любым)
# pytest -s -v tests\users\test_users.py --alluredir=allureress

# Далее генерируем отчет в html
# allure serve allureress

def test_getting_users_list(get_users, calculate, make_number):
    Response(get_users).assert_status_code(200).validate(User)


@pytest.mark.production
@pytest.mark.development
@pytest.mark.skip('[ISSUE - 32354] Issue with network connection')
def test_another():
    assert 1 == 1  # SKIPPED ([ISSUE - 32354] Issue with network connection)


# запустить тесты с маркером development
# pytest -s -v -k development tests\users\test_users.py

# запустить тесты, которые не маркированы как development
# pytest -s -v -k "not development" tests\users\test_users.py
@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b', 'b', None)
])
def test_calculator(first_value, second_value, result, calculate):
    """
    In test we are testing calculating with different values (valid and invalid)
    """
    assert calculate(first_value, second_value) == result


@pytest.mark.production
@pytest.mark.development
def test_another_failing():
    """
    In that test we try to check that 1 is equal to 2
    """
    assert 1 == 2


def test_pydantic_object():
    comp = Computer.parse_obj(computer)
    print(comp.detailed_info)
