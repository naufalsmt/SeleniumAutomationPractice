import time
from Pages.loginPage import LoginPage
from Pages.responseMessage import ResponseMessage
from Test.base_test import BaseTest


class TestLogin(BaseTest):
    def test_login_by_valid_credential(self):
        login_page = LoginPage(self.driver)
        login_page.navigate_to_login_page()
        login_page.login_to_application('test99@mail.com', '123456')
        time.sleep(2)
        identify_key = login_page.logged_page()
        assert identify_key.is_displayed(), "My Account"

    def test_login_by_invalid_email_valid_password(self):
        login_page = LoginPage(self.driver)
        response_message = ResponseMessage(self.driver)
        login_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_time_stamp(), '123456')
        time.sleep(2)
        login_warning_msg = response_message.login_error_message()
        assert login_warning_msg.is_displayed(), "Warning: No match for E-Mail Address and/or Password."

    def test_login_by_valid_email_invalid_password(self):
        login_page = LoginPage(self.driver)
        response_message = ResponseMessage(self.driver)
        login_page.navigate_to_login_page()
        login_page.login_to_application('test99@mail.com', '12345678')
        time.sleep(2)
        login_warning_msg = response_message.login_error_message()
        assert login_warning_msg.is_displayed(), "Warning: No match for E-Mail Address and/or Password."

    def test_login_by_without_credentials(self):
        login_page = LoginPage(self.driver)
        response_message = ResponseMessage(self.driver)
        login_page.navigate_to_login_page()
        login_page.login_to_application('', '')
        time.sleep(2)
        login_warning_msg = response_message.login_error_message()
        assert login_warning_msg.is_displayed(), "Warning: No match for E-Mail Address and/or Password."

