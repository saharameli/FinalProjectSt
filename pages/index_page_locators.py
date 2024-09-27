from selenium.webdriver.common.by import By

# index locators
class IndexPageLocators:


    USER_NAME_TXTBX = (By.NAME, "uid")
    PASSWORD_TXTBX = (By.NAME, "password")
    LOGIN_SUBMIT_BUTTON = (By.NAME, "btnLogin")
    MINI_STM_BTN = (By.XPATH, "//*[@href='MiniStatementInput.php']")

