from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from utilities.config_loader import load_config
from utilities.logger import get_logger

logger = get_logger("browser_manager")

def get_driver():

    config = load_config()
    browser_type = config["browser"]["type"]
    browser_wait_imp = config["browser"]["implicit_wait"]

    logger.info(f"Launching browser: {browser_type}")

    if browser_type == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    else:
        raise ValueError(f"Browser not supported: {browser_type}")


    driver.maximize_window()
    driver.implicitly_wait(browser_wait_imp)

    logger.info("Browser successfully launched.")
    return driver