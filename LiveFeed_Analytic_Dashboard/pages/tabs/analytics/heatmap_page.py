from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging


class HeatmapTabPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _select_analytics_tab = "//span[contains(text(),'Analytics')]"
    _select_heatmap_tab = "//a[contains(text(),'Heatmap')]"

    def select_analytic_heatmap_tab(self):
        self.elementClick(self._select_analytics_tab, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_heatmap_tab, locatorType="xpath")
        self.hold_wait()

    _select_floor = "//div[@class='leaflet-control-layers-base']/label//div//span[contains(text(), ' 4')]"

    def select_floor(self):
        self.elementClick(self._select_floor, locatorType="xpath")


    _select_venue = "//mat-select[@placeholder='Venue']"

    def enter_venue_name(self, v_n):
        self.hold_wait()
        self.elementClick(self._select_venue, locatorType="xpath")
        self.hold_wait()
        self.sendKeys(v_n, self._select_venue, locatorType="xpath")
        # self.elementClick(self._select_venue_it, locatorType="xpath")
        self.click_out()
        self.hold_wait()


    _click_out = "//body"

    def click_out(self):
        self.elementClick(self._click_out, locatorType="xpath")

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


    _time_zone = "//input[@data-placeholder='Timezone']"

    def select_timezone(self, country_name):
        self.hold_wait()
        self.backspace_clear(self._time_zone, locatorType="xpath")
        self.hold_wait()
        self.sendKeys(country_name, self._time_zone, locatorType="xpath")
        self.hold_wait()
        self.click_out()

    _search_ = "//span[contains(text(),'Search')]"

    def click_search(self):
        self.elementClick(self._search_, locatorType="xpath")
        self.hold_wait()


    # _select_all_users = "//div[@class='map-all-tree-users-select']//div[@class='mat-checkbox-inner-container']"
    _select_all_users = "//div[@class='map-all-tree-users-select']"

    def select_all_users(self):
        self.hold_wait()
        self.elementClick(self._select_all_users, locatorType="xpath")
        self.hold_wait()
        self.hold_wait()
        self.screen_shot(file="test_3_4_1_populate_heatmap")