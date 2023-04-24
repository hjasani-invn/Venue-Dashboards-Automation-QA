import time

from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class RouteDrawingPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        log = cl.customLogger(logging.DEBUG)
        # locators

    def any_future_automation_method(self):
        """
        this is empty method, as route drawing tests need to perform manually.
        future scopes for route drawing related will be implemented here.
        """
        pass
