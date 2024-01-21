from behave import *

from selenium import webdriver


@given('I open "{browser}" browser')
def open_browser(context, browser):
    if browser.lower() == "chrome":
        context.driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        context.driver = webdriver.Firefox()
    context.driver.maximize_window()


@given('I open browser')
def open_param_browser(context):
    browser = context.config.userdata.get("browser", "chrome")
    if browser.lower() == "chrome":
        context.driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        context.driver = webdriver.Firefox()
    context.driver.maximize_window()


@then('I close browser')
def close_browser(context):
    context.driver.close()
