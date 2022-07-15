
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '[value="Add to basket"]')
    ADDED_TO_BASKET = (By.CSS_SELECTOR, '#messages > :nth-child(1) > .alertinner')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6 h1')
    NAME_PRODUCT_MESSAGE = (By.CSS_SELECTOR, '#messages > :nth-child(1) > .alertinner > :nth-child(1)')
    CART_PRICE_MESSAGE = (By.CSS_SELECTOR, '#messages > :nth-child(3) > .alertinner > :nth-child(1)')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'p.price_color')
    CART_PRICE = (By.CSS_SELECTOR, '#messages > :nth-child(3) > .alertinner > :nth-child(1) > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > :nth-child(1)')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")