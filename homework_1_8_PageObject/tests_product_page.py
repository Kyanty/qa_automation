""" Tests product page Opencart"""
import pytest
from selenium.common.exceptions import NoSuchElementException
from homework_1_8_PageObject.models.locator import LoginPageLocators


@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestProductPage:
    def test_add_product(self, driver, product_page, login_page):
        """ Test add product Opencart"""
        product_page.add_product()
        text = driver.find_element(*LoginPageLocators.SUCCESS).text.rstrip("\n×'")
        assert "Success: You have modified products!" in text
        login_page.logout()

    def test_edit_product(self, driver, product_page, login_page):
        """ Test edit product Opencart"""
        product_page.edit_product()
        text = driver.find_element(*LoginPageLocators.SUCCESS).text.rstrip("\n×'")
        assert "Success: You have modified products!" in text
        login_page.logout()

    def test_del_product(self, driver, product_page, login_page):
        """ Test delete product Opencart"""
        product_page.delete_product()
        try:
            text = driver.find_element(*LoginPageLocators.SUCCESS).text.rstrip("\n×'")
            assert "Success: You have modified products!" in text
        except NoSuchElementException:
            print("No products delete")
            pass
        login_page.logout()

