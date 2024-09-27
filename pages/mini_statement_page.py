import time

from pages.base_page import BasePage
from pages.mini_statement_page_locators import MinistPageLocators
from resources.constants import MAX_WAIT_INTERVAL
from selenium.webdriver.support.select import Select


class MinistatementPage(BasePage):

    def find_mini_st(self):
        # Print locator details for debugging
        print(f"Locator for MINI_STM_BTN: {MinistPageLocators.MINI_STM_BTN}")

        # Attempt to find the element and click it
        try:
            mini_stm_element = self.find_element(MinistPageLocators.MINI_STM_BTN)
            print(f"Found element: {mini_stm_element}")
            mini_stm_element.click()

        except Exception as e:
            print(f"Error while finding or clicking MINI_STM_BTN: {e}")

    def wait_and_choose_option(self):
        # Wait for the dropdown element and find it
        dropdown_element = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 MinistPageLocators.ACCOUNT_NO_DRPDN_BOX)

        # Create a Select object from the dropdown element
        select = Select(dropdown_element)

        # Use select_by_value to choose the option
        select.select_by_visible_text("3308")  # Replace "3308" with the actual value you want to select
        time.sleep(5)

    def click_submit_btn(self):
        # Use the explicitly wait method to find the submit button and click it
        submit_button = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, MinistPageLocators.SUBMIT_BUTTON)

