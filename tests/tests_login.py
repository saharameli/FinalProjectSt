import time
from pages.login_success_page import LoginSuccessPage
from tests.test_utils import *
from pages.index_page import IndexPage
from pages.mini_statement_page import MinistatementPage
from pages.mini_statement_success_page import MinistSuccessPage



class TestLogin:

    def test_login(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.login_using_username_password(username_password[0], username_password[1])
        login_success_page = LoginSuccessPage(driver)
        assert login_success_page.is_login_success(), "Login Failed!"

    def test_mini_st(self, driver):
        mini_stmnt = MinistatementPage(driver)
        mini_stmnt.find_mini_st()
        mini_stmnt.wait_and_choose_option()
        mini_stmnt.click_submit_btn()
        mini_success_page = MinistSuccessPage(driver)
        assert mini_success_page.is_mini_success(), "User is not logged in to the statement!"




