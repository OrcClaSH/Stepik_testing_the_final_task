from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # product_name = ''
    # product_price = ''

    def should_be_product_page(self):
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_press_to_button_add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_product_name_in_basket()
        self.should_be_product_price_in_basket()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), 'Name of product not presended'
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), 'Price of product not presended'
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_press_to_button_add_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_BUTTON_ADD_TO_BASKET), 'Button of add product in basket not presended'
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_product_name_in_basket(self):
        product_added_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET).text
        assert product_added_to_basket == self.product_name, 'Product name does not match product name in basket'

    def should_be_product_price_in_basket(self):
        product_price_total_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_TOTAL_PRICE).text
        assert product_price_total_basket == self.product_price, 'The price of the product does not match the total cost of the basket'
