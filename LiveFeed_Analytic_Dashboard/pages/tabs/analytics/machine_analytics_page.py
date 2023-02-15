import os
from pathlib import Path

from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging


class MachineAnalyticsTabPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _select_analytics_tab = "//span[contains(text(),'Analytics')]"
    _select_machine_analytics_tab = "//a[contains(text(),'Machine Analytics')]"

    def select_machine_analytic_downloads_tab(self):
        self.hold_wait()
        self.elementClick(self._select_analytics_tab, locatorType="xpath")
        self.hold_wait()
        self.hold_wait()
        self.elementClick(self._select_machine_analytics_tab, locatorType="xpath")
        self.hold_wait()

    _select_venue = "//mat-select[@placeholder='Venue']"

    def enter_venue_name(self, v_n):
        self.hold_wait()
        self.elementClick(self._select_venue, locatorType="xpath")
        self.hold_wait()
        self.sendKeys(v_n, self._select_venue, locatorType="xpath")
        self.click_out()
        self.hold_wait()

    _click_out = "//body"

    def click_out(self):
        self.elementClick(self._click_out, locatorType="xpath")

    # "//span[contains(@class,'mat-select-placeholder')]"
    # _all_machine_xpath = "//span[contains(text(),'All Machines')]"
    _all_machine_xpath = "(//mat-select[@role='combobox'])[2]"
    _select_all_xpath = "//span[@class='mat-checkbox-label']"
    def select_all_machines(self):
        self.elementClick(self._all_machine_xpath, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_all_xpath, locatorType="xpath")
        self.hold_wait()
        self.click_out()

    _start_date = "//input[@data-placeholder='Start Date']"
    _start_time = "//input[@data-placeholder='Start time']"

    _end_date = "//input[@data-placeholder='End Date']"
    _end_time = "//input[@data-placeholder='End time']"

    def choose_date_and_time(self, s_date, s_time, e_date, e_time):
        self.backspace_clear(self._start_date, locatorType="xpath")
        self.sendKeys(s_date, self._start_date, locatorType="xpath")
        self.hold_wait()
        self.backspace_clear(self._start_time, locatorType="xpath")
        self.sendKeys(s_time, self._start_time, locatorType="xpath")

        self.backspace_clear(self._end_date, locatorType="xpath")
        self.sendKeys(e_date, self._end_date, locatorType="xpath")
        self.hold_wait()
        self.backspace_clear(self._end_time, locatorType="xpath")
        self.sendKeys(e_time, self._end_time, locatorType="xpath")

    _search_ = "//span[contains(text(),'Search')]"

    def click_search(self):
        self.hold_wait()
        self.hold_wait()
        self.elementClick(self._search_, locatorType="xpath")
        self.hold_wait()

    _chevron_left = "//mat-icon[normalize-space()='chevron_left']"
    def remove_search_panel_to_left(self):
        self.hold_wait()
        self.elementClick(self._chevron_left, locatorType="xpath")
        self.hold_wait()