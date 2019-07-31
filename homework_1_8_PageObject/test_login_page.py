import pytest
import time
from homework_1_8_PageObject.models.locator import LoginPageLocators


def login_forgotten_right_email(login_page):
    """ Login with login_forgotten_right_email Opencart"""
    login_page.set_email("gonovans@gmail.com")
    login_page.login()
    time.sleep(5)


@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestLoginPage:

    def test_login(self, driver, login_page):
        login_page.signin()
        print(driver.current_url)
        assert "dashboard" in driver.current_url
        login_page.logout()

    def test_login_with_empty_password(self, driver, login_page):
        """ test_login_empty_password Opencart"""
        login_page.login_with_empty_password()
        text = driver.find_element(*LoginPageLocators.ERROR).text
        assert "No match" in text

    def test_login_with_wrong_password(self, driver, login_page):
        """ test_login_wrong_password Opencart"""
        login_page.login_with_wrong_password()
        text = driver.find_element(*LoginPageLocators.ERROR).text
        assert "No match" in text

    def test_login_forgotten_password_wrong_email(self, driver, login_page):
        """ test_login_forgotten_password_wrong_email Opencart"""
        login_page.login_forgotten_wrong_email()
        text = driver.find_element(*LoginPageLocators.ERROR).text
        assert "The E-Mail Address was not found" in text
        login_page.reply()

    def test_login_forgotten_password_right_email(self, driver, login_page):
        """ test_login_forgotten_password_right_email Opencart"""
        login_page.forgotten_password_right_email()
        text = driver.find_element(*LoginPageLocators.SUCCESS).text
        assert "An email with a confirmation link has been sent" in text


