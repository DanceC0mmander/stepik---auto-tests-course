import time 


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_add_to_basket_btn(browser):
	browser.get(link)
	time.sleep(10)
	add_to_basket_btn = browser.find_element_by_css_selector(".btn-add-to-basket")
	time.sleep(3)
	
	assert add_to_basket_btn.is_displayed(), "No Button"
