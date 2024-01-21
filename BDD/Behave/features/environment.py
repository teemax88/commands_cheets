from behave import fixture
from behave import use_fixture
from selenium import webdriver


@fixture
def browser_firefox(context):
    context.driver = webdriver.Firefox()
    yield context.driver
    context.driver.maximize_window()
    context.driver.close()


@fixture
def browser_chrome(context):
    context.driver = webdriver.Chrome()
    context.add_cleanup(context.driver.close)
    context.driver.maximize_window()
    return context.driver


def before_tag(context, tag):
    if tag == "fixture.browser.firefox":
        use_fixture(browser_firefox, context)
    elif tag == "fixture.browser.chrome":
        use_fixture(browser_chrome, context)
