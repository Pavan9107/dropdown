from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.amazon.in/")

# Wait for page to load
time.sleep(3)

# Capture full page screenshot
screenshot_path = "amazon_homepage.png"
driver.save_screenshot(screenshot_path)
print(f"Screenshot saved at: {screenshot_path}")

driver.quit()
