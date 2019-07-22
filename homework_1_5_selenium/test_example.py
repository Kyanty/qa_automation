import pytest


@pytest.mark.usefixtures
def test_base_page_opencart(driver, url):
    driver.get(url)
    assert driver.find_element_by_id("logo")
