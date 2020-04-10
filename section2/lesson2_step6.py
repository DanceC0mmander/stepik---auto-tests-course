import math
from selenium import webdriver
import time

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    # Посчитать математическую функцию от x
    y = calc(x)

    # Проскроллить страницу вниз до кнопки Submit включительно
    submitBtn = browser.find_element_by_css_selector("button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'})", submitBtn)
    
    # Ввести ответ в текстовое поле
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Выбрать checkbox "I'm the robot"
    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()

    # Переключить radiobutton "Robots rule!"
    robotsRule = browser.find_element_by_id("robotsRule")
    robotsRule.click()

    # Нажать на кнопку Submit
    submitBtn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    