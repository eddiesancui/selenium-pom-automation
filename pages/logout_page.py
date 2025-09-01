from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    LOGIN_PAGE_HEADER = (By.XPATH, "//h5[text()='Login']")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def is_returned_to_login(self):
        return self.wait.until(EC.visibility_of_element_located(self.LOGIN_PAGE_HEADER)).is_displayed()
