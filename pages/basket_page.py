from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def should_be_cant_see_product_in_basket(self) -> None:
        assert self.is_not_element_present(*BasketLocators.PRODUCT_IN_BASKET),\
            'Product in basket presended, should be cant see product in basket'

    def should_be_basket_is_empty(self) -> None:
        assert self.is_element_present(*BasketLocators.YOUR_BASKET_IS_EMPTY),\
            'Basket is not empty'
