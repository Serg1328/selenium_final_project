from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()


    def should_be_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET), "product not added"

    def should_be_name_product_added_to_basket_as_same_name_product_on_product_page(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_product_message = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_MESSAGE).text
        assert name_product == name_product_message, f"product name is different name_product = {name_product}, name_product_message={name_product_message}"

    def should_be_cart_price_message(self):
        assert self.is_element_present(*ProductPageLocators.CART_PRICE_MESSAGE), "no add to cart prise message"

    def should_be_cart_prise_as_same_price_product(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        assert price_product == cart_price, "cart price differs from price on product page"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should have disappeared"


