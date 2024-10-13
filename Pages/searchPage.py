from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    product_name_link_text = 'HP LP3065'

    def valid_product_name_displaying(self):
        return self.driver.find_element(By.LINK_TEXT, self.product_name_link_text).is_displayed
