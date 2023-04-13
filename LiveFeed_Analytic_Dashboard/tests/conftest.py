import logging
import os
import sys
import time
from pydoc import html

import pytest
import pytest_html_reporter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.core import driver

from base.webdriver_factory import WebDriverFactory
from pytest_html_reporter import attach
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setUp():
    print("Running method level setUp")

    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("\nRunning one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("\nRunning one time tearDown")
    # attach(data=driver.get_screenshot_as_png())
    # pytest_html_reporter.attach("..\\LiveFeed_Analytic_Dashboard\\report\\pytest_screenshots\\1681229377.png")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("http://dashboard-test.venuepositioning.com//"))
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             report_dir = os.path.dirname(item.config.option.htmlpath)
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             # file_name = str(int(round(time.time() * 1000))) + ".png"
#             destinationFile = os.path.join(report_dir, file_name)
#             feature_request = item.funcargs["request"]
#             driver = feature_request.getfixturevalue("setup")
#             driver.save_screenshot(destinationFile)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:300px;height:200px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# # def _capture_screenshot(name):
# #     driver.get_screenshot_as_file(name)
#
#
def pytest_html_report_title(report):
    report.title = "Livefeed Automation Report"

# @pytest.fixture(scope="function")
# def driver(request):
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()

# @pytest.fixture(scope="function")
# def screenshot_on_failure(request):
#     yield
#     if request.node.rep_call.failed:
#         driver = request.node.funcargs['driver']
#         driver.save_screenshot("screenshots/{}.png".format(request.node.name))


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     This hook is used to take screenshots when a test fails and attach them to the Allure report
#     """
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == "call" and report.failed:
#         allure.attach(
#             name="screenshot",
#             body=item.funcargs['browser'].get_screenshot_as_png(),
#             attachment_type=allure.attachment_type.PNG
#         )