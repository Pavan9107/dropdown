import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[text() = 'Click for JS Alert']").click()
alert = driver.switch_to.alert
alert.accept()
time.sleep(5)

driver.find_element(By.XPATH, "//button[text() = 'Click for JS Confirm']").click()
alert = driver.switch_to.alert
alert.dismiss()
time.sleep(5)