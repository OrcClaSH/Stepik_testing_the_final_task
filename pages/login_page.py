from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url[-6:], '"login" is not in url address'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_EMAIL), \
            'Login form email is not presended'
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD), \
            'Login form password is not presended'
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_BUTTON_SUBMIT), \
            'Login form button submit is not presended'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL), \
            'Register form email is not presended'
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASSWORD), \
            'Register form password is not presended'
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD), \
            'Register form confirm password is not presended'
        assert self.is_element_present(*LoginPageLocators.REGISTER_FROM_BUTTON_SUBMIT), \
            'Register form button submit is not presended'
