import time

from pages.profile_page import ProfilePage


def test_edit_name_pet(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.open_edit_card_pet()
    time.sleep(5)
    page.edit_pet_name()
    browser.save_screenshot('edit_card_name_pet.png')


def test_edit_age_pet(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.open_edit_card_pet()
    time.sleep(5)
    page.edit_pet_age()
    browser.save_screenshot('edit_card_age_pet.png')
