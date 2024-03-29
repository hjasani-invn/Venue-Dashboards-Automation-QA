import time

import selenium.common.exceptions

from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging
import os.path


class KeyListPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _click_key_list = "//span[normalize-space()='Key List']"

    def open_key_list(self):
        self.elementClick(self._click_key_list, locatorType="xpath")
        self.hold_wait()
        self.hold_wait()

    _find_keys_name = "//h3[contains(text(),'Keys')]"
    def verify_keys_opens(self):
        get_keyss_name = self.getElement(self._find_keys_name, locatorType="xpath")
        return get_keyss_name.text

