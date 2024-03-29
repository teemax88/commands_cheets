import platform
import pytest


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="https://www.google.com/", help="Google page")
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('allure')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        # extra.append(pytest_html.extras.url('http://www.example.com/'))
        xfail = hasattr(report, 'wasxfail')
        # if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional allure on failure
            # extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra


@pytest.mark.usefixtures("environment_info")
@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request, environment_info):
    request.config._metadata.update(
        {"browser": request.config.getoption("--browser"),
         "address": request.config.getoption("--address"),
         "test_data": environment_info[1],
         "test_title": "Hello World"})
    yield


@pytest.fixture(scope="session")
def environment_info():
    os_platform = platform.platform()
    linux_dist = platform.machine()
    return os_platform, linux_dist


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        # only add this during call instead of during any stage
        report.test_metadata = 'whatever'
        # edit stage metadata
        report.stage_metadata = {
            'foo': 'bar'
        }
    elif report.when == 'setup':
        report.stage_metadata = {
            'hoof': 'doof'
        }
    elif report.when == 'teardown':
        report.stage_metadata = {
            'herp': 'derp'
        }

