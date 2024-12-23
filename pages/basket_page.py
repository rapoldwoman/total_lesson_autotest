from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        basket_empty = self.browser.find_element(By.XPATH, "//div[@class='container-fluid page']/div[@class='page_inner']/div[@class='content']/div[@id='content_inner']/p").text
        assert ""