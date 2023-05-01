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
	############click
	options = webdriver.ChromeOptions()
	options.add_argument("start-maximized");
	options.add_argument("disable-infobars")
	options.add_argument("--disable-extensions")

	'''
	/usr/lib/chromium-browser/chromedriver
	To put the chromedriver binary in the path,
	you would write
	export PATH=$PATH:/usr/lib/chromium-browser/
	'''
	#driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Utility\BrowserDrivers\chromedriver.exe')
	driver = webdriver.Chrome(chrome_options=options)

	driver.get('https://www.customs.go.th/statistic_report.php?lang=en&')
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@track-element='header-login']"))).click()
	###########

	title = driver.title
	assert title == "Thai Customs"

	#driver.implicitly_wait(0.5)

	#create action chain object
	action = ActionChains(driver)

	text_box = driver.find_element(by=By.NAME, value="tariff_code")

	submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

	text_box.send_keys("39011012000")

	driver.implicitly_wait(10)

	#submit_button.click()
	ActionChains(driver).move_to_element(submit_button).click(submit_button).perform()

	message = driver.find_element(by=By.ID, value="message")
	value = message.text
	assert value == "Received!"

	action.pause(3)

	#perform the operation
	action.perform()

	driver.quit()


if __name__ == '__main__':
	os.system('tput reset')

	test_eight_components()
