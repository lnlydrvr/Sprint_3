import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()