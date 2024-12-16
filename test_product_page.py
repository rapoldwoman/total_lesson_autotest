import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time

def test_should_be_product_url(browser):
    print("Проверка, что находимся на странице продукта:")
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_url()

def test_add_product_to_basket(browser):
    print("Проверка добавления продукта в корзину")
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()

def test_should_price_product_in_basket(browser):
    print("Проверка, что продукт добавлен в корзину")
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.should_price_in_basket()

def test_should_name_product_in_notification(browser):
    print("Проверка, что имя продукта в уведомлении верно")
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.should_name_product_in_notification()
