from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self) -> None:
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_press_to_button_add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_product_name_in_basket()
        self.should_be_product_price_in_basket()
        self.should_be_success_message()

    def should_be_product_name(self) -> None:
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME), 'Name of product not presended'
        self.product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text

    def should_be_product_price(self) -> None:
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE), \
                'Price of product not presended'
        self.product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text

    def should_be_press_to_button_add_to_basket(self) -> None:
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_BUTTON_ADD_TO_BASKET
            ), 'Button of add product in basket not presended'
        button_add_to_basket = self.browser.find_element(
            *ProductPageLocators.PRODUCT_BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_product_name_in_basket(self) -> None:
        product_added_to_basket = self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADDED_TO_BASKET).text
        assert product_added_to_basket == self.product_name, \
            'Product name does not match product name in basket'

    def should_be_product_price_in_basket(self) -> None:
        product_price_total_basket = self.browser.find_element(
            *ProductPageLocators.PRODUCT_BASKET_TOTAL_PRICE).text
        assert product_price_total_basket == self.product_price, \
            'The price of the product does not match \
                the total cost of the basket'

    def should_be_success_message(self) -> None:
        success_message_lst = self.browser.find_elements(
            *ProductPageLocators.PRODUCT_BASKET_SUCCESS_MESSAGE)
        assert len(success_message_lst) == 3, 'Success message not presended'

    # Verify that there is no success message using is_not_element_present
    def should_be_cant_see_success_message_after_adding_product_to_basket(self) -> None:
        assert self.is_not_element_present(
            *ProductPageLocators.PRODUCT_BASKET_SUCCESS_MESSAGE), \
                'Success message is presented, but should not be'

    # Check that there is no success message using is_not_element_present
    # without adding the item to the basket
    def should_be_cant_see_success_message(self) -> None:
        assert self.is_not_element_present(
            *ProductPageLocators.PRODUCT_BASKET_SUCCESS_MESSAGE), \
                'Success message is presended, guest cant see success_message'

    # Verify that there is no success message using is_disappeared
    def should_be_message_disappeared_after_adding_product_to_basket(self) -> None:
        assert self.is_disappeared(
            *ProductPageLocators.PRODUCT_BASKET_SUCCESS_MESSAGE), \
                'Saccess message is presended, message disappeared \
                    after adding product to basket'
