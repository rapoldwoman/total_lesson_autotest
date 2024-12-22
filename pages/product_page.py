from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By




class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_button_add_to_basket()
        self.should_be_product_name()

    def should_be_product_url(self):
        assert "/catalogue/" in self.url, "Неверный урл"

    def should_be_button_add_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.BUTTON_ADD), "Кнопки добавить в корзину - нет"

    def should_be_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)

    def add_product_in_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button_add.click()
        self.solve_quiz_and_get_code()

    def should_price_in_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price == self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text, "Сумма в корзине отличается"

    def should_name_product_in_notification(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert name_product == self.browser.find_element(*ProductPageLocators.NAME_IN_ALERTINNER).text, "Название добавлено не то"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MASSAGES_PRODUCT), "Success message is presented, but should not be"