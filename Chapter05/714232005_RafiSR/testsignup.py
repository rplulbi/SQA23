from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.roblox.com/")
driver.maximize_window()

dropdown = driver.find_element("id", "MonthDropdown")
dropdown.click()
option = driver.find_element("xpath","//option[@value='Apr']")
option.click()

driver.find_element("id", "DayDropdown")
dropdown.click()
option = driver.find_element("xpath","//option[@value='08']")
option.click()


driver.find_element("id", "YearDropdown")
dropdown.click()
option = driver.find_element("xpath","//option[@value='1990']")
option.click()

driver.find_element("name","signupUsername").send_keys("rsrustian109")
driver.find_element("name","signupPassword").send_keys("@rsrustian109")  

gender_button = driver.find_element("id","FemaleButton")
gender_button.click()

signup_button = driver.find_element("id","signup-button")
signup_button.click()
