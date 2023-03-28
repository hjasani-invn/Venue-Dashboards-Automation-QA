from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging


class PlaybackTabPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _select_analytics_tab = "//span[contains(text(),'Analytics')]"
    _select_playback_tab = "//a[contains(text(),'Playback')]"

    def select_analytic_playback_tab(self):
        self.elementClick(self._select_analytics_tab, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_playback_tab, locatorType="xpath")
        self.hold_wait()

    # _select_floor = "//label[@class='map-selected-floor']//span[contains(text(), ' 4')]"
    # _select_floor = "//label[@class='map-selected-floor']//input[@type='radio']"
    _select_floor = "//div[@class='leaflet-control-layers-base']/label//div//span[contains(text(), '4')]"


    def select_floor(self):
        self.elementClick(self._select_floor, locatorType="xpath")

    # locators

    # _select_venue = "//mat-select[@role='combobox']"
    _select_venue = "//mat-select[@placeholder='Venue']"
    # _choose_venue = "//input[@placeholder='Search']"
    _select_venue_it = "//span[@class='mat-option-text'][normalize-space()='ICA_2021']"

    def enter_venue_name(self, v_n):
        self.hold_wait()
        self.elementClick(self._select_venue, locatorType="xpath")
        # self.hold_wait()
        # self.backspace_clear(self._select_venue, locatorType="xpath")
        self.hold_wait()
        # self.sendKeys(v_n, self._choose_venue, locatorType="xpath")
        # self.hold_wait()
        self.elementClick(self._select_venue_it, locatorType="xpath")
        self.click_out()
        self.hold_wait()

    _click_out = "//body"

    def click_out(self):
        self.elementClick(self._click_out, locatorType="xpath")

    _duration = "//mat-select[@placeholder='Duration']"
    # _select_duration_slot = "//span[contains(text(),'1 hour')]"
    _select_duration_slot = "//mat-select[@placeholder='Duration']//span[contains(text(),'8 hours')]"

    # def set_duration(self):
    #     self.elementClick(self._duration, locatorType="xpath")
    #     self.hold_wait()
    #
    #     self.elementClick(self._select_duration_slot)
    #     self.hold_wait()

    _start_date = "//input[@data-placeholder='Start Date']"
    _start_time = "//input[@data-placeholder='Start time']"

    _end_date = "//input[@data-placeholder='End Date']"
    _end_time = "//input[@data-placeholder='End time']"

    _start_date_error = "//mat-error[contains(text(),'Start date should be greater than ')]"
    def choose_date_and_time(self, s_date, s_time, e_date, e_time):
        # self.select_floor()

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

        # start_date_error_msg_appear = self.isElementPresent(self._start_date_error, locatorType="xpath")
        # txt = start_date_error_msg_appear.text
        # print(txt)
        # if start_date_error_msg_appear == True:
        #     starting_with = txt[:34]
        #     print(starting_with)
        #     return starting_with

    _time_zone = "//input[@data-placeholder='Timezone']"

    # _time_zone_name = "//span[normalize-space()='Africa/Dar_es_Salaam']"

    def select_timezone(self, country_name):
        # self.elementClick(self._time_zone, locatorType="xpath")
        self.hold_wait()
        self.backspace_clear(self._time_zone, locatorType="xpath")
        self.hold_wait()
        self.sendKeys(country_name, self._time_zone, locatorType="xpath")
        self.hold_wait()
        self.click_out()

    # _draw_type = "//span[contains(text(),'Dot')]"
    # _draw_type_dot = "//mat-option[@role='option'][1]"
    _draw_type = "//mat-select[@placeholder='Draw Type']"
    _draw_type_Line = "//span[@class='mat-option-text'][normalize-space()='Line']"
    _draw_type_Dot = "//span[@class='mat-option-text'][normalize-space()='Dot']"
    _draw_type_Trail = "//span[@class='mat-option-text'][normalize-space()='Trail']"

    def select_draw_style(self):
        self.elementClick(self._draw_type, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._draw_type_Trail, locatorType="xpath")  # change this xpath as per requirements
        self.hold_wait()


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

    # def click_search(self):
    #     self.elementClick(self._search_, locatorType="xpath")
    #     self.hold_wait()



    # _select_all_users = "//label[@for='mat-checkbox-5-input']//div[@class='mat-checkbox-inner-container']"
    # _select_all_users = "//div[@class='map-all-tree-users-select']//div[@class='mat-checkbox-inner-container']"
    _select_all_users = "//div[@class='map-all-tree-users-select']"

    def select_all_users(self):
        # self.waitForElement(self._select_all_users, locatorType="xpath", timeout=10, pollFrequency=0.5)
        self.hold_wait()
        self.elementClick(self._select_all_users, locatorType="xpath")
        self.hold_wait()


    _play_arrow = "//mat-icon[normalize-space()='play_arrow']"
    def play_btn(self):
        # self.isElementPresent(self._play_arrow, locatorType="xpath")
        self.hold_wait()
        try:
            self.elementClick(self._play_arrow, locatorType="xpath")
            self.hold_wait()
        except:
            print("sdd")
        self.screen_shot(file="test_3_3_1_filter_sessions_by_time_playback")




    _select_venue_for_show_zone = "//mat-select[@placeholder='Venue']"
    _select_venue_it_for_show_zone = "//span[@class='mat-option-text'][normalize-space()='TDK_HQ_Nihonbashi']"

    def enter_venue_name_for_show_zone(self):
        self.hold_wait()
        self.elementClick(self._select_venue_for_show_zone, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_venue_it_for_show_zone, locatorType="xpath")
        self.click_out()
        self.hold_wait()


    _sel_flr = "//label[@class='map-selected-floor']//span[contains(text(), '')]"
    # _set_floor = "//label[@class='map-selected-floor']//span[contains(text(), ' 26')]"
    _set_floor = "//div[@class='leaflet-control-layers-base']/label//div//span[contains(text(), '28F')]"
    _toggle_show_zone = "//div[@class='mat-slide-toggle-bar']"
    def show_zones(self):
        self.select_analytic_playback_tab()
        self.enter_venue_name_for_show_zone()
        self.elementClick(self._toggle_show_zone, locatorType="xpath")
        # self.elementClick(self._sel_flr, locatorType="xpath")
        self.elementClick(self._set_floor, locatorType="xpath")
        self.hold_wait()
        get_floor_number_element = self.getElement(self._set_floor, locatorType="xpath")
        get_floor_number_txt = get_floor_number_element.text
        print(get_floor_number_txt)
        self.screen_shot(file="test_3_3_2_show_zones")
        return get_floor_number_txt