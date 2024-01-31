import pytest
import requests


class APIClient:
    """
    Упрощенный клиент для работы с API
    Инициализируется базовым url на который пойдут запросы
    """

    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        return requests.get(url=self.base_address + path, params=params)


# Тестовое API: https://jsonplaceholder.typicode.com
def pytest_addoption(parser):
    parser.addoption(
        "--url",  # Название опции
        action="store",
        default="https://ya.ru",  # Этот параметр говорит, какое значение использовать по умолчанию
        required=True,  # Этот параметр говорит, что указывать url ОБЯЗАТЕЛЬНО (иначе будет ошибка)
        help="This is request url"  # Этот параметр говорит, что делает эта опция (как справка)
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)


"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""


# 2-й Пример

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://httpbin.org/",
        help="This is request url"
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="method to execute"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))
