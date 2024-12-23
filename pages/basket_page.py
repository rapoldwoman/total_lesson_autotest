from .base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.common.by import By



class BasketPage(BasePage):
    def should_basket_is_empty(self):
        assert self.browser.find_element(By.XPATH, "//div[@class='container-fluid page']/div[@class='page_inner']/div[@class='content']/div[@id='content_inner']/p").text, "Корзина не пустая"
