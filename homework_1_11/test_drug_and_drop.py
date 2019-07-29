""" Test drug and drop on demo Opencart"""
import pytest


@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_demo")
def test_drug_and_drop(driver, login_page, product_page):
    """ Test drug and drop on demo Opencart"""
    login_page.clear_username()
    login_page.clear_password()
    login_page.set_username("demo")
    login_page.set_password("demo")
    login_page.login()
    driver.find_element_by_id('menu-design').click()
    driver.find_element_by_xpath("//a[contains(text(), 'Конструктор Меню')]").click()
    assert product_page.drug_and_drop() == True



