from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    account_icon_xpath = '//*[@id="top-links"]/ul/li[2]/a/i'
    login_icon_xpath = '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a'
    email_field_id = 'input-email'
    password_field_id = 'input-password'
    login_button_xpath = '//*[@id="content"]/div/div[2]/div/form/input'
    logged_page_xpath = '//*[@id="content"]/h2[1]'

    def click_account_icon(self):
        self.driver.find_element(By.XPATH, self.account_icon_xpath).click()

    def click_login_icon(self):
        self.driver.find_element(By.XPATH, self.login_icon_xpath).click()

    def navigate_to_login_page(self):
        self.click_account_icon()
        self.click_login_icon()

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_field_id).clear()
        self.driver.find_element(By.ID, self.email_field_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def login_to_application(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        return self.click_login_button()

    def logged_page(self):
        return self.driver.find_element(By.XPATH, self.logged_page_xpath)
