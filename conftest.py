import pytest
from selenium import webdriver

main_page_url = 'https://stellarburgers.nomoreparties.site/'
register_page_url = 'https://stellarburgers.nomoreparties.site/register'
login_page_url = 'https://stellarburgers.nomoreparties.site/login'
forgot_password_page_url = 'https://stellarburgers.nomoreparties.site/forgot-password'
profile_page_url = 'https://stellarburgers.nomoreparties.site/account/profile'

test_user_name = 'Test Testov'
test_user_login = 'test_testov777@inbox.ru'
test_user_password = 'test_testov'

@pytest.fixture(scope='module')
def website_urls():
    return {
        'main_page_url': main_page_url,
        'register_page_url': register_page_url,
        'login_page_url': login_page_url,
        'forgot_password_page_url': forgot_password_page_url,
        'profile_page_url': profile_page_url
    }
    
@pytest.fixture(scope='function')
def test_user():
    return {
        'test_user_name': test_user_name,
        'test_user_login': test_user_login,
        'test_user_password': test_user_password
    }
    
@pytest.fixture(scope='function')
def driver_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()