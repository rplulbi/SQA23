from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.co.id/")
driver.find_element("name", "q").send_keys("Rafi Saumi Rustian" + Keys.ENTER)
assert "Rafi Saumi Rustian" in driver.find_element("css_selector","h3").text
assert "Rafi Saumi Rustian" in driver.title

driver.quit()
