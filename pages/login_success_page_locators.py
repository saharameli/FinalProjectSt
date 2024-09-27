from selenium.webdriver.common.by import By

from pages.base_page import BasePage


#index page
class LoginSuccessPageLocators(BasePage):

    LOGIN_SUCCESS_TXT = (By.XPATH, "//marquee[contains(text(), 'Welcome To Customer')]")
    LOGOUT_BTN = (By.XPATH,"//a[@href='Logout.php']")

