from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

#UJI KATA SANDI DI WEBSITE RENAN STORE
driver = webdriver.Chrome(options=options)
driver.get("https://renanstore.co.id/myaccount/login/")
driver.maximize_window()

#INPUT EMAIL SALAH PASSWORD BENAR
driver.find_element("id", "user_login").send_keys("rafi.rustian@gmail.com")
driver.find_element("id", "user_pass").send_keys("08April1990")  
login_button = driver.find_element("id","wp-submit")
login_button.click()

#INPUT EMAIL BENAR PASSWORD SALAH
driver.find_element("id", "user_login").send_keys("saumirafi@gmail.com")
driver.find_element("id", "user_pass").send_keys("08April1991")  
login_button = driver.find_element("id","wp-submit")
login_button.click()

#INPUT EMAIL DAN PASSWORD BENAR
driver.find_element("id", "user_login").send_keys("saumirafi@gmail.com")
driver.find_element("id", "user_pass").send_keys("08April1990")  
login_button = driver.find_element("id","wp-submit")
login_button.click()

#APABILA LOGIN BERHASI MUNCUL TOPBOX KELUAR DARI DRIVER
driver.find_element("id", "topbox")

driver.quit()
