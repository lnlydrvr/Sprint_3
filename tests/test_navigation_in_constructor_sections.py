from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import WebsiteLocators

class TestSectionsNavigation:

    def test_navigation_to_sections(self, driver_chrome, website_urls):
        driver = driver_chrome
        driver.get(website_urls['main_page_url'])
        wait = WebDriverWait(driver, 60)
        
        # Проверяем переход к разделу "Соусы"
        sauces_section_inactive = wait.until(EC.element_to_be_clickable(WebsiteLocators.SAUCES_SECTION_INACTIVE))
        sauces_section_inactive.click()
        sauces_section_active = wait.until(EC.visibility_of_element_located(WebsiteLocators.SAUCES_SECTION_ACTIVE))
        assert 'current' in sauces_section_active.get_attribute('class')

        # Проверяем переход к разделу "Булки"
        buns_section_inactive = wait.until(EC.element_to_be_clickable(WebsiteLocators.BUNS_SECTION_INACTIVE))
        buns_section_inactive.click()
        buns_section_active = wait.until(EC.visibility_of_element_located(WebsiteLocators.BUNS_SECTION_ACTIVE))
        assert 'current' in buns_section_active.get_attribute('class')

        # Проверяем переход к разделу "Начинки"
        stuffings_section_inactive = wait.until(EC.element_to_be_clickable(WebsiteLocators.STUFFINGS_SECTION_INACTIVE))
        stuffings_section_inactive.click()
        stuffings_section_active = wait.until(EC.visibility_of_element_located(WebsiteLocators.STUFFINGS_SECTION_ACTIVE))
        assert 'current' in stuffings_section_active.get_attribute('class')