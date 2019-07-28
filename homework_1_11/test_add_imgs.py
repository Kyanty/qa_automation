""" Tests product page Opencart"""
import pytest


COUNT = 3


@pytest.fixture(scope="function")
def add_img(driver, product_page):
    """ Add new product Opencart"""
    product_page.add_new_product()
    product_page.input_product_name()
    product_page.input_meta_tag()
    product_page.click_product_data()
    product_page.input_model()
    product_page.click_product_img_menu()
    count = 0
    while count < 3:
        product_page.add_img()
        product_page.click_on_image()
        product_page.edit_img()
        product_page.choose_img()
        count += 1


@pytest.mark.usefixtures("open_product_page")
@pytest.mark.usefixtures("login")
@pytest.mark.usefixtures("open_login_page")
class TestImgs:
    def test_add_img(self, driver, add_img):
        """ Test add product Opencart"""
        check = driver.find_elements_by_xpath("//table[@id='images']/tbody/tr")
        assert len(check) == COUNT

