import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    submitBtn = browser.find_element_by_css_selector("button[type='submit']")
    submitBtn.click()

    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Пройти капчу для робота и получить число-ответ
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    submitBtn = browser.find_element_by_css_selector("button[type='submit']")
    submitBtn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    