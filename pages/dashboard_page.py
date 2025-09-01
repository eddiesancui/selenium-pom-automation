from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    # Locator — assumes a heading or element visible upon login
    DASHBOARD_HEADER = (By.CSS_SELECTOR, ".oxd-topbar-header-title")
    USERDROPDOWN_BUTTON = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    LOGOUT_BUTTON_2 = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def is_loaded(self):
        return self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_HEADER)).is_displayed()

    def click_logout(self):
        # Example: clicking the dropdown and selecting logout
        self.wait.until(EC.element_to_be_clickable(self.USERDROPDOWN_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON_2)).click()
        from pages.logout_page import LogoutPage
        return LogoutPage(self.driver)
