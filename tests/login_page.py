from utilities.browser_manager import get_driver
from pages.login_page import LoginPage
from utilities.config_loader import load_config

# Step 1: Load configuration
config = load_config()
username = config["salesforce"]["username"]
password = config["salesforce"]["password"]
base_url = config["salesforce"]["base_url"]

# Step 2: Launch browser
driver = get_driver()

# Step 3: Initialize page objects
login_page = LoginPage(driver)

# Step 4: Open Salesforce login page
login_page.open(base_url)

# Step 5: Perform login
login_page.login(username, password)

# Step 6: Close browser
driver.quit()
