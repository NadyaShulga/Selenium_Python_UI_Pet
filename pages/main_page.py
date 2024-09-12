from settings import PET_NAME, COMMENT
from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser, link):
        super().__init__(browser, link)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def filter_by_type(self):
        filter_type = self.browser.find_element(*MainPageLocators.FILTER_TYPE)
        filter_type.click()
        filter_type_cat = self.browser.find_element(*MainPageLocators.FILTER_TYPE_CAT)
        filter_type_cat.click()

    def filter_by_name(self):
        filter_name = self.browser.find_element(*MainPageLocators.FILTER_PET_NAME)
        filter_name.send_keys(PET_NAME)
        filter_name.click()

    def open_details(self):
        details_btn = self.browser.find_element(*MainPageLocators.DETAILS_BTN)
        details_btn.click()

    def write_comment(self):
        text_area = self.browser.find_element(*MainPageLocators.TEXT_AREA)
        text_area.send_keys(COMMENT)
        save_comment = self.browser.find_element(*MainPageLocators.SUBMIT_BTN)
        save_comment.click()

    def like_pet(self):
        like_btn = self.browser.find_element(*MainPageLocators.LIKE_BTN)
        like_btn.click()

    def click_logo(self):
        logo = self.browser.find_element(*MainPageLocators.LOGO)
        logo.click()
