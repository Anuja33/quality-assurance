import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.demoblaze.com/")

# Locate and click on the login navigation link
nav_login = driver.find_element(By.ID, 'login2')
nav_login.click()

try:
    # Locate username field and enter username
    uname = driver.find_element(By.ID, 'loginusername')
    uname.send_keys("testmorning")

    # Locate password field and enter password
    pwd = driver.find_element(By.ID, 'loginpassword')
    pwd.send_keys("test123")

    # Locate login button and click it
    login_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    login_button.click()

    # Wait for a while to observe the result
    time.sleep(10)

except ElementNotInteractableException as e:
    # Print the exception if something goes wrong
    print("This is from not interactable exception")

    # Try again with implicit wait
    driver.implicitly_wait(5)

    # Locate username field and enter username again
    uname = driver.find_element(By.ID, 'loginusername')
    uname.send_keys("testmorning")

    # Locate password field and enter password again
    pwd = driver.find_element(By.ID, 'loginpassword')
    pwd.send_keys("test123")

    # Locate login button and click it again
    login_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    login_button.click()

    # Wait for a while to observe the result
    time.sleep(10)
