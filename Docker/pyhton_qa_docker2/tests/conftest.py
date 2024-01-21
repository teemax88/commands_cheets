import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--app_host", default="http://192.168.1.73")
    parser.addoption("--executor", default="192.168.1.73")


@pytest.fixture
def browser(request):

    bro = request.config.getoption("--browser")
    app_host = request.config.getoption("--app_host")
    executor = request.config.getoption("--executor")

    caps = {"browserName": bro}

    wd = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub", desired_capabilities=caps)
    request.addfinalizer(wd.quit)
    wd.get(app_host)
    return wd

