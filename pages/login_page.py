from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    USERNAME_INPUT = (By.ID, "Admin")
    PASSWORD_INPUT = (By.ID, "admin123")
    LOGIN_BUTTON   = (By.ID, "loginBtn")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait   = WebDriverWait(driver, timeout)

    def enter_username(self, username: str):
        el = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        el.clear(); el.send_keys(username)
        assert el.get_attribute("value") == username, "Username input failed"
        
    def enter_password(self, password: str):
        el = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        el.clear(); el.send_keys(password)
        assert el.get_attribute("value") == password, "Password input failed"

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        assert self.wait.until(EC.invisibility_of_element_located(self.LOGIN_BUTTON)), \
               "Login button still visible after click"

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
