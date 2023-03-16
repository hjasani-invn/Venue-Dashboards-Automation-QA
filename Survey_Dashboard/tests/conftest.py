import pytest
from selenium import webdriver
from base.webdriver_factory import WebDriverFactory


@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser, product):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser, product)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--product")
    parser.addoption("--osType", help="Type of operating system")
    # parser.addoption("--headless")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def product(request):
    return request.config.getoption("--product")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

# @pytest.fixture(scope="session")
# def osType(request):
#     return request.config.getoption("--headless")