from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # For unique timestamp-based screenshots

class LoginPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")

    def _screenshot(self, step_name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        self.driver.save_screenshot(f"{step_name}_{timestamp}.png")

    # Actions
    def enter_username(self, username):
        element = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        element.send_keys(username)
        self._screenshot("enter_username")

    def enter_password(self, password):
        element = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        element.send_keys(password)
        self._screenshot("enter_password")

    def click_login(self):
        element = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        element.click()
        self._screenshot("click_login")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
