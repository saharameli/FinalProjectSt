import time

from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL,TEST_SITE_URL


#index page
class IndexPage(BasePage):


    def login_using_username_password(self,user_name, password):
        self.navigate_to(TEST_SITE_URL)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,IndexPageLocators.USER_NAME_TXTBX).send_keys(user_name)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,IndexPageLocators.PASSWORD_TXTBX).send_keys(password)
        self.find_element(IndexPageLocators.LOGIN_SUBMIT_BUTTON).click()
        time.sleep(4)




