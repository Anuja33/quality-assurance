import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the URL
driver.get("https://demo.automationtesting.in/Alerts.html")

# Locate and click on the "Alert with OK" option
textbox_nav = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a")
textbox_nav.click()

# Locate and click on the "click the button to display an alert box" button
button3 = driver.find_element(By.XPATH, '//*[@id="Textbox"]/button')  # Fixed syntax error here
button3.click()

# Wait for the alert to appear
time.sleep(5)
driver.switch_to.alert.send_keys("anuja")

# Accept the alert
driver.switch_to.alert.accept()

time.sleep(5)