import random
from selenium.webdriver.common.by import By

from config import CHROMEDRIVER
from selenium.webdriver import ActionChains
from selenium import webdriver

chrome = webdriver.Chrome(executable_path=CHROMEDRIVER)

# Долгое открытие страницы
chrome.implicitly_wait(20)
chrome.maximize_window()

# Открываем страницу и закрываем поп-ап
chrome.get("https://konflic.github.io/examples/drawdivs/index.html")

# Получаем облассть в которой можно рисовать
draw_area = chrome.find_element(By.CSS_SELECTOR, "#board")

# Создаем объект ActionChains в который будем записывать наши действия
actions = ActionChains(chrome)

# Наполняем actions 10 разными действиями
for i in range(20):
    # Определяем случайные координаты по x и y
    random_x = random.randint(300, 700)
    random_y = random.randint(300, 700)
    # Нажимаем на кнопку мыши в этих координатах и не отпускаем
    actions.move_to_element_with_offset(draw_area, random_x, random_y).click_and_hold()
    actions.pause(0.5)
    # Определяем случайные величины для смешения курсора от текущей точки
    offset_x = random.randint(-150, 250)
    offset_y = random.randint(-200, 250)
    # Выполняем движение мышью на заданное количество пикселей и отпускаем
    actions.move_by_offset(offset_x, offset_y)
    actions.release()

# Выполняем все накопленные в цикле for действия начиная с первого
actions.perform()

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

def test_drag_and_drop(browser):

    browser.get("https://konflic.github.io/examples/pages/draganddrop.html")
    browser.maximize_window()

    actions = ActionChains(browser)

    # Итерируемся по 10 элементам которые нужно перебросить
    for i in range(1, 11):
        # Создаю строки для селекторов
        card_id = "card{}".format(i)
        zone_id = "zone{}".format(i)
        # Нахожу нужные элементы
        card_element = browser.find_element_by_id(card_id)
        zone_element = browser.find_element_by_id(zone_id)
        # Создаю действие
        actions.click_and_hold(card_element).pause(0.5).move_to_element(zone_element).release()

    actions.perform()