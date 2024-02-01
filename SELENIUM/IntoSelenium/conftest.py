import pytest
import time
from selenium import webdriver

"""application.py"""


class Application:
    def __init__(self, browser_name):
        self.browser = browser_name
        if self.browser == 'chrome':
            self.wd = webdriver.Chrome()
        else:
            self.wd = webdriver.Firefox()

    def test_git(self):
        self.wd.get("https://git-scm.com/")
        time.sleep(3)
        self.wd.quit()

    def test_google(self):
        self.wd.get("https://www.google.com/")
        time.sleep(3)
        self.wd.quit()


"""conftest.py"""


@pytest.fixture(scope='session')
def app(browser_name):
    return Application(browser_name)


"""test_chrome.py"""


@pytest.fixture(scope='function')
def app():
    return Application('chrome')


"""test_firefox.py"""


@pytest.fixture(scope='function')
def app():
    return Application('firefox')
