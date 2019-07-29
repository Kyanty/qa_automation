from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from homework_1_11.models.page import BasePage
from homework_1_11.models.locator import BaseLocators, LoginPageLocators, ProductPageLocators


class LoginPage(BasePage):
    def set_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def clear_username(self):
        self._clear_element_(self.driver.find_element(*LoginPageLocators.USERNAME))

    def clear_password(self):
        self._clear_element_(self.driver.find_element(*LoginPageLocators.PASSWORD))

    def login(self):
        self.driver.find_element(*BaseLocators.PRIMARY_BUTTON).click()

    def logout(self):
        self.driver.find_element(*LoginPageLocators.LOGOUT).click()

    def close_alert(self):
        self.driver.find_element(*LoginPageLocators.CLOSE_BUTTON).click()

    def reply(self):
        self.driver.find_element(*LoginPageLocators.REPLY).click()

    def forgotten_password(self):
        self.driver.find_element(*LoginPageLocators.FORGOTTEN_PASSWORD).click()

    def set_email(self, email):
        self.driver.find_element(*LoginPageLocators.EMAIL).send_keys(email)


class ProductPage(BasePage):
    def click_catalog_menu(self):
        self.driver.find_element(*ProductPageLocators.CATALOG).click()

    def click_product_data(self):
        self.driver.find_element(*ProductPageLocators.DATA_PRODUCT).click()

    def click_product_img_menu(self):
        self.driver.find_element(*ProductPageLocators.PRODUCT_IMG_MENU).click()

    def open_product_page(self):
        self.driver.find_element(*ProductPageLocators.PRODUCT_MENU).click()

    def add_new_product(self):
        self.driver.find_element(*ProductPageLocators.NEW_PRODUCT).click()

    def save_changes(self):
        self.driver.find_element(*ProductPageLocators.SAVE).click()

    def edit(self):
        self.driver.find_element(*ProductPageLocators.EDIT_BUTTON).click()

    def input_product_name(self):
        self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).send_keys(*BaseLocators.PRODUCT_NAME)

    def input_meta_tag(self):
        self.driver.find_element(*ProductPageLocators.META_TAG_TITLE).send_keys(*BaseLocators.META_TAG)

    def input_model(self):
        self.driver.find_element(*ProductPageLocators.MODEL).send_keys(*BaseLocators.PRODUCT_MODEL)

    def filter_product(self):
        self.driver.find_element(*ProductPageLocators.FILTER_NAME).send_keys(*BaseLocators.PRODUCT_NAME)

    def filter_confirm(self):
        self.driver.find_element(*ProductPageLocators.FILTER_CONFIRM).click()

    def click_checkbox(self):
        self.driver.find_element(*ProductPageLocators.CHECKBOX).click()

    def add_img(self):
        return self.driver.find_element(*ProductPageLocators.ADD_IMG).click()

    def click_on_image(self):
        return self.driver.find_element(*ProductPageLocators.IMG_ICON).click()

    def edit_img(self):
        return self.driver.find_element(*ProductPageLocators.EDIT_IMG).click()

    def choose_img(self):
        return self.driver.find_element(*ProductPageLocators.CHOOSE_IMG).click()

    def get_element1_for_dnd(self):
        return self.driver.find_element(*ProductPageLocators.PRODUCT_COMPUTER)

    def get_element2_for_dnd(self):
        return self.driver.find_element(*ProductPageLocators.PRODUCT_NOTEBOOK)

    def drug_and_drop(self):
        element1 = self.get_element1_for_dnd()
        element2 = self.get_element2_for_dnd()
        ActionChains(self.driver).drag_and_drop(element1, element2).perform()
        return True




