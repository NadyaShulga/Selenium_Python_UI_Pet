import time

from pages.profile_page import ProfilePage
from settings import BASE_URL

base_url_profile = BASE_URL + '/profile'


def test_open_new_card_pet(browser, login):
    page = ProfilePage(browser, base_url_profile)
    page.open()
    page.open_new_card_pet()
    time.sleep(5)
    browser.save_screenshot('../report/create_card.png')


def test_open_edit_card_pet(browser, login):
    page = ProfilePage(browser, base_url_profile)
    page.open()
    page.open_edit_card_pet()
    time.sleep(5)
    browser.save_screenshot('../report/edit_card.png')
