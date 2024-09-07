from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import WebsiteLocators

class TestUserLogin:

    def test_login_via_account_button(self, driver_chrome, website_urls, test_user):
        driver = driver_chrome
        driver.get(website_urls['main_page_url'])
        wait = WebDriverWait(driver, 60)

        # Ожидаем и кликаем кнопку "Войти в аккаунт"
        account_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_INTO_ACCOUNT_BUTTON))
        account_button.click()

        # Ожидаем переход на страницу входа
        wait.until(EC.url_to_be(website_urls['login_page_url']))

        # Вводим email для входа в поле
        email_input = wait.until(EC.presence_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM))
        email_input.send_keys(test_user['test_user_login'])

        # Вводим пароль для входа в поле
        password_input = wait.until(EC.presence_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM))
        password_input.send_keys(test_user['test_user_password'])

        # Нажимаем кнопку "Войти"
        login_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_BUTTON_FORM))
        login_button.click()

        # Ожидаем, что кнопка "Оформить заказ" появится на главной странице
        make_order_button = wait.until(EC.presence_of_element_located(WebsiteLocators.MAKE_ORDER_BUTTON))
        assert make_order_button.is_displayed()
    
    def test_login_via_account_button_in_header(self, driver_chrome, website_urls, test_user):
        driver = driver_chrome
        driver.get(website_urls['main_page_url'])
        wait = WebDriverWait(driver, 60)

        # Ожидаем и кликаем кнопку "Личный Кабинет"
        account_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.ACCOUNT_BUTTON))
        account_button.click()

        # Ожидаем переход на страницу входа
        wait.until(EC.url_to_be(website_urls['login_page_url']))

        # Вводим email для входа в поле
        email_input = wait.until(EC.presence_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM))
        email_input.send_keys(test_user['test_user_login'])

        # Вводим пароль для входа в поле
        password_input = wait.until(EC.presence_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM))
        password_input.send_keys(test_user['test_user_password'])

        # Нажимаем кнопку "Войти"
        login_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_BUTTON_FORM))
        login_button.click()

        # Ожидаем, что кнопка "Оформить заказ" появится на главной странице
        make_order_button = wait.until(EC.presence_of_element_located(WebsiteLocators.MAKE_ORDER_BUTTON))
        assert make_order_button.is_displayed()
    
    def test_login_via_registration_form(self, driver_chrome, website_urls, test_user):
        driver = driver_chrome
        driver.get(website_urls['register_page_url'])
        wait = WebDriverWait(driver, 60)

        # Нажимаем кнопку-ссылку "Войти"
        login_text_link = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_TEXT_LINK))
        login_text_link.click()

        # Ожидаем переход на страницу входа
        wait.until(EC.url_to_be(website_urls['login_page_url']))

        # Вводим email для входа в поле
        email_input = wait.until(EC.presence_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM))
        email_input.send_keys(test_user['test_user_login'])

        # Вводим пароль для входа в поле
        password_input = wait.until(EC.presence_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM))
        password_input.send_keys(test_user['test_user_password'])

        # Нажимаем кнопку "Войти"
        login_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_BUTTON_FORM))
        login_button.click()

        # Ожидаем, что кнопка "Оформить заказ" появится на главной странице
        make_order_button = wait.until(EC.presence_of_element_located(WebsiteLocators.MAKE_ORDER_BUTTON))
        assert make_order_button.is_displayed()
        
    def test_login_via_forgot_password_form(self, driver_chrome, website_urls, test_user):
        driver = driver_chrome
        driver.get(website_urls['forgot_password_page_url'])
        wait = WebDriverWait(driver, 60)
        
        # Ожидаем и нажимаем кнопку-ссылку "Войти"
        login_text_link = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_TEXT_LINK))
        login_text_link.click()

        # Ожидаем переход на страницу входа
        wait.until(EC.url_to_be(website_urls['login_page_url']))

        # Вводим email для входа в поле
        email_input = wait.until(EC.presence_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM))
        email_input.send_keys(test_user['test_user_login'])

        # Вводим пароль для входа в поле
        password_input = wait.until(EC.presence_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM))
        password_input.send_keys(test_user['test_user_password'])

        # Нажимаем кнопку "Войти"
        login_button = wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_BUTTON_FORM))
        login_button.click()

        # Ожидаем, что кнопка "Оформить заказ" появится на главной странице
        make_order_button = wait.until(EC.presence_of_element_located(WebsiteLocators.MAKE_ORDER_BUTTON))
        assert make_order_button.is_displayed()