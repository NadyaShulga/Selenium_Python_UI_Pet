from settings import VALID_EMAIL, VALID_PASSWORD
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(VALID_EMAIL)

    def go_to_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(VALID_PASSWORD)

    def submit_btn(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN).submit()
