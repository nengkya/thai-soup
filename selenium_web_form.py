import os

from selenium import webdriver
from selenium.webdriver.common.by import By

#for input text in html form
from selenium.webdriver.common.keys import Keys

#click
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#extract form submit result
from bs4 import BeautifulSoup

import urllib.request


def test_eight_components():
	options = webdriver.EdgeOptions()
	options.add_argument("start-maximized");
	options.add_argument("disable-infobars")
	options.add_argument("--disable-extensions")

	driver = webdriver.Edge(options=options)

	driver.get('https://www.customs.go.th/statistic_report.php?lang=en&')

	title = driver.title
	assert title == "Thai Customs"

	text_box = driver.find_element(by=By.NAME, value="tariff_code")

	hs_code = "39011012000"

	text_box.send_keys(hs_code)

	WebDriverWait(driver, 0).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form[1]/div[3]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[7]/td[2]/button[1]"))).click()

	soup = BeautifulSoup(driver.page_source, features = "html.parser")

	with open(hs_code + ".html", "w") as file:
		file.write(str(soup))

	##########extract data
	#Verifying tables and their classes
	print('Classes of each table:')

	for table in soup.find_all('table'):

		print(table.get('class'))
	##########

	driver.quit()


if __name__ == '__main__':
	os.system('tput reset')

	test_eight_components()
