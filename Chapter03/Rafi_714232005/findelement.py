from selenium.webdriver import Chrome

driver = Chrome()
driver.get("https://sso-siasn.bkn.go.id/auth/realms/public-siasn/protocol/openid-connect/auth?client_id=si-kinerja&redirect_uri=https%3A%2F%2Fkinerja.bkn.go.id%2Flogin&state=49535869-1f0b-47e0-9889-adb2ae2ef505&response_mode=fragment&response_type=code&scope=openid&nonce=b9a96742-0e8e-407e-92da-04233eaedd4e")
driver.find_element_by_id("username").sendkeys("199004082020122007")
