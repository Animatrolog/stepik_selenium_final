from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini span>a")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner>p>strong")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")


class BasketPageLocators:
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner>p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
