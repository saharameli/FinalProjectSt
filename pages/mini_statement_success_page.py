from pages.base_page import BasePage
from pages.mini_statement_success_page_locators import MinistSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL, MINI_STMNT_SUCCESS_TEXT,MINI_ST_BTN_TEXT
from pages.mini_statement_page_locators import MinistPageLocators


class MinistSuccessPage(BasePage):


        def is_mini_success(self):
            mini_success_label = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                        MinistSuccessPageLocators.INPUT_SUCCESS_TXT).text
            if (mini_success_label == MINI_STMNT_SUCCESS_TEXT):
                return True
            else:
                return False


        def mini_st_if_logged_in(self):
            mini_st_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                             MinistPageLocators.MINI_ST_BTN).text

            if mini_st_text == MINI_ST_BTN_TEXT:
                return True
            else:
                return False


