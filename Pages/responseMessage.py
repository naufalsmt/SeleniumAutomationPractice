from selenium.webdriver.common.by import By


class ResponseMessage:
    def __init__(self, driver):
        self.driver = driver

    no_product_search_message_xpath = '//*[@id="content"]/p[2]'
    login_error_message_xpath = '//*[@id="account-login"]/div[1]'
    registration_response_success_xpath = '//*[@id="content"]/h1'
    missed_checkbox_warning_message_xpath = '//*[@id="account-register"]/div[1]'
    f_name_validation_message_xpath = '//*[@id="account"]/div[2]/div/div'
    email_exist_warning_xpath = '//*[@id="account-register"]/div[1]'

    def no_product_search_message(self):
        self.driver.find_element(By.XPATH, self.no_product_search_message_xpath)

    def login_error_message(self):
        return self.driver.find_element(By.XPATH, self.login_error_message_xpath)

    def registration_success_message(self):
        self.driver.find_element(By.XPATH, self.registration_response_success_xpath)

    def checkbox_missed_warning_text(self):
        self.driver.find_element(By.XPATH, self.missed_checkbox_warning_message_xpath)

    def f_name_validation_message_text(self):
        self.driver.find_element(By.XPATH, self.f_name_validation_message_xpath)

    def email_existing_warning_text(self):
        self.driver.find_element(By.XPATH, self.email_exist_warning_xpath)
