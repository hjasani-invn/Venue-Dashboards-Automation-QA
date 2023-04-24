import time

from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class RouteUploadDownloadPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        log = cl.customLogger(logging.DEBUG)

        # locators

    def any_future_automation_method(self):
        """
        this is empty method, as route upload, download, modification tests need to perform manually.
        future scopes for route upload, download, modification related should implement here.
        """
        pass
