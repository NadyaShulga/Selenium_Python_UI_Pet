import time

from pages.main_page import MainPage


def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('open_login.png')


def test_filter_pet(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_type()
    time.sleep(5)
    browser.save_screenshot('filter_pet_type.png')


def test_filter_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_name()
    time.sleep(5)
    browser.save_screenshot('filter_pet_name.png')


def test_open_details(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.open_details()
    browser.save_screenshot('details.png')


def test_write_comment(browser, login):
    link = 'http://34.141.58.52:8080/#/login'
    page = MainPage(browser, link)
    page.open()
    page.click_logo()
    page.open_details()
    page.write_comment()
    time.sleep(5)
    browser.save_screenshot('comment.png')


def test_like(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.like_pet()
    time.sleep(5)
    browser.save_screenshot('like.png')
