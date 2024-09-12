
from pages.new_pet_page import ProfileNewPetPage
from pages.profile_page import ProfilePage


def test_open_new_card_pet(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.open_new_card_pet()
    page = ProfileNewPetPage(browser, link)
    page.open()
    page.open_new_card_pet()
    page.new_pet_name()
    page.new_pet_age()
    page.new_pet_type()
    page.submit_btn()
    page.add_photo()
    page.submit_add_photo()
    browser.save_screenshot('fill_new_pet_card.png')


