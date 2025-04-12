from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        btn.click()

    def should_be_product_name_in_added_to_basket_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_alert = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_ALERT_ADDED_TO_BASKET
        )
        assert (
            product_name.text == product_name_alert.text
        ), "Product name in alert is incorrect"

    def should_be_price_basket_equal_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        assert (
            product_price.text in basket_total.text
        ), "Product price in basket total is incorrect"
