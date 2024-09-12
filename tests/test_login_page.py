import time

from pages.login_page import LoginPage
from settings import BASE_URL

base_url_login = BASE_URL + '/login'


def test_go_to_login(browser):
    page = LoginPage(browser, base_url_login)
    page.open()
    page.go_to_login()
    page.go_to_password()
    time.sleep(5)
    page.submit_btn()
    time.sleep(5)
    browser.save_screenshot('../report/login.png')
