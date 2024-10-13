import time
from Pages.loginPage import LoginPage
from Pages.registrationPage import RegistrationPage
from Pages.responseMessage import ResponseMessage
from Test.base_test import BaseTest


class TestRegistration(BaseTest):
    def test_registration_form_with_all_mandatory_field(self):
        lp = LoginPage(self.driver)
        rp = RegistrationPage(self.driver)
        rm = ResponseMessage(self.driver)

        lp.click_account_icon()
        rp.click_registration_icon()

        page_text = rp.registration_page_text().text
        assert page_text.is_displayed

        rp.fill_the_registration_form('John', 'Abraham', self.generate_email_with_time_stamp(),
                                      '0989812334', '909090', '909090')
        checked_checkbox = rp.checked_checkbox()
        if not checked_checkbox.is_selected():
            checked_checkbox.click()
        rp.click_continue_button()
        response_text = rm.registration_success_message().text
        assert response_text.is_displayed
        time.sleep(3)

        rp.click_continue_link()
        identify_key = lp.logged_page().text
        assert identify_key.is_displayed()
        time.sleep(3)

    def test_registration_form_without_checked(self):
        lp = LoginPage(self.driver)
        rp = RegistrationPage(self.driver)
        rm = ResponseMessage(self.driver)

        lp.click_account_icon()
        rp.click_registration_icon()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll to bottom
        rp.click_continue_button()
        response_text = rm.checkbox_missed_warning_text().text
        assert response_text.is_displayed
        time.sleep(3)

    def test_registration_form_checked_without_response(self):
        lp = LoginPage(self.driver)
        rp = RegistrationPage(self.driver)

        lp.click_account_icon()
        rp.click_registration_icon()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll to bottom
        checked_checkbox = rp.checked_checkbox()
        if not checked_checkbox.is_selected():
            checked_checkbox.click()
        rp.click_continue_button()
        response_text = 'Warning: You must agree to the Privacy Policy!'
        page_source = self.driver.page_source
        assert response_text not in page_source
        time.sleep(3)

    def test_registration_form_with_checked_and_without_any_mandatory_field(self):
        lp = LoginPage(self.driver)
        rp = RegistrationPage(self.driver)
        rm = ResponseMessage(self.driver)

        lp.click_account_icon()
        rp.click_registration_icon()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll to bottom
        checked_checkbox = rp.checked_checkbox()
        if not checked_checkbox.is_selected():
            checked_checkbox.click()
        rp.click_continue_button()
        f_name_validation = rm.f_name_validation_message_text().text
        assert f_name_validation.is_displayed
        time.sleep(3)

    def test_registration_form_with_email_id_already_used_before(self):
        lp = LoginPage(self.driver)
        rp = RegistrationPage(self.driver)
        rm = ResponseMessage(self.driver)

        lp.click_account_icon()
        rp.click_registration_icon()

        rp.fill_the_registration_form('John', 'Abraham', 'test99@mail.com',
                                      '0989812334', '909090', '909090')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll to bottom
        checked_checkbox = rp.checked_checkbox()
        if not checked_checkbox.is_selected():
            checked_checkbox.click()
        rp.click_continue_button()
        email_warning_validation = rm.email_existing_warning_text().text
        assert email_warning_validation.is_displayed
        time.sleep(3)
