import time
import unittest
from Pages.addToCartPage import AddToCart
from Pages.loginPage import LoginPage
from Pages.checkoutPage import Checkout
from Pages.responseMessage import ResponseMessage
from Test.base_test import BaseTest
from Utilities import ExcelLoginData

import pytest


class TestCartProduct(BaseTest):
    @pytest.mark.parametrize(
        "email, password", ExcelLoginData.get_login_data('ExcelFiles/loginData.xlsx', 'UserData')
    )
    def test_add_to_cart(self, email, password):
        lp = LoginPage(self.driver)
        ac = AddToCart(self.driver)
        lp.navigate_to_login_page()
        lp.login_to_application(email, password)
        time.sleep(2)
        ac.click_menu()
        ac.click_mac_option()
        time.sleep(2)
        ac.navigate_to_product()
        time.sleep(2)
        ac.click_add_to_cart()
        time.sleep(2)
        ac.navigate_to_cart_btn_and_click_on_it()
        time.sleep(2)
        cart_item = ac.cart_product_text()
        assert cart_item.is_displayed()

    @pytest.mark.parametrize(
        "email, password", ExcelLoginData.get_login_data('ExcelFiles/loginData.xlsx', 'UserData')
    )
    def test_checkout_from_cart(self, email, password):
        lp = LoginPage(self.driver)
        ac = AddToCart(self.driver)
        ch = Checkout(self.driver)
        rm = ResponseMessage(self.driver)
        lp.navigate_to_login_page()
        lp.login_to_application(email, password)
        time.sleep(2)
        ac.navigate_to_cart_btn_and_click_on_it()

        ch.click_checkout_link()
        time.sleep(2)
        checkout_product_name = ch.return_checkout_product_name()
        # product_status_response = rm.return_checkout_product_status_response()
        checkout_title = ch.checkout_page_title()
        assert checkout_title.is_displayed()

        ch.click_shipping_tap()
        time.sleep(2)
        ch.select_country()
        time.sleep(2)
        ch.select_region()
        time.sleep(2)
        ch.enter_postal_code("1234567")
        time.sleep(2)
        ch.click_quote_btn()
        time.sleep(2)
        popup_shipping = ch.return_shipping_price()
        ch.click_shipping_method_radio_btn()
        time.sleep(2)
        ch.click_apply_shipping_btn()
        time.sleep(2)

        ch.navigate_to_table()
        time.sleep(2)
        checkout_shipping = ch.return_checkout_shipping_price()
        assert checkout_shipping not in popup_shipping, f"{checkout_shipping} is not found in {popup_shipping}"

        ch.click_checkout_btn()
        time.sleep(2)
        assert '***' in checkout_product_name, \
            "Products marked with *** are not available in the desired quantity or not in stock!"




