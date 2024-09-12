import time

from pages.profile_page import ProfilePage
from settings import BASE_URL

base_url_profile = BASE_URL + '/profile'


def test_edit_name_pet(browser, login):
    page = ProfilePage(browser, base_url_profile)
    page.open()
    page.open_edit_card_pet()
    time.sleep(5)
    page.edit_pet_name()
    browser.save_screenshot('../report/edit_card_name_pet.png')


def test_edit_age_pet(browser, login):
    page = ProfilePage(browser, base_url_profile)
    page.open()
    page.open_edit_card_pet()
    time.sleep(5)
    page.edit_pet_age()
    browser.save_screenshot('../report/edit_card_age_pet.png')
