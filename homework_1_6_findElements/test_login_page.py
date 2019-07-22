""" Test login page Opencart"""
import time
import pytest
from homework_1_6_findElements.locators import LoginPageLocators
from homework_1_6_findElements.page_objects import LoginPage


@pytest.fixture(scope="session")
def open_login_page(driver, request):
    """ Open login page Opencart"""
    url = 'opencart/admin/'
    return driver.get("".join([request.config.getoption("--address"), url]))


@pytest.fixture(scope="function")
def login_page(driver):
    """ Login Opencart"""
    return LoginPage(driver)


@pytest.fixture(scope="function")
def login(login_page):
    """ Login in login page Opencart"""
    login_page.set_username("admin")
    login_page.set_password("admin")
    login_page.login()
    time.sleep(5)


@pytest.fixture(scope="function")
def close_alert(login_page):
    """ close alert Opencart"""
    login_page.close_alert()


@pytest.fixture(scope="function")
def logout(login_page):
    """ Logout Opencart"""
    login_page.logout()


@pytest.fixture(scope="function")
def login_empty_password(login_page):
    """ Login with empty password Opencart"""
    login_page.set_username("admin")
    login_page.set_password("")
    login_page.login()
    time.sleep(5)


@pytest.fixture(scope="function")
def login_wrong_password(login_page):
    """ Login with wrong password Opencart"""
    login_page.set_username("admin")
    login_page.set_password("error")
    login_page.login()
    time.sleep(5)


@pytest.fixture(scope="function")
def login_forgotten_password_input_email(login_page):
    """ Login with forgotten_password_input_email Opencart"""
    login_page.forgotten_password()
    time.sleep(5)


@pytest.fixture(scope="function")
def login_forgotten_wrong_email(login_page):
    """ Login with login_forgotten_wrong_email Opencart"""
    login_page.set_email("e1@e1.com")
    login_page.login()
    time.sleep(5)


@pytest.fixture(scope="function")
def login_forgotten_right_email(login_page):
    """ Login with login_forgotten_right_email Opencart"""
    login_page.set_email("gonovans@gmail.com")
    login_page.login()
    time.sleep(5)


@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestLoginPage:

    @pytest.mark.usefixtures("login_empty_password")
    def test_login_empty_password(self, driver):
        """ test_login_empty_password Opencart"""
        login_empty_password
        print(driver.find_element(*LoginPageLocators.ERROR).text)
        assert driver.find_element(*LoginPageLocators.ERROR).is_displayed()
        assert "No match" in driver.find_element(*LoginPageLocators.ERROR).text

    @pytest.mark.usefixtures("login_wrong_password")
    def test_login_wrong_password(self, driver):
        """ test_login_wrong_password Opencart"""
        print(driver.find_element(*LoginPageLocators.ERROR).text)
        assert driver.find_element(*LoginPageLocators.ERROR).is_displayed()
        assert "No match" in driver.find_element(*LoginPageLocators.ERROR).text

    @pytest.mark.usefixtures
    def test_login_forgotten_password_wrong_email(self, driver,
                                                  login_forgotten_password_input_email,
                                                  login_forgotten_wrong_email):
        """ test_login_forgotten_password_wrong_email Opencart"""
        login_forgotten_password_input_email
        login_forgotten_wrong_email
        print(driver.find_element(*LoginPageLocators.ERROR).text)
        assert driver.find_element(*LoginPageLocators.ERROR).is_displayed()
        assert "The E-Mail Address was not found" in \
               driver.find_element(*LoginPageLocators.ERROR).text
        driver.find_element(*LoginPageLocators.REPLY).click()

    @pytest.mark.usefixtures("login_forgotten_password_input_email")
    def test_login_forgotten_password_input_email(self, driver):
        """ test_login_forgotten_password_input_email Opencart"""
        print(driver.find_element(*LoginPageLocators.EMAIL).is_displayed())
        print(driver.find_element(*LoginPageLocators.EMAIL).text)
        driver.find_element(*LoginPageLocators.REPLY).click()

    @pytest.mark.usefixtures
    def test_login_forgotten_password_right_email(self, driver,
                                                  login_forgotten_password_input_email,
                                                  login_forgotten_right_email):
        """ test_login_forgotten_password_right_email Opencart"""
        login_forgotten_password_input_email
        login_forgotten_right_email
        print(driver.find_element(*LoginPageLocators.SUCCESS).text)
        assert driver.find_element(*LoginPageLocators.SUCCESS).is_displayed()
        assert "An email with a confirmation link has been sent" in \
               driver.find_element(*LoginPageLocators.SUCCESS).text

    @pytest.mark.usefixtures("login", "close_alert")
    def test_login(self, driver):
        """ test_login Opencart"""
        assert "dashboard" in driver.current_url
        close_alert
