import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

url_neg = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
base_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=offer"


# @pytest.mark.parametrize('number_offer', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="product name is different {name_product} != {name_product_message}")),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.parametrize('number_offer', [pytest.param(n, marks=pytest.mark.xfail(n == 7,
        reason="product name is different {name_product} != {name_product_message}"))
                                          for n in range(10)])



@pytest.mark.xfail(reason="")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url_neg, 0)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url_neg, 0)
    page.open()
    page.add_to_basket()
    page.should_disappear_of_success_message()

def test_geust_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, url=browser.current_url)
    page.should_be_empty_basket()
    page.should_be_text_basket_is_empty()

class TestUserAddBasketFromProductPage(object):
    pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, url_neg, 0)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser, number_offer):
        # url = number_offer
        url = f"{base_url}{number_offer}"
        page = ProductPage(browser, url)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_added_to_basket()
        page.should_be_name_product_added_to_basket_as_same_name_product_on_product_page()
        page.should_be_cart_price_message()
        page.should_be_cart_prise_as_same_price_product()