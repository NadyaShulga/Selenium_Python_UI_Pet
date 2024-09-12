import time

from pages.main_page import MainPage
from settings import BASE_URL

base_url_main = BASE_URL + '/'
base_url_login = BASE_URL + '/login'


def test_go_to_login_page(browser):
    page = MainPage(browser, base_url_main)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('../report/open_login.png')


def test_filter_pet(browser):
    page = MainPage(browser, base_url_main)
    page.open()
    page.filter_by_type()
    time.sleep(5)
    browser.save_screenshot('../report/filter_pet_type.png')


def test_filter_name(browser):
    page = MainPage(browser, base_url_main)
    page.open()
    page.filter_by_name()
    time.sleep(5)
    browser.save_screenshot('../report/filter_pet_name.png')


def test_open_details(browser):
    page = MainPage(browser, base_url_main)
    page.open()
    page.open_details()
    browser.save_screenshot('../report/details.png')


def test_write_comment(browser, login):
    page = MainPage(browser, base_url_login)
    page.open()
    page.click_logo()
    page.open_details()
    page.write_comment()
    time.sleep(5)
    browser.save_screenshot('../report/comment.png')


def test_like(browser):
    page = MainPage(browser, base_url_main)
    page.open()
    page.like_pet()
    time.sleep(5)
    browser.save_screenshot('../report/like.png')
