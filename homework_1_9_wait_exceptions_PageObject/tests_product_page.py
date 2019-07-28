""" Tests product page Opencart"""
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework_1_9_wait_exceptions_PageObject.models.page_objects.page_objects import ProductPage


@pytest.fixture(scope="function")
def product_page(driver):
    """ Return ProductPage Opencart"""
    return ProductPage(driver)


@pytest.fixture(scope="function")
def open_product_page(driver):
    """ Open product page Opencart"""
    page = ProductPage(driver)
    page.click_catalog_menu()
    page.open_product_page()


@pytest.fixture(scope="function")
def add_product(product_page, delete_product):
    """ Add new product Opencart"""
    delete_product
    product_page.add_new_product()
    product_page.input_product_name()
    product_page.input_meta_tag()
    product_page.click_product_data()
    product_page.input_model()
    product_page.save_changes()


@pytest.fixture(scope="function")
def edit_product(product_page):
    """ Edit product Opencart"""
    product_page.edit()
    product_page.save_changes()


@pytest.fixture(scope="function")
def delete_product(driver, product_page):
    """ Delete product Opencart"""
    product_page.filter_product()
    product_page.filter_confirm()
    try:
        product_page.click_checkbox()
        driver.find_element_by_class_name("fa.fa-trash-o").click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        driver.switch_to_alert
        Alert(driver).accept()
    except NoSuchElementException:
        print("No such product")


@pytest.mark.usefixtures("open_product_page")
@pytest.mark.usefixtures("login")
@pytest.mark.usefixtures("open_login_page")
class TestProductPage:
    def test_add_product(self, driver, add_product):
        """ Test add product Opencart"""
        text = driver.find_element_by_class_name(
            "alert.alert-success.alert-dismissible").text.rstrip("\n×'")
        assert text == "Success: You have modified products!"
        driver.find_element(By.CLASS_NAME, "fa.fa-sign-out").click()

    def test_edit_product(self, driver, edit_product):
        """ Test edit product Opencart"""
        text = driver.find_element_by_class_name(
            "alert.alert-success.alert-dismissible").text.rstrip("\n×'")
        assert text == "Success: You have modified products!"
        driver.find_element(By.CLASS_NAME, "fa.fa-sign-out").click()

    def test_del_product(self, driver, delete_product):
        """ Test delete product Opencart"""
        try:
            text = driver.find_element_by_class_name(
                "alert.alert-success.alert-dismissible").text.rstrip("\n×'")
            assert text == "Success: You have modified products!"
        except NoSuchElementException:

            print("No products delete")
            pass
        driver.find_element(By.CLASS_NAME, "fa.fa-sign-out").click()

