from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    FILTER_TYPE = (By.XPATH, '//*[@id="typesSelector"]')
    FILTER_TYPE_CAT = (By.ID, "pv_id_2_1")
    FILTER_PET_NAME = (By.CSS_SELECTOR, 'input#petName')
    DETAILS_BTN = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/button')
    LIKE_BTN = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[2]/span[1]/i')
    TEXT_AREA = (
        By.XPATH, '//*[@id="app"]/main[1]/div[2]/div[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[2]/div[1]/p[1]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[2]/div[1]/div[1]/div[3]/form[1]/div[1]/button[1]')
    LOGO = (By.XPATH, '//*[@id="app"]/header/div/div/img')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    ADD_PET = (By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[1]/button')
    EDIT_PET = (
        By.CSS_SELECTOR,
        'div#app > main > div > div > div:nth-of-type(2) > div > div > div > div:nth-of-type(2) > button')
    DELETE_PET = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[2]')
    NAME_PET = (By.XPATH, '//*[@id="name"]')
    AGE_PET = (By.XPATH, '//*[@id="age"]/input[1]')


class NewPetPageLocators:
    NAME_NEW_PET = (By.XPATH, '//*[@id="name"]')
    AGE_NEW_PET = (By.XPATH, '//*[@id="age"]/input[1]')
    TYPE_NEW_PET = (By.ID, 'typeSelector')
    TYPE_NEW_PET_DOG = (By.XPATH, '/html/body/div[3]/div/ul/li[1]')
    GENDER_NEW_PET = (By.XPATH, '//*[@id="genderSelector"]')
    GENDER_NEW_PET_FEMALE = (By.XPATH, '//*[@id="pv_id_3_1"]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    # CHOOSE_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span[1]/span[2]')
    # FILE_PATH = (By.XPATH, "//input[@type='file']")
    ADD_PHOTO = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/input')
    SUBMIT_ADD_PHOTO = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span')