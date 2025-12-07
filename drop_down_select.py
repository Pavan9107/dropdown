import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)
driver.get("https://www.amazon.in/")
dropdown_element = driver.find_element(By.ID, "searchDropdownBox")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Books")
time.sleep(3)

selected_option = dropdown.first_selected_option.text
assert selected_option == "Books"

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("python")

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.s-suggestion")))

suggestions = driver.find_elements(By.CSS_SELECTOR, "div.s-suggestion")
for suggestion in suggestions:
    if suggestion.get_attribute("aria-label") == "python book":
        suggestion.click()
        time.sleep(5)
        break


wait.until(EC.visibility_of_element_located((By.XPATH, "//a[h2/span[contains(text(),'Python All-in-One for Dummies')]]")))


book_link = driver.find_element(By.XPATH, "//a[h2/span[contains(text(),'Python All-in-One for Dummies')]]")
print("Book URL:", book_link.get_attribute("href"))
book_link.click()


windows = driver.window_handles
print("Windows:", windows)

driver.switch_to.window(windows[1])
print(driver.current_url)





