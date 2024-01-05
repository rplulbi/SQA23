from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://putr.cianjurkab.go.id/administrator-login")
driver.find_element("name", "email").send_keys("putr@cianjurkab.go.id")
driver.find_element("name", "password").send_keys("DinasPUTR123^^" + Keys.ENTER)

driver.quit()
