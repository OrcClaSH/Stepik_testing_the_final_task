from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Validation url address
        assert 'login' in self.browser.current_url[-6:], \
            '"login" is not in url address'

    def should_be_login_form(self):
        # We verify that there is a login form
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM_EMAIL
            ), 'Login form email is not presended'
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM_PASSWORD
            ), 'Login form password is not presended'
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM_BUTTON_SUBMIT
            ), 'Login form button submit is not presended'

    def should_be_register_form(self):
        # We check that there is a registration form on the page
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM_EMAIL
            ), 'Register form email is not presended'
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM_PASSWORD
            ), 'Register form password is not presended'
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD
            ), 'Register form confirm password is not presended'
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FROM_BUTTON_SUBMIT
            ), 'Register form button submit is not presended'

    def register_new_user(self, email, password):
        register_email = self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_EMAIL
            )
        register_email.send_keys(email)

        register_password = self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_PASSWORD
            )
        register_password.send_keys(password)

        register_confirm_password = self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD
            )
        register_confirm_password.send_keys(password)

        register_button = self.browser.find_element(
            *LoginPageLocators.REGISTER_FROM_BUTTON_SUBMIT
            )
        register_button.click()
