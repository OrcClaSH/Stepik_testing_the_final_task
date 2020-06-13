from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_FORM_BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_FROM_BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

