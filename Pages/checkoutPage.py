from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Checkout:
    def __init__(self, driver):
        self.driver = driver

    checkout_link_text = "Checkout"
    checkout_page_xpath = '//*[@id="content"]/h1'
    shipping_detail_xpath = '//*[@id="accordion"]/div[2]/div[1]/h4/a'
    input_country_id = 'input-country'
    input_region_id = 'input-zone'
    input_postal_code_id = 'input-postcode'
    quote_btn_id = 'button-quote'
    shipping_method_rd_btn_name = 'shipping_method'
    shipping_price_xpath = '//*[@id="modal-shipping"]/div/div/div[2]/div/label'
    apply_shipping_btn_id = 'button-shipping'
    checkout_shipping_price_xpath = '//*[@id="content"]/div[2]/div/table/tbody/tr[2]/td[2]'
    table_section_xpath = '//*[@id="content"]/h2'

    # checkout function calls

    def click_checkout_link(self):
        self.driver.find_element(By.LINK_TEXT, self.checkout_link_text).click()

    def checkout_page_title(self):
        return self.driver.find_element(By.XPATH, self.checkout_page_xpath)

    def click_shipping_tap(self):
        element = self.driver.find_element(By.XPATH, self.shipping_detail_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def select_country(self):
        dropdown_country = self.driver.find_element(By.ID, self.input_country_id)
        select = Select(dropdown_country)
        country_to_select = '99'
        select.select_by_value(country_to_select)

    def select_region(self):
        dropdown_region = self.driver.find_element(By.ID, self.input_region_id)
        select = Select(dropdown_region)
        region_to_select = '1484'
        select.select_by_value(region_to_select)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(By.ID, self.input_postal_code_id).send_keys(postal_code)

    def click_quote_btn(self):
        self.driver.find_element(By.ID, self.quote_btn_id).click()

    def click_shipping_method_radio_btn(self):
        self.driver.find_element(By.NAME, self.shipping_method_rd_btn_name).click()

    def return_shipping_price(self):
        return self.driver.find_element(By.XPATH, self.shipping_price_xpath).text

    def click_apply_shipping_btn(self):
        self.driver.find_element(By.ID, self.apply_shipping_btn_id).click()

    def navigate_to_table(self):
        table_section = self.driver.find_element(By.XPATH, self.table_section_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", table_section)

    def return_checkout_shipping_price(self):
        return self.driver.find_element(By.XPATH, self.checkout_shipping_price_xpath).text





