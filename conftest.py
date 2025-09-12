import pytest
from selenium import webdriver

# This is where the setting up of the driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
