from .base_page import BasePage
from .locators import LoginPageLocators
import faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.url, "Видимо неверный урл"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Логин формы нет"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Регистр формы нет"

    def register_new_user(self):
        f = faker.Faker()
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_EMAIL)
        input_email.send_keys(f.email())
        input_password = self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_PASSWORD1).send_keys(f.password())
        input_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_PASSWORD2)
        input_password2.send_keys(input_password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button.click()
