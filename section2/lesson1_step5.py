import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element_by_id("input_value")

    # Посчитать математическую функцию от x 
    x = x_element.text
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
    