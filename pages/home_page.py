from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    DASHBOARD = (By.ID, "dashboard")   # Visible after successful login
    LOGOUT_BUTTON = (By.ID, "logoutBtn")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait   = WebDriverWait(driver, timeout)
        # Ensure we really are on the home/dashboard page
        assert self.wait.until(EC.visibility_of_element_located(self.DASHBOARD)), \
               "Dashboard element not visible; not on Home page"

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()
        # Assert that login page is visible again
        from pages.login_page import LoginPage   # local import avoids circular dependency
        assert self.wait.until(
            EC.visibility_of_element_located(LoginPage.LOGIN_BUTTON)
        ), "Login button not visible after logout"

#good morning.