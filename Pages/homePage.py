from selenium.webdriver.common.by import By

from Pages.searchPage import SearchPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # define locators
    search_field_box_name = "search"
    search_button_xpath = '//*[@id="search"]/span/button'

    # define function (action)
    def enter_values_into_search_field(self, product_name):
        self.driver.find_element(By.NAME, self.search_field_box_name).clear()
        self.driver.find_element(By.NAME, self.search_field_box_name).send_keys(product_name)

    def click_search_btn(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)
