from selenium.webdriver import Chrome

driver = Chrome()
driver.get("https://www.google.co.id/")
driver.find_element("name", "q")