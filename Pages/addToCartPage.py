import time

from selenium.webdriver.common.by import By


class AddToCart:
    def __init__(self, driver):
        self.driver = driver

    desktop_xpath = '//*[@id="menu"]/div[2]/ul/li[1]/a'
    mac_option_xpath = '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a'
    mac_link_text = 'iMac'
    add_to_cart_icon_xpath = '//*[@id="content"]/div[2]/div/div/div[2]/div[2]/button[1]'
    cart_button_xpath = '//*[@id="cart"]/button'
    cart_product_link_text = 'iMac'

    # add to cart function class

    def click_menu(self):
        self.driver.find_element(By.XPATH, self.desktop_xpath).click()

    def click_mac_option(self):
        self.driver.find_element(By.XPATH, self.mac_option_xpath).click()

    def navigate_to_product(self):
        element = self.driver.find_element(By.LINK_TEXT, self.mac_link_text)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_add_to_cart(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_icon_xpath).click()

    def navigate_to_cart_btn_and_click_on_it(self):
        cart_button = self.driver.find_element(By.XPATH, self.cart_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", cart_button)
        time.sleep(2)
        cart_button.click()

    def click_on_cart_button(self):
        self.driver.find_element(By.XPATH, self.cart_button_xpath).click()

    def cart_product_text(self):
        return self.driver.find_element(By.LINK_TEXT, self.cart_product_link_text)
