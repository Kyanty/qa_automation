""" Tests product page Opencart"""
import time
import random
import pytest
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from homework_1_7_productPage.page_objects import LoginPage


@pytest.fixture(scope="session")
def open_login_page(driver, request):
    """ Open login page Opencart"""
    url = 'opencart/admin/'
    return driver.get("".join([request.config.getoption("--address"), url]))


@pytest.fixture(scope="session")
def login_page(driver):
    """ Login Opencart"""
    return LoginPage(driver)


@pytest.fixture(scope="session")
def login(login_page):
    """ Login in login page Opencart"""
    login_page.set_username("admin")
    login_page.set_password("admin")
    login_page.login()
    time.sleep(5)
    login_page.close_alert()


@pytest.mark.usefixtures("login")
@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestProductPage:
    def test_add_product(self, driver):
        """ Test add product Opencart"""
        els = driver.find_elements_by_class_name("parent.collapsed")
        for el in els:
            if el.text == "Catalog":
                catalog = el
                break
        catalog.click()
        catalog_elements = driver.find_elements_by_tag_name("li")
        for catalog_element in catalog_elements:
            if catalog_element.text == "Products":
                catalog_element.click()
                break

        driver.find_element(By.CLASS_NAME, "fa.fa-plus").click()
        panel_elements = driver.find_elements_by_tag_name("li")
        for panel_element in panel_elements:
            if panel_element.text == "General":
                panel_element.click()
                break
        general_required = driver.find_elements_by_class_name("form-group.required")
        for field in general_required:
            if field.text == 'Product Name':
                num = [1, 3, 4, 5, 19, 3, 6, 7]
                field.find_element(By.TAG_NAME, "input").send_keys("test_name1"
                                                                   + str(random.choice(num)))
            elif field.text == 'Meta Tag Title':
                field.find_element(By.TAG_NAME, "input").send_keys("test_meta-title")
                break

        panel_elements1 = driver.find_elements_by_tag_name("li")
        for panel_element1 in panel_elements1:
            if panel_element1.text == "Data":
                panel_element1.click()
                break
        data_required = driver.find_elements_by_class_name("form-group.required")
        for field in data_required:
            if field.text == 'Model':
                field.find_element(By.TAG_NAME, "input").send_keys("test_model")
                break
        driver.find_element(By.CLASS_NAME, "fa.fa-save").click()
        notification = driver.find_element_by_class_name("alert.alert-success.alert-dismissible")
        notification_text = notification.text.rstrip("\n×'")
        assert notification
        assert notification_text == "Success: You have modified products!"

    def test_edit_product(self, driver):
        """ Test edit product Opencart"""
        els = driver.find_elements_by_class_name("parent.collapsed")
        for el in els:
            if el.text == "Catalog":
                catalog = el
                break
        catalog.click()
        catalog_elements = driver.find_elements_by_tag_name("li")
        for catalog_element in catalog_elements:
            if catalog_element.text == "Products":
                catalog_element.click()
                break
        edits = driver.find_element_by_class_name("fa.fa-pencil")
        print(edits.text)
        edits.click()
        driver.find_element(By.CLASS_NAME, "fa.fa-save").click()
        notification = driver.find_element_by_class_name("alert.alert-success.alert-dismissible")
        notification_text = notification.text.rstrip("\n×'")
        assert notification
        assert notification_text == "Success: You have modified products!"

    def test_del_product(self, driver):
        """ Test delete product Opencart"""
        els = driver.find_elements_by_class_name("parent.collapsed")
        for el in els:
            if el.text == "Catalog":
                catalog = el
                break
        catalog.click()
        catalog_elements = driver.find_elements_by_tag_name("li")
        for catalog_element in catalog_elements:
            if catalog_element.text == "Products":
                catalog_element.click()
                break
        driver.find_element(By.XPATH, "//*[@placeholder='Product Name']").send_keys("test_name1")
        driver.find_element_by_id("button-filter").click()

        names = driver.find_elements_by_class_name("text-left")
        for name in names:
            if name.tag_name == "test_name1":
                driver.find_element_by_class_name()
                break
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_class_name("fa.fa-trash-o").click()
        driver.switch_to_alert
        Alert(driver).accept()
        notification = driver.find_element_by_class_name("alert.alert-success.alert-dismissible")
        notification_text = notification.text.rstrip("\n×'")
        assert notification
        assert notification_text == "Success: You have modified products!"
