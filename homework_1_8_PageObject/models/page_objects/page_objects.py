import time
from selenium.common.exceptions import NoSuchElementException
from homework_1_8_PageObject.models.page import BasePage
from homework_1_8_PageObject.models.locator import LoginPageLocators


class LoginPage(BasePage):
    def signin(self):
        self._clear_username_()
        self._clear_password_()
        self._set_username_("admin")
        self._set_password_("admin")
        self._login_confirm_()
        self._close_alert_()

    def login_with_empty_password(self):
        """ Login with empty password Opencart"""
        self._clear_username_()
        self._clear_password_()
        self._set_username_("admin")
        self._set_password_("")
        self._login_confirm_()

    def login_with_wrong_password(self):
        """ Login with wrong password Opencart"""
        self._clear_username_()
        self._clear_password_()
        self._set_username_("admin")
        self._set_password_("error")
        self._login_confirm_()

    def forgotten_password_input_email(self):
        """ Login with forgotten_password_input_email Opencart"""
        self._clear_username_()
        self._clear_password_()
        self._forgotten_password_()
        time.sleep(5)

    def forgotten_password_right_email(self):
        """ Login with login_forgotten_right_email Opencart"""
        self._clear_username_()
        self._clear_password_()
        self._forgotten_password_()
        time.sleep(5)
        self._set_email_("gonovans@gmail.com")
        self._login_confirm_()

    def login_forgotten_wrong_email(self):
        """ Login with login_forgotten_wrong_email Opencart"""
        self._clear_username_()
        self._clear_password_()
        self._forgotten_password_()
        time.sleep(5)
        self._set_email_("e1@e1.com")
        self._login_confirm_()

    def logout(self):
        self._logout_()

    def reply(self):
        self._reply_()

    def text_success(self):
        self.driver.find_element(*LoginPageLocators.SUCCESS)


class ProductPage(BasePage):

    def product_page(driver):
        """ Return ProductPage Opencart"""
        return ProductPage(driver)

    def open_product_page(driver):
        """ Open product page Opencart"""
        page = ProductPage(driver)
        page._click_catalog_menu_()
        page._open_product_page_()

    def delete_product(self):
        """ Delete product Opencart"""
        self._clear_username_()
        self._clear_password_()
        self._set_username_("admin")
        self._set_password_("admin")
        self._login_confirm_()
        self._close_alert_()
        self._click_catalog_menu_()
        self._open_product_page_()
        self._filter_product_()
        self._filter_confirm_()
        try:
            self._delete_choose_product()
        except NoSuchElementException:
            print("No such product")

    def add_product(self):
        self._clear_username_()
        self._clear_password_()
        self._set_username_("admin")
        self._set_password_("admin")
        self._login_confirm_()
        self._close_alert_()
        self._click_catalog_menu_()
        self._open_product_page_()
        self._filter_product_()
        self._filter_confirm_()
        try:
            self._delete_choose_product()
        except NoSuchElementException:
            print("No such product")
        self._add_new_product_()
        self._input_product_name_()
        self._input_meta_tag_()
        self._click_product_data_()
        self._input_model_()
        self._save_changes_()

    def edit_product(self):
        self._clear_username_()
        self._clear_password_()
        self._set_username_("admin")
        self._set_password_("admin")
        self._login_confirm_()
        self._close_alert_()
        self._click_catalog_menu_()
        self._open_product_page_()
        self._edit_()
        self._save_changes_()







