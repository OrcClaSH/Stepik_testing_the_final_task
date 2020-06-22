from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage): 
    # def go_to_login_page(self) -> None:
    #     login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     login_link.click()

    # def should_be_login_link(self) -> None:
    #     assert self.is_element_present(
    #         *MainPageLocators.LOGIN_LINK), 'Login link is not presented'

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
