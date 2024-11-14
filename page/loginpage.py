import time
from selenium.webdriver.common.by import By
from locate.locators import Locate

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.lc = Locate

    def loginp(self, username, password):
        driver = self.driver
        nav_login = driver.find_element(By.ID, self.lc.nav_log_id)
        nav_login.click()
        driver.implicitly_wait(5)

        # Locate username field and enter username
        uname = driver.find_element(By.ID, self.lc.uname_id)
        uname.send_keys(username)

        # Locate password field and enter password
        pwd = driver.find_element(By.ID, self.lc.pwd_id)
        pwd.send_keys(password)

        # Locate login button and click it
        login_button = driver.find_element(By.XPATH, self.lc.lb_xpath)
        login_button.click()

        # Wait for a while to observe the result
        time.sleep(10)
