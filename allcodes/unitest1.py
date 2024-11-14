import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com")

    def test_login(self):
        driver = self.driver
        nav_login = driver.find_element(By.ID, 'login2')
        nav_login.click()
        driver.implicitly_wait(5)

        # Locate and enter username
        uname = driver.find_element(By.ID, 'loginusername')
        uname.send_keys("testmorning")  # Sample username

        # Locate and enter password
        pwd = driver.find_element(By.ID, 'loginpassword')
        pwd.send_keys("test123")  # Sample password

        # Locate and click the login button
        login_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        login_button.click()

        time.sleep(5)

        # Verify the login was successful by checking welcome message
        expected_result = "Welcome testmorning"
        actual_result = driver.find_element(By.ID, "nameofuser").text
        self.assertEqual(expected_result, actual_result, "Login failed: Usernames do not match.")

    def tearDown(self) -> None:
        self.driver.quit()


# Running the test
if __name__ == "__main__":
    unittest.main()
