from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
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

@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link) -> None:
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    # time.sleep(5)
