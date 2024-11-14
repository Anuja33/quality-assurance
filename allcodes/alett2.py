import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the URL
driver.get("https://demo.automationtesting.in/Alerts.html")

# Locate and click on the "Alert with OK" option
confirm_nav = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a")
confirm_nav.click()

# Locate and click on the "click the button to display an alert box" button
button2 = driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button')  # Fixed syntax error here
button2.click()

# Wait for the alert to appear
time.sleep(5)


# Accept the alert
driver.switch_to.alert.dismiss()

time.sleep(5)