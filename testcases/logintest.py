import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page.loginpage import Login  # Import the Login page class


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com")
        self.lp = Login(self.driver)  # Corrected `self.lb` to `self.lp`

    def test_login(self):  # Updated method name for clarity
        driver = self.driver
        self.lp.loginp("testmorning", "test123")  # Call the login method

        # Check if login was successful by comparing the welcome message
        expected_result = "Welcome testmorning"
        actual_result = driver.find_element(By.ID, "nameofuser").text
        self.assertEqual(expected_result, actual_result, "Username and logged-in username did not match")

        time.sleep(5)  # To observe the result, if necessary

    def tearDown(self) -> None:
        self.driver.quit()  # Close the browser after
