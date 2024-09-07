from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import WebsiteLocators

class TestConstructorNavigation:

    def test_navigation_from_account_to_constructor_via_constructor_button(self, driver_chrome, website_urls, test_user):
        driver = driver_chrome
        driver.get(website_urls['login_page_url'])
        wait = WebDriverWait(driver, 60)

        # Входим в личный кабинет пользователя
        email_input = wait.until(EC.presence_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM))
        email_input.send_keys(test_user['test_user_login'])
        password_input = wait.until(EC.presence_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM))
        password_input.send_keys(test_user['test_user_password'])
        login_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_BUTTON_FORM))
        login_button.click()

        # Переходим на страницу личного кабинета
        wait.until(EC.url_to_be(website_urls['main_page_url']))
        account_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.ACCOUNT_BUTTON))
        account_button.click()
        wait.until(EC.url_to_be(website_urls['profile_page_url']))

        # Кликаем кнопку "Конструктор"
        constructor_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.CONSTRUCTOR_BUTTON))
        constructor_button.click()

        # Ожидаем переход на страницу конструктора
        wait.until(EC.url_to_be(website_urls['main_page_url']))
        constructor_header = wait.until(EC.presence_of_element_located(WebsiteLocators.CONSTRUCTOR_HEADER))
        assert constructor_header.is_displayed()

    def test_navigation_from_account_to_constructor_via_logo(self, driver_chrome, website_urls, test_user):
        driver = driver_chrome
        driver.get(website_urls['login_page_url'])
        wait = WebDriverWait(driver, 60)

        # Входим в личный кабинет пользователя
        email_input = wait.until(EC.presence_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM))
        email_input.send_keys(test_user['test_user_login'])
        password_input = wait.until(EC.presence_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM))
        password_input.send_keys(test_user['test_user_password'])
        login_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_BUTTON_FORM))
        login_button.click()

        # Переходим на страницу личного кабинета
        wait.until(EC.url_to_be(website_urls['main_page_url']))
        account_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.ACCOUNT_BUTTON))
        account_button.click()
        wait.until(EC.url_to_be(website_urls['profile_page_url']))

        # Кликаем на логотип Stellar Burgers
        logo_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.SERVICE_LOGO_BUTTON))
        logo_button.click()

        # Ожидаем переход на страницу конструктора
        wait.until(EC.url_to_be(website_urls['main_page_url']))
        constructor_header = wait.until(EC.presence_of_element_located(WebsiteLocators.CONSTRUCTOR_HEADER))
        assert constructor_header.is_displayed()
