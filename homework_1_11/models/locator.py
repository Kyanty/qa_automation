from selenium.webdriver.common.by import By


class BaseLocators(object):
    PRIMARY_BUTTON = (By.CLASS_NAME, "btn.btn-primary")
    PRODUCT_NAME = "Test_product1"
    PRODUCT_MODEL = "Test model"
    META_TAG = "Test meta_tag1"


class LoginPageLocators(object):

    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    EMAIL = (By.ID, "input-email")
    CLOSE_BUTTON = (By.CLASS_NAME, "close")
    SUCCESS = (By.CLASS_NAME, "alert.alert-success.alert-dismissible")
    ERROR = (By.CLASS_NAME, "alert.alert-danger.alert-dismissible")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    REPLY = (By.CLASS_NAME, "fa.fa-reply")
    LOGOUT = (By.CLASS_NAME, "fa.fa-sign-out")


class ProductPageLocators(object):
    CATALOG = (By.CLASS_NAME, "parent.collapsed")
    PRODUCT_MENU = (By.XPATH, "//a[contains(text(),'Products')]")
    NEW_PRODUCT = (By.CLASS_NAME, "fa.fa-plus")
    SAVE = (By.CLASS_NAME, "fa.fa-save")
    EDIT_BUTTON = (By.CLASS_NAME, "fa.fa-pencil")
    PRODUCT_NAME = (By.NAME, 'product_description[1][name]')
    META_TAG_TITLE = (By.NAME, 'product_description[1][meta_title]')
    MODEL = (By.NAME, 'model')
    DATA_PRODUCT = (By.PARTIAL_LINK_TEXT, 'Data')
    NAME_PRODUCT = (By.XPATH, "//td[contains(text(),'Test')]/parent::*//input")
    FILTER_NAME = (By.NAME, "filter_name")
    FILTER_CONFIRM = (By.ID, "button-filter")
    CHECKBOX = (By.XPATH, "//td[contains(text(),'Test_product1')]//..//td/input[@name='selected[]']")
    PRODUCT_IMG_MENU = (By.LINK_TEXT, "Image")
    ADD_IMG = (By.XPATH, "//button[@data-original-title='Add Image']")
    IMG_ICON = (By.XPATH, "(//div[@class='table-responsive']//table[@id='images']//*//img)[last()]")
    EDIT_IMG = (By.ID, "button-image")
    CHOOSE_IMG =(By.XPATH, "//div[@id='modal-image']//img[@title='%s']" % "cart.png")
    COUNT_IMGS = (By.XPATH, "//table[@id='images']/tbody/tr")
    PRODUCT_COMPUTER = (By.XPATH, "//span[contains(text(), 'Компьютеры')]")
    PRODUCT_NOTEBOOK = (By.XPATH, "//span[contains(text(), 'Ноутбуки')]")

