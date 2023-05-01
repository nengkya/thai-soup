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
import pandas as pd
import csv


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

	#pd.set_option('display.max_colwidth', 30)	
	#pd.set_option('display.max_column', None)	

	df_pandas=pd.read_html(driver.page_source, attrs={'class':'table-bordered'},flavor='bs4')

	####################
	#field names 
	fields = ['Name', 'Branch', 'Year', 'CGPA'] 
		
	#data rows of csv file 
	rows = df_pandas[1].values.tolist()
	
	#name of csv file

	'''
	for	mylist in soup.find_all("li", {"class": "active"}):
		for a in soup.find_all('a', href=True):
			print("Found the URL:", a['href'])
	'''

	filename = "university_records.csv"
		
	#writing to csv file 
	with open(filename, 'w') as csvfile: 
		#creating a csv writer object 
		csvwriter = csv.writer(csvfile) 
			
		#writing the fields 
		csvwriter.writerow(fields) 
			
		#writing the data rows
		for i in range(0, 3):
			csvwriter.writerow(rows[i])
	##############

	for i in range(0, 3):
		print(type(rows[i]))
		print(rows[i])

	driver.quit()


if __name__ == '__main__':
	os.system('tput reset')

	test_eight_components()
