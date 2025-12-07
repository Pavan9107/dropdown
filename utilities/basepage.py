from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger

logger = get_logger("BasePage")

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()
        logger.info(f"Clicked on element: {locator}")

    def type(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        logger.info(f"Typed '{text}' into element: {locator}")

    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        text = element.text
        logger.info(f"Got text '{text}' from element: {locator}")
        return text
