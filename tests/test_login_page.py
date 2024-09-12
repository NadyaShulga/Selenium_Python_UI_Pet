import time

from pages.login_page import LoginPage


def test_go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    time.sleep(5)
    page.submit_btn()
    time.sleep(5)
    browser.save_screenshot('login.png')

