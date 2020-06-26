from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_FORM_BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_CONFIRM_PASSWORD = (
        By.CSS_SELECTOR,
        '#id_registration-password2'
        )
    REGISTER_FROM_BUTTON_SUBMIT = (
        By.CSS_SELECTOR,
        'button[name="registration_submit"]'
        )


class ProductPageLocators():
    PRODUCT_BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_ADDED_TO_BASKET = (
        By.CSS_SELECTOR,
        '#messages div:nth-child(1) strong'
        )
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_BASKET_TOTAL_PRICE = (
        By.CSS_SELECTOR,
        '.alert-info .alertinner strong'
        )
    PRODUCT_BASKET_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-default[href]:nth-child(1)')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketLocators():
    BASKET_BUTTON_ORDER = (By.CSS_SELECTOR, '.btn-block')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, 'col-sm-6 h3')
    YOUR_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
