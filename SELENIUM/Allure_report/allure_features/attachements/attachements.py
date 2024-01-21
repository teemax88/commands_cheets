import allure
import pytest
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def attach_file_in_module_scope_fixture_with_finalizer(request):
    allure.attach('A text attacment in module scope fixture', 'blah blah blah', allure.attachment_type.TEXT)

    def finalizer_module_scope_fixture():
        allure.attach('A text attacment in module scope finalizer', 'blah blah blah blah',
                      allure.attachment_type.TEXT)
    request.addfinalizer(finalizer_module_scope_fixture)


def test_with_attacments_in_fixture_and_finalizer(attach_file_in_module_scope_fixture_with_finalizer):
    with allure.step("Step one"):
        with allure.step("Inner step two"):
            with allure.step("Super inner"):
                pass


def test_multiple_attachments():
    allure.attach.file('/home/msamoylov/Downloads/hqdefault.jpg', attachment_type=allure.attachment_type.PNG)
    allure.attach('<head></head><body> a page </body>', 'Attach with HTML type', allure.attachment_type.HTML)

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

def test_attachments_failed(driver):
    driver.get("https://yandex.ru")

    with allure.step("Прикрепил html"):

        allure.attach(
            body=driver.page_source,
            name='Attach_with_HTML_type',
            attachment_type=allure.attachment_type.HTML)
        with allure.step("Поиск элемента"):
            try:
                driver.find_element_by_css_selector("no-such-selector")
            except NoSuchElementException as e:
                allure.attach(
                    body=driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG)
                raise AssertionError(e.msg)


def test_attachments_success(driver):
    driver.get("https://yandex.ru")
    with allure.step("Прикрепил html"):
        allure.attach(
            body='<h1>HTML is here</h1><span>And it is very good</span><br><a href="https://otus.ru">OTUS</a>',
            name='Attach_with_HTML_type',
            attachment_type=allure.attachment_type.HTML)
        with allure.step("Выполняю элемента"):
            try:
                driver.find_element_by_css_selector("input")
            except NoSuchElementException as e:
                allure.attach(body=driver.get_screenshot_as_png(),
                              name="screenshot_image")
                raise AssertionError(e.msg)