import os
from selenium import webdriver
from selenium.webdriver.common.by import By

#import Action chains for pause
from selenium.webdriver.common.action_chains import ActionChains

def test_eight_components():
	options = webdriver.ChromeOptions()
	options.add_argument("start-maximized");
	options.add_argument("disable-infobars")
	options.add_argument("--disable-extensions")

	driver = webdriver.Chrome(options=options)

	driver.get("https://www.selenium.dev/selenium/web/web-form.html")
	#driver.get('https://www.customs.go.th/statistic_report.php?lang=en&')

	title = driver.title
	#assert title == "Thai Customs"
	assert title == "Web form"

	text_box = driver.find_element(by=By.NAME, value="my-text")
	#text_box = driver.find_element(by=By.NAME, value="tariff_code")

	submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

	text_box.send_keys("39011012000")

	#create action chain object
	action = ActionChains(driver)

	action.pause(3)

	#perform the operation
	action.perform()

	submit_button.click()

	message = driver.find_element(by=By.ID, value="message")
	value = message.text
	assert value == "Received!"

	action.pause(1)
	action.perform()

	driver.quit()


if __name__ == '__main__':
	os.system('tput reset')

	test_eight_components()
