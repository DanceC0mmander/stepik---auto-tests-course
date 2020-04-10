import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    firstName = browser.find_element_by_name("firstname")
    firstName.send_keys("Tasya")

    lastName = browser.find_element_by_name("lastname")
    lastName.send_keys("Babasya")

    email = browser.find_element_by_name("email")
    email.send_keys("tasya@babasya.com")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    file_attach = browser.find_element_by_id("file")
    folder = os.path.abspath( os.path.dirname(__file__) ) # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(folder, "additional_files/blah.txt") # добавляем к этому пути путь до файла и его название
    file_attach.send_keys(file_path)

    # Нажать на кнопку Submit
    submitBtn = browser.find_element_by_css_selector("button[type='submit']")
    submitBtn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    