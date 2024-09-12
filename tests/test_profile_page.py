import time

from pages.profile_page import ProfilePage


def test_open_new_card_pet(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.open_new_card_pet()
    time.sleep(5)
    browser.save_screenshot('create_card.png')


def test_open_edit_card_pet(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.open_edit_card_pet()
    time.sleep(5)
    browser.save_screenshot('edit_card.png')