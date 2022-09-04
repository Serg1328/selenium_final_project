from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), \
            'basket NOT empty'


    def should_be_text_basket_is_empty(self):
        assert 'empty' in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text, \
            "NO messege 'basket is empty'"