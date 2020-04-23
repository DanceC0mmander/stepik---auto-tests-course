import time
from selenium import webdriver
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

# Создайте класс с тестами, который должен наследоваться от unittest.TestCase 
class TestRegistrationForm( unittest.TestCase ):
	
	def test_registration1( self ):
		
		browser = webdriver.Chrome()
		browser.get(link1)

		first_name = browser.find_element_by_xpath("//input[contains(@placeholder, 'first')]")
		first_name.send_keys("Tasya")

		last_name = browser.find_element_by_xpath("//input[contains(@placeholder, 'last')]")
		last_name.send_keys("Babasya")

		email = browser.find_element_by_xpath("//input[contains(@placeholder, 'email')]")
		email.send_keys("tasya@babasy.com")

		submit_button = browser.find_element_by_css_selector("button[type='submit']")
		submit_button.click()

		time.sleep(1)
		message = browser.find_element_by_tag_name("h1")
		message_text = message.text

		self.assertEqual( "Congratulations! You have successfully registered!", message_text, "You did something wrong" )

	def test_registration2( self ):
		
		browser = webdriver.Chrome()
		browser.get(link2)

		first_name = browser.find_element_by_xpath("//input[contains(@placeholder, 'first')]")
		first_name.send_keys("Tasya")

		email = browser.find_element_by_xpath("//input[contains(@placeholder, 'email')]")
		email.send_keys("tasya@babasy.com")

		submit_button = browser.find_element_by_css_selector("button[type='submit']")
		submit_button.click()

		time.sleep(1)
		message = browser.find_element_by_css_selector("h1")
		message_text = message.text

		self.assertEqual( "Congratulations! You have successfully registered!", message_text, "You did something wrong" )


if __name__ == "__main__":
	unittest.main()

