import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать сумму заданных чисел
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")

    summa = int(num1.text) + int(num2.text)

    print(summa)

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(summa))

    # Нажать на кнопку Submit
    submitBtn = browser.find_element_by_css_selector("button[type='submit']")
    submitBtn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    