from selenium import webdriver

driver = webdriver.Edge()

# to maximize the browser window
driver.maximize_window()

#get method to launch the URL
driver.get("https://www.tutorialspoint.com/index.htm")

#to refresh the browser
driver.refresh()

# identifying the edit box with the help of id and enter text
driver.find_element(by=By.ID, value = "gsc-i-id1").send_keys("Selenium")

# submit the text contents
driver.find_element(By.id("gsc-i-id1")).submit()

#to close the browser
driver.close()
