import time


def test_add_contact(browser):
    name_input = browser.find_element_by_css_selector("input[name='name']")
    phone_input = browser.find_element_by_css_selector("input[name='phone']")
    name_input.send_keys("Hello")
    phone_input.send_keys("89992323224")
    browser.find_element_by_css_selector("form[id='record']").submit()
    time.sleep(2)


def test_remove_contact(browser):
    before_remove = len(browser.find_elements_by_css_selector("tr[attr='contact']"))
    browser.find_element_by_css_selector("#remove-button").click()
    after_remove = len(browser.find_elements_by_css_selector("tr[attr='contact']"))
    assert before_remove == after_remove + 1
    time.sleep(2)
