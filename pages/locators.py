from selenium.webdriver.common.by import By



class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, '[value="Log In"]')
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_INPUT_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_INPUT_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, '[value="Register"]')

class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERTINNER = (By.CSS_SELECTOR, ".alertinner")
    NAME_PRODUCT = (By.TAG_NAME, "h1")
    MASSAGES_PRODUCT = (By.CSS_SELECTOR, "#massage")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, ".basket-mini")