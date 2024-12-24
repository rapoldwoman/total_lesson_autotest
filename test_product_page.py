from .pages.basket_page import BasketPage
import pytest
from .pages.product_page import ProductPage



def test_should_be_product_url(browser):
    print("Проверка, что находимся на странице продукта:")
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_url()

def test_should_price_product_in_basket(browser):
    print("Проверка, что цена продукта добавлена в корзину")
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.should_price_in_basket()

@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_should_name_product_in_notification(browser,url):
    print("Проверка, что имя продукта в уведомлении верно")
    link = f"{url}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.should_name_product_in_notification()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    print("Негатив, Проверка, что нет success massage после добавления в корзину")
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    print("Негатив, Проверка, что сообщение пропадает после добавление в корзину")
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.should_message_disappeared()

def test_guest_should_be_login_link(browser):
    print("Проверяем, что ссылка на логинстраницу есть")
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    print("Проверяем, что можно перейти на логинстраницу")
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.test
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    print("Проверяем, что при переходе в корзину из product_page - корзина пустая")
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser,browser.current_url)
    basket_page.should_basket_is_empty()

class TestUserAddToBasketFromProductPage():
    def test_user_cant_see_success_message(self,browser):
        print("Негатив, Проверка, что гость не видит success message на странице товара")
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_add_product_to_basket(self, browser):
        print("Проверка добавления продукта в корзину")
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_in_basket()