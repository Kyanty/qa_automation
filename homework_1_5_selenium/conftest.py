import pytest
import sys
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://192.168.56.101/opencart/", help="Opencart address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        wd = webdriver.Firefox()
        wd.fullscreen_window()
    elif browser == 'chrome':
        wd = webdriver.Chrome()
        wd.fullscreen_window()
    else:
        print('Unsupported browser!')
        sys.exit(1)
    yield wd
    wd.quit()


@pytest.fixture(scope="session", autouse=True)
def url(request):
    url = request.config.getoption("--address")
    yield url
