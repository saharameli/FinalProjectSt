from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_success_page_locators import LoginSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL, LOGIN_SUCCESS_MESSAGE_TEXT, MINI_ST_BTN_TEXT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#index page
class LoginSuccessPage(BasePage):


    def is_login_success(self):
        try:
            login_success_label = WebDriverWait(self.driver, MAX_WAIT_INTERVAL).until(
                EC.visibility_of_element_located(LoginSuccessPageLocators.LOGIN_SUCCESS_TXT)
            )
            return login_success_label.text
        except TimeoutException:
            return False




