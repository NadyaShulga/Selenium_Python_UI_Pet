import time

from settings import NEW_PET_NAME, NEW_PET_ADE
from .locators import NewPetPageLocators
from .profile_page import ProfilePage


class ProfileNewPetPage(ProfilePage):

    def new_pet_name(self):
        add_pet_name = self.browser.find_element(*NewPetPageLocators.NAME_NEW_PET)
        add_pet_name.send_keys(NEW_PET_NAME)

    def new_pet_age(self):
        add_pet_age = self.browser.find_element(*NewPetPageLocators.AGE_NEW_PET)
        add_pet_age.send_keys(NEW_PET_ADE)

    def new_pet_type(self):
        self.browser.find_element(*NewPetPageLocators.TYPE_NEW_PET).click()
        self.browser.find_element(*NewPetPageLocators.TYPE_NEW_PET_DOG).click()

    def add_photo(self):
        add_photo = self.browser.find_element(*NewPetPageLocators.ADD_PHOTO)
        add_photo.send_keys('C:\Documents\dog.jpeg')
        time.sleep(10)

    def submit_add_photo(self):
        submit_add_photo = self.browser.find_element(*NewPetPageLocators.SUBMIT_ADD_PHOTO)
        submit_add_photo.click()
