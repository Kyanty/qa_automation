import logging
from browsermobproxy import Server
import pytest
from selenium.webdriver.common.by import By

server = Server(r"/Users/Kyanty/PycharmProjects/qa_automation/browsermob-proxy-2.1.4/bin/browsermob-proxy")
server.start()


class TestLoginPage:
    @pytest.mark.usefixtures("login")
    @pytest.mark.usefixtures("login_page")
    @pytest.mark.usefixtures("open_login_page")
    def test_login(self, driver):
        logging.basicConfig(level=logging.DEBUG)
        logging.debug('opened dashboard')
        lst = driver.get_log("browser")
        for l in lst:
            print(l)
        assert "dashboard" in driver.current_url
        driver.find_element(By.CLASS_NAME, "fa.fa-sign-out").click()

    def test_proxy(self, driver):
        """test proxy"""
        driver.get('https://otus.ru')
        proxy = server.create_proxy()
        proxy.new_har()
        pass

