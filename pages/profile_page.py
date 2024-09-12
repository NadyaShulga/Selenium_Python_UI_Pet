from settings import EDIT_PET_NAME, EDIT_PET_AGE
from .locators import ProfilePageLocators
from .login_page import LoginPage


class ProfilePage(LoginPage):
    def open_new_card_pet(self):
        add_new_pet = self.browser.find_element(*ProfilePageLocators.ADD_PET).click()

    def open_edit_card_pet(self):
        edit_card_pet = self.browser.find_element(*ProfilePageLocators.EDIT_PET).click()

    def edit_pet_name(self):
        new_pet_name = self.browser.find_element(*ProfilePageLocators.NAME_PET)
        new_pet_name.clear()
        new_pet_name.send_keys(EDIT_PET_NAME)

    def edit_pet_age(self):
        new_pet_age = self.browser.find_element(*ProfilePageLocators.AGE_PET)
        new_pet_age.clear()
        new_pet_age.send_keys(EDIT_PET_AGE)
