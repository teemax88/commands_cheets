import allure
from allure_commons.types import Severity
# $ pytest directory_with_tests/ --alluredir=/tmp/my_allure_report \
#  --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'


@allure.link('https://www.youtube.com/watch?v=4YYzUTYZRMU')
def test_with_link():
    pass


@allure.link('https://www.youtube.com/watch?v=Su5p2TqZxKU', name='Click me')
def test_with_named_link():
    pass


@pytest.mark.skip(reason="JIRA-9000")
@allure.issue('https://pytest.org', 'Pytest-flaky test retries shows like test steps')
def test_with_issue_link():
    assert False


@allure.testcase(TEST_CASE_LINK, 'Test case title')
def test_with_testcase_link():
    pass

@allure.severity(severity_level=Severity.BLOCKER)
@allure.link('https://docs.qameta.io/allure/#_pytest', name='I am custom link name')
def test_with_named_link():
    pass