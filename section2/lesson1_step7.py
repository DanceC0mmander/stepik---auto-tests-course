import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти элемент-картинку, который является изображением сундука с сокровищами.
    treasure = browser.find_element_by_id("treasure")

    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = treasure.get_attribute("valuex")

    # Посчитать математическую функцию от x 
    y = calc(x)

    # Ввести ответ в текстовое поле
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Отметить checkbox "I'm the robot"
    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()

    # Выбрать radiobutton "Robots rule!"
    robotsRule = browser.find_element_by_id("robotsRule")
    robotsRule.click()

    # Нажать на кнопку Submit
    submitBtn = browser.find_element_by_css_selector("button[type='submit']")
    submitBtn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    