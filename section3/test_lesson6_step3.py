import pytest
import time
import math
from selenium import webdriver


def answer():
	return str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
	print("\nstart browser for test..")
	browser = webdriver.Chrome()
	browser.implicitly_wait(10) # фидбек может появиться не сразу
	yield browser
	print("\nquit browser..")
	browser.quit()

@pytest.mark.parametrize('lesson', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_check_answer(browser, lesson):
	link = f"https://stepik.org/lesson/236{lesson}/step/1"
	browser.get(link)
	# ввести правильный ответ 
	textarea = browser.find_element_by_css_selector("textarea")
	textarea.send_keys(answer())
	# нажать кнопку "Отправить" 
	sendBtn = browser.find_element_by_css_selector(".submit-submission")
	sendBtn.click()
	# дождаться фидбека о том, что ответ правильный
	feedback = browser.find_element_by_css_selector(".smart-hints__hint")
	feedback_text = feedback.text
	print(feedback_text)
	# проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
	assert feedback_text == "Correct!"
