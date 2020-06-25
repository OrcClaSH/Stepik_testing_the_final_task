from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


number_link_xfail = 7
mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
links = [mask+str(i) for i in range(10) if i != number_link_xfail]
link_xfail = pytest.param(
    mask + str(number_link_xfail), 
    marks=pytest.mark.xfail(reason=f'xfail: Error page {number_link_xfail}')
    )
links.insert(number_link_xfail, link_xfail)

@pytest.mark.need_review
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link) -> None:
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

@pytest.mark.xfail(
    reason='guest cant see success message after adding product to basket'
    )
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_press_to_button_add_to_basket()
    page.should_be_cant_see_success_message_after_adding_product_to_basket()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_cant_see_success_message()

@pytest.mark.xfail(
    reason='test message disappeared after adding product to basket'
    )
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_press_to_button_add_to_basket()
    page.should_be_message_disappeared_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

# 4.3.10 the task
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_cant_see_product_in_basket()
    page.should_be_basket_is_empty()


# 4.3.13 the task
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        login_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        email = str(time.time()) + '@fakemail.org'
        password = '123Test123'
        self.page = LoginPage(browser, login_link)
        self.page.open()
        # Additional verification of the registration form before 
        # user registration
        self.page.should_be_register_form()
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser) -> None:
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_cant_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser) -> None:
        # Promotion link for verification
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
