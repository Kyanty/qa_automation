from homework_1_7_productPage.models.page import BasePage
from homework_1_7_productPage.models.locators import BaseLocators, LoginPageLocators


class LoginPage(BasePage):
    def set_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def login(self):
        self.driver.find_element(*BaseLocators.PRIMARY_BUTTON).click()

    def close_alert(self):
        self.driver.find_element(*LoginPageLocators.CLOSE_BUTTON).click()

    def logout(self):
        self.driver.find_element(*LoginPageLocators.LOGOUT).click()

    def reply(self):
        self.driver.find_element(*LoginPageLocators.REPLY).click()

    def clear_username(self):
        self._clear_element_(self.driver.find_element(*LoginPageLocators.USERNAME))

    def clear_password(self):
        self._clear_element_(self.driver.find_element(*LoginPageLocators.PASSWORD))

    def forgotten_password(self):
        self.driver.find_element(*LoginPageLocators.FORGOTTEN_PASSWORD).click()

    def set_email(self, email):
        self.driver.find_element(*LoginPageLocators.EMAIL).send_keys(email)

    def click_menu(self):
        self.driver.find_element(*LoginPageLocators.RRR).click()
