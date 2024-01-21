from behave import *

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


@given('I open admin page')
def open_admin_page(context):
    url = context.config.userdata.get("url", "demo.opencart.com")
    context.driver.get(f"http://{url}/admin")


@when('I input login "{user}" and password "{password}"')
def login_on_admin_page(context, user, password):
    context.driver.find_element_by_id("input-username").send_keys(user)
    context.driver.find_element_by_id("input-password").send_keys(password)


@when('I press submit button')
def login_on_admin_page(context):
    context.driver.find_element_by_css_selector("button[type='submit']").click()


@then('Admin page opens')
def verify_admin_page_opens(context):
    try:
        WebDriverWait(context.driver, 3).until(EC.presence_of_element_located((By.ID, "user-profile")))
    except TimeoutException:
        raise AssertionError("Element #user-profile was not found")


@then('Error message is displayed')
def verify_error_message(context):
    try:
        WebDriverWait(context.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
    except TimeoutException:
        raise AssertionError("Element .alert-danger was not found")
