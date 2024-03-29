import pytest


@pytest.mark.webtest
def test_send_http():
    pass  # perform some webtest test for your app


def test_something_quick():
    pass


def test_another():
    pass


class TestClass(object):
    def test_method(self):
        pass


# Run marked tests
# pytest -v -m webtest
# pytest -v -m "not webtest"
# Using -k expr to select tests based on their name -- Запуск по части названия теста
# pytest -v -k http
# pytest -k "not send_http" -v
# pytest -k "http or quick" -v

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""


@pytest.mark.env("stage1")
def test_basic_db_operation():
    print('Test result1')


@pytest.mark.env("stage1")
@pytest.mark.env("stage2")
def test_basic_db_operation_ex():
    print('Test result2')


# pytest -E stage2
# pytest -E stage1

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""


# Platform_specific
@pytest.mark.darwin
def test_if_apple_is_evil():
    pass


@pytest.mark.linux
def test_if_linux_works():
    pass


@pytest.mark.win32
def test_if_win32_crashes():
    pass


def test_runs_everywhere():
    pass
