from selenium.webdriver.common.by import By


class BaseLocators(object):
    PRIMARY_BUTTON = (By.CLASS_NAME, "btn.btn-primary")


class LoginPageLocators(object):
    USERNAME = (By.ID, "input-username")
    USERNAME2 = (By.NAME, "username")
    USERNAME3 = (By.CSS_SELECTOR, "#input-username")
    USERNAME4 = (By.XPATH, "//*[@placeholder='Username']")
    PASSWORD = (By.ID, "input-password")
    SUCCESS = (By.CLASS_NAME, "alert.alert-success.alert-dismissible")
    ERROR = (By.CLASS_NAME, "alert.alert-danger.alert-dismissible")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    EMAIL = (By.ID, "input-email")
    CLOSE_BUTTON = (By.CLASS_NAME, "close")
    LOGOUT = (By.CLASS_NAME, "fa.fa-sign-out")
    REPLY = (By.CLASS_NAME, "fa.fa-reply")
    RRR = (By.CLASS_NAME, "parent.collapsed")