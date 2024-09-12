
from pages.new_pet_page import ProfileNewPetPage
from pages.profile_page import ProfilePage
from settings import BASE_URL

base_url_profile = BASE_URL + '/profile'


def test_open_new_card_pet(browser, login):
    page = ProfilePage(browser, base_url_profile)
    page.open()
    page.open_new_card_pet()
    page = ProfileNewPetPage(browser, base_url_profile)
    page.open()
    page.open_new_card_pet()
    page.new_pet_name()
    page.new_pet_age()
    page.new_pet_type()
    page.submit_btn()
    page.add_photo()
    page.submit_add_photo()
    browser.save_screenshot('../report/fill_new_pet_card.png')


