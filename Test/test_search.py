import time
from Pages.homePage import HomePage
from Test.base_test import BaseTest


class TestSearch(BaseTest):
    def test_search_by_valid_keyword(self):
        home_page = HomePage(self.driver)
        home_page.enter_values_into_search_field('HP')
        search_page = home_page.click_search_btn()
        time.sleep(3)
        assert search_page.valid_product_name_displaying()
        time.sleep(3)

    def test_search_by_invalid_keyword(self):
        home_page = HomePage(self.driver)
        home_page.enter_values_into_search_field('HONDA')
        home_page.click_search_btn()
        time.sleep(3)
        expected_result = 'There is no product that matches the search criteria.'
        page_source = self.driver.page_source
        assert expected_result in page_source
        time.sleep(3)

    def test_search_without_keyword(self):
        home_page = HomePage(self.driver)
        home_page.enter_values_into_search_field('')
        home_page.click_search_btn()
        time.sleep(3)
        expected_result = 'There is no product that matches the search criteria.'
        page_source = self.driver.page_source
        assert expected_result in page_source
        time.sleep(3)
