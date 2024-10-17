import time
import pytest
from Pages.loginPage import LoginPage
from Pages.responseMessage import ResponseMessage
from Test.base_test import BaseTest
from Utilities import ExcelUtils


class TestLogin(BaseTest):
    # passing the excell file data to the login fields
    @pytest.mark.parametrize("email_address, password",
                             ExcelUtils.get_data_from_excel(
                                 'ExcelFiles/loginfile.xlsx',
                                 'LoginPage')
                             )
    def test_login_by_valid_credential(self, email_address, password):
        login_page = LoginPage(self.driver)
        login_page.navigate_to_login_page()
        login_page.login_to_application(email_address, password)
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

