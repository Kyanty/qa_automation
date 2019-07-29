import pytest
import sys
from selenium import webdriver
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from homework_2_12_log.models.page_objects.page_objects import LoginPage


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://192.168.56.101/",
                     help="Opencart web address")
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")
    parser.addoption("--wait", action="store", default=10000, help="Wait time")


class MyListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        driver.save_screenshot('screenshots/exception.png')
        print(exception)


@pytest.fixture(scope="session", autouse=True)
def address(request):
    url = request.config.getoption("--address")
    yield url


@pytest.fixture(scope="session", autouse=True)
def wait(request):
    wait = request.config.getoption("--address")
    yield wait


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    wait = request.config.getoption("--wait")
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': int(wait), 'pageLoad': int(wait)}
        capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
                                        'performance': 'ALL', 'server': 'ALL'}
        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.accept_untrusted_certs = True
        wd = EventFiringWebDriver(webdriver.Firefox(firefox_profile=profile, capabilities=capabilities), MyListener())
        wd.maximize_window()
    elif browser == 'chrome':
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['timeouts'] = {'implicit': int(wait), 'pageLoad': int(wait)}
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        wd = webdriver.Chrome(desired_capabilities=capabilities)
        wd.fullscreen_window()
    else:
        print('Unsupported browser!')
        sys.exit(1)
    yield wd
    wd.quit()


@pytest.fixture(scope="session")
def open_login_page(driver, request):
    url = 'opencart/admin/'
    driver.get("".join([request.config.getoption("--address"), url]))


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="function")
def login(driver, login_page):
    login_page.clear_username()
    login_page.clear_password()
    login_page.set_username("admin")
    login_page.set_password("admin")
    login_page.login()
    login_page.close_alert()



