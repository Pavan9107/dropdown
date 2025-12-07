from selenium.webdriver.common.by import By
from utilities.basepage import BasePage
from utilities.logger import get_logger

logger = get_logger("LoginPage")

class LoginPage(BasePage):
    # Salesforce login page locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "Login")

    def __init__(self, driver):
        super().__init__(driver)  # initialize BasePage
        logger.info("LoginPage initialized")

    def login(self, username, password):
        """
        Perform login on Salesforce.
        """
        logger.info(f"Logging in with user: {username}")
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        logger.info("Login button clicked")
