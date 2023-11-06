import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",    # Название опции
        action="store",
        default="https://ya.ru",    # Этот параметр говорит, какое значение использовать по умолчанию
        required=True,  # Этот параметр говорит, что указывать url ОБЯЗАТЕЛЬНО (иначе будет ошибка)
        help="This is request url"  # Этот параметр говорит, что делает эта опция (как справка)
    )


@pytest.fixture
def url_param(request):
    return request.config.getoption("--url")
