from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # SETUP LOCATORS - I added extra spaces before the "=" in some lines to align the locators.
    # This improves readability and makes the code more visually pleasing.
    # Python is case-sensitive, but it ignores extra spaces around the "=".
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON   = (By.XPATH, "//button[normalize-space()='Login']")
    ERROR_MESSAGE  = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    # In this section, we set up the WebDriver (driver) and a timeout for explicit waits.
    # I recommend using explicit waits so the test waits until specific elements
    # or conditions are loaded before moving to the next step.
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Actions / Behaviors
    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        from pages.dashboard_page import DashboardPage
        return DashboardPage(self.driver)

    # Validation helper
    def is_error_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).is_displayed()