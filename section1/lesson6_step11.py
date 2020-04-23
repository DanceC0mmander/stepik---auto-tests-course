import time

# webdriber это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему.
# ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")

# напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# после выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()