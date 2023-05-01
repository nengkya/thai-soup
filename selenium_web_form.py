import os
from selenium import webdriver
from selenium.webdriver.common.by import By
#for input text in html form
from selenium.webdriver.common.keys import Keys

#import Action chains for pause
from selenium.webdriver.common.action_chains import ActionChains

def test_eight_components():
	driver = webdriver.Chrome()

	#driver.get("https://www.selenium.dev/selenium/web/web-form.html")
	driver.get('https://www.customs.go.th/statistic_report.php?lang=en&')

	title = driver.title
	assert title == "Thai Customs"
	#assert title == "Web form"

	driver.implicitly_wait(0.5)

	#text_box = driver.find_element(by=By.NAME, value="my-text")
	text_box = driver.find_element(by=By.NAME, value="tariff-code")

	#submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
	submit_button = driver.find_element(by=By.CLASS_NAME, value="btn btn-success")

	#text_box.send_keys("Selenium")
	text_box.send_keys("")


	#create action chain object
	action = ActionChains(driver)

	action.pause(5)

	#perform the operation
	action.perform()

	submit_button.click()

	message = driver.find_element(by=By.ID, value="message")
	value = message.text
	assert value == "Received!"

	action.pause(5)

	#perform the operation
	action.perform()

	driver.quit()


if __name__ == '__main__':
	os.system('tput reset')

	test_eight_components()
