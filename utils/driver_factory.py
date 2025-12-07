from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def create_driver(browser_name = "chrome"):
    browser_name = browser_name.lower()

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=EdgeService(GeckoDriverManager().install()))

    else:
        raise Exception("browser_name must be 'chrome', 'edge', or 'firefox'")

    driver.maximize_window()
    return driver








