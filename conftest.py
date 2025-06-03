import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    drv = webdriver.Chrome()          # adapt if you use another browser/driver-manager
    drv.maximize_window()
    yield drv
    drv.quit()
