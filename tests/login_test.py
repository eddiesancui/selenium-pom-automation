import pytest
from pages.login_page import LoginPage
from data.credentials import USERNAME, PASSWORD

def test_login_dashboard_logout(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(driver)

    # Use credentials from data file
    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    dashboard_page = login_page.click_login()

    assert dashboard_page.is_loaded()

    logout_page = dashboard_page.click_logout()
    assert logout_page.is_returned_to_login()

# Run Pytest in Terminal:
# 	pytest –->> this to run the script
# 	pytest -v -->>> this is to run the script with verbose mode (clear test results)
#   pytest --html=report.html --self-contained-html –->> to run script with report generation