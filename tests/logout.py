import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.home_page import HomePage

LOGIN_URL  = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"   # <-- This is where you put the URL
USERNAME   = "testuser"
PASSWORD   = "testpassword"

@pytest.mark.smoke
def test_login_then_logout(driver):
    driver.get(LOGIN_URL)

    # ---------- Login ----------
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    # ---------- Post-login checks & Logout ----------
    home_page = HomePage(driver)   # constructor already asserts dashboard visibility
    home_page.logout()

    # ---------- Final assertion (redundant but explicit) ----------
    assert driver.find_element(*LoginPage.LOGIN_BUTTON).is_displayed(), \
           "User is not back on the login page after logout"
