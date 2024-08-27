from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def check_product_name(self):
        expected_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_product_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text
        assert expected_product_name == basket_product_name, \
            f"Wrong product in basket name! Expected {expected_product_name}, got {basket_product_name}"

    def check_product_price(self):
        expected_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_product_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert expected_product_price == basket_product_price, \
            f"Wrong basket price! Expected {expected_product_price}, got {basket_product_price}"

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

