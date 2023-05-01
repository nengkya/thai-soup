import os
from selenium import webdriver
from selenium.webdriver.common.by import By

#import Action chains for pause
from selenium.webdriver.common.action_chains import ActionChains

def test_eight_components():
	driver = webdriver.Chrome()

	#driver.get("https://www.selenium.dev/selenium/web/web-form.html")
	driver.get('https://www.customs.go.th/statistic_report.php?lang=en&')

	title = driver.title
	assert title == "Thai Customs"

	#driver.implicitly_wait(0.5)

	text_box = driver.find_element(by=By.NAME, value="my-text")

	submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

	#create action chain object
	action = ActionChains(driver)

	action.pause(15)

	#perform the operation
	action.perform()

	text_box.send_keys("Selenium")
	submit_button.click()

	message = driver.find_element(by=By.ID, value="message")
	value = message.text
	assert value == "Received!"

	driver.quit()


if __name__ == '__main__':
	os.system('tput reset')

	test_eight_components()
