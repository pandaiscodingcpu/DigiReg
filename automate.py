from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/")

# Wait for the username field to load
wait = WebDriverWait(driver, 15)
username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

username.send_keys("vaishnavarchit06@gmail.com")
password.send_keys("python@ai.com")
login_button.click()

time.sleep(5)
