
from selenium.webdriver.common.by import By

class MinistPageLocators:
    ACCOUNT_NO_DRPDN_BOX = (By.NAME, "accountno")
    SUBMIT_BUTTON = (By.NAME, "AccSubmit")
    RESET_BUTTON = (By.NAME, "res")
    MINI_STM_BTN = (By.XPATH, "//*[@href='MiniStatementInput.php']")
    MINI_ST_BTN = (By.XPATH, "//*[@class='heading3']")

