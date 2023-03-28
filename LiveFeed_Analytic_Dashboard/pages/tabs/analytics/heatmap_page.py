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
    _start_date_error = "//mat-error[contains(text(),'Start date should be greater than ')]"


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

        # # start_date_error_msg_appear = self.getElement(self._start_date_error, locatorType="xpath")
        # # txt = start_date_error_msg_appear.text
        # # print(txt)
        # # if txt != "":
        # #     # get_txt = start_date_error_msg_appear.text()
        # #     starting_with = txt[:34]
        # #     print(starting_with)
        # #     return starting_with
        #
        #
        # start_date_error_msg_appear = self.isElementPresent(self._start_date_error, locatorType="xpath")
        # if start_date_error_msg_appear == True:
        #     print("if loop")
        #     return None


    _time_zone = "//input[@data-placeholder='Timezone']"

    def select_timezone(self, country_name):
        self.hold_wait()
        self.backspace_clear(self._time_zone, locatorType="xpath")
        self.hold_wait()
        self.sendKeys(country_name, self._time_zone, locatorType="xpath")
        self.hold_wait()
        self.click_out()

    _search_ = "//span[contains(text(),'Search')]"
    _search_btn_status_ = "//div[@class='map-input map-submit-wrapper']//button"


    def click_search(self):
        # self.elementClick(self._search_, locatorType="xpath")
        # self.hold_wait()

        get_search_btn_attribute = self.getElement(self._search_btn_status_, locatorType="xpath")
        get_search_btn_stats = get_search_btn_attribute.get_attribute("disabled")
        print(get_search_btn_stats)

        if get_search_btn_stats != 'true':
            self.elementClick(self._search_, locatorType="xpath")
            self.hold_wait()
        return get_search_btn_stats


    # _select_all_users = "//div[@class='map-all-tree-users-select']//div[@class='mat-checkbox-inner-container']"
    _select_all_users = "//div[@class='map-all-tree-users-select']"

    def select_all_users(self):
        self.hold_wait()
        # check_box_visible = self.getElement(self._select_all_users, locatorType="xpath")
        # check_box_visible_get_value = check_box_visible.get_attribute("aria-checked")
        # if check_box_visible_get_value == "true":
        self.elementClick(self._select_all_users, locatorType="xpath")
        self.hold_wait()
        self.hold_wait()
        # else:
        #     print("users not selected")

        self.screen_shot(file="test_3_4_1_populate_heatmap")