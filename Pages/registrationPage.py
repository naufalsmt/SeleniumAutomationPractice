from selenium.webdriver.common.by import By


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    registration_option_link_text = 'Register'
    registration_page_text_xpath = '//*[@id="content"]/h1'

    first_name_field_id = 'input-firstname'
    last_name_field_id = 'input-lastname'
    email_field_id = 'input-email'
    phone_number_field_id = 'input-telephone'
    password_field_id = 'input-password'
    confirm_password_field_id = 'input-confirm'
    checkbox_xpath = '//*[@id="content"]/form/div/div/input[1]'
    continue_button_xpath = '//*[@id="content"]/form/div/div/input[2]'
    continue_link_text = 'Continue'

    def click_registration_icon(self):
        self.driver.find_element(By.LINK_TEXT, self.registration_option_link_text).click()

    def registration_page_text(self):
        self.driver.find_element(By.XPATH, self.registration_page_text_xpath)

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.first_name_field_id).clear()
        self.driver.find_element(By.ID, self.first_name_field_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.last_name_field_id).clear()
        self.driver.find_element(By.ID, self.last_name_field_id).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_field_id).clear()
        self.driver.find_element(By.ID, self.email_field_id).send_keys(email)

    def enter_phone_number(self, phone_number):
        self.driver.find_element(By.ID, self.phone_number_field_id).clear()
        self.driver.find_element(By.ID, self.phone_number_field_id).send_keys(phone_number)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.ID, self.confirm_password_field_id).clear()
        self.driver.find_element(By.ID, self.confirm_password_field_id).send_keys(confirm_password)

    def checked_checkbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_xpath)

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def click_continue_link(self):
        self.driver.find_element(By.LINK_TEXT, self.continue_link_text).click()

    def fill_the_registration_form(self, first_name, last_name, email, phone_number, password, confirm_password):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_phone_number(phone_number)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
