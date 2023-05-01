import os
from selenium import webdriver
from selenium.webdriver.common.by import By
#for input text in html form
from selenium.webdriver.common.keys import Keys
#import Action chains for pause
from selenium.webdriver.common.action_chains import ActionChains
#click
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_eight_components():
	options = webdriver.EdgeOptions()
	options.add_argument("start-maximized");
	options.add_argument("disable-infobars")
	options.add_argument("--disable-extensions")

	driver = webdriver.Edge(options=options)

	driver.get('https://www.customs.go.th/statistic_report.php?lang=en&')

	WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form[1]/div[3]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[7]/td[2]/button[1]"))).click()

	title = driver.title
	assert title == "Thai Customs"

	#create action chain object
	action = ActionChains(driver)

	text_box = driver.find_element(by=By.NAME, value="tariff_code")

	#submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

	text_box.send_keys("39011012000")

	action.pause(3)

	#perform the operation
	action.perform()

	#submit_button.click()
	#action.move_to_element(submit_button).click(submit_button).perform()

	'''
	message = driver.find_element(by=By.ID, value="message")
	value = message.text
	assert value == "Received!"
	'''

	driver.quit()


if __name__ == '__main__':
	os.system('tput reset')

	test_eight_components()
