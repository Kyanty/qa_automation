import pytest
import sys
from selenium import webdriver
from homework_1_8_PageObject.models.page_objects.page_objects import LoginPage, ProductPage


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://192.168.56.101/",
                     help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")
    parser.addoption("--wait", action="store", default=10000, help="Wait time")


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
        wd = webdriver.Firefox(firefox_profile=profile, capabilities=capabilities)
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
    return driver.get("".join([request.config.getoption("--address"), url]))


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="function")
def product_page(driver):
    """ Return ProductPage Opencart"""
    return ProductPage(driver)




