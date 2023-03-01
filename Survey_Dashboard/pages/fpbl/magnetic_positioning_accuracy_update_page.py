import time

from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class MagneticPositioningAccuracyUpdatePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        log = cl.customLogger(logging.DEBUG)

    # LOCATORS:
    _admin_btn = "//span[contains(text(),'Admin')]"
    def click_admin(self):
        self.elementClick(self._admin_btn, locatorType="xpath")

    _survey_editor = "//span[contains(text(),'Survey - Editor')]"
    def click_survey_editor(self):
        self.elementClick(self._survey_editor, locatorType="xpath")

    _click_venue_search = "//span[contains(text(),'Select Venue')]"
    _search_venue_name = "//input[starts-with(@class, 'p-dropdown-filter p-inputtext p-component')]"
    _select_venue = "//p-dropdownitem//li[@aria-label='ICA Calgary ']"
    def enter_venue(self, venue_name="ICA"):
        '''
        space after ICA is not acceptable, name should be continue;
        i.e. ICA_Calgary: it will search ICA and select venue "ICA Calgary"
        '''
        self.elementClick(self._click_venue_search, locatorType="xpath")
        self.sendKeys(venue_name, self._search_venue_name, locatorType="xpath")
        self.elementClick(self._select_venue, locatorType="xpath")
        self.hold_wait()

    _select_floor = "//span[contains(text(),'Fourth Floor')]"
    def select_floor(self):
        self.elementClick(self._select_floor, locatorType="xpath")
        self.hold_wait()
