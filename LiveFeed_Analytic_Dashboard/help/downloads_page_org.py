from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging


class DownloadsTabPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _select_analytics_tab = "//span[contains(text(),'Analytics')]"
    _select_downloads_tab = "//a[contains(text(),'Downloads')]"

    def select_analytic_downloads_tab(self):
        self.hold_wait()
        self.elementClick(self._select_analytics_tab, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_downloads_tab, locatorType="xpath")
        self.hold_wait()


    _open_drop_down = "(//div[contains(@class,' ui-widget ui-state-default ui-corner-all')])[1]"
    _distance_drop_down = "//li[@aria-label='Distances']"

    def select_distance(self):
        self.elementClick(self._open_drop_down, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._distance_drop_down, locatorType="xpath")
        self.hold_wait()

    _movements_drop_down = "//li[@aria-label='Movements']"
    def select_movement(self):
        self.elementClick(self._open_drop_down, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._movements_drop_down, locatorType="xpath")
        self.hold_wait()

    _playback_drop_down = "//li[@aria-label='Playback']"
    def select_playback(self):
        self.elementClick(self._open_drop_down, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._playback_drop_down, locatorType="xpath")
        self.hold_wait()

    _assets_playback_drop_down = "//li[@aria-label='Assets Playback']"
    def select_assets_playback(self):
        self.elementClick(self._open_drop_down, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._assets_playback_drop_down, locatorType="xpath")
        self.hold_wait()


    _select_venue = "(//div[contains(@class,' ui-widget ui-state-default ui-corner-all')])[2]"
    _input_text = "((//div[contains(@class,' ui-widget ui-state-default ui-corner-all')])[2]//input[@type='text'])[2]"
    _click = "//li[@role='option']"
    def select_venue(self, venue_name):
        self.elementClick(self._select_venue, locatorType="xpath")
        self.sendKeys(venue_name, self._input_text, locatorType="xpath")
        self.elementClick(self._click, locatorType="xpath")
        self.hold_wait()

    _click_out = "//body"
    def click_out(self):
        self.elementClick(self._click_out, locatorType="xpath")


    # 01/09/2023 - 01/14/2023
    # MM/DD/YYYY - MM/DD/YYYY
    _date_range_select_for_wipe = "//p-calendar[@selectionmode='range']"
    _date_range_select = "//button[@type='button']"
    _date_text_box = "//span[contains(@class,'ui-calendar ui-calendar-w-btn')]//input[@type='text']"
    def add_dates(self, dates):
        # self.elementClick(self._date_range_select, locatorType="xpath")
        # self.hold_wait()
        # # dt_clear = self.getElement(self._date_range_select, locatorType="xpath")
        # # dt_clear.clear()
        # self.hold_wait()
        # # self.backspace_clear(self._date_range_select, locatorType="xpath")
        # self.hold_wait()
        # self.sendKeys(dates, self._date_range_select, locatorType="xpath")
        # self.hold_wait()
        # self.backspace_clear(self._date_range_select, locatorType="xpath")
        # self.hold_wait()
        # self.sendKeys(dates, self._date_range_select, locatorType="xpath")
        #
        # self.hold_wait()
        # self.click_out()

        self.elementClick(self._date_text_box, locatorType="xpath")
        self.hold_wait()
        self.backspace_clear(self._date_text_box, locatorType="xpath")
        self.hold_wait()
        self.sendKeys(dates, self._date_text_box, locatorType="xpath")
        self.hold_wait()
        self.click_out()


    def click_dates(self):
        self.elementClick(self._date_text_box, locatorType="xpath")
        self.hold_wait()


    _all_dates_xpath = "//table[contains(@class, 'ui-datepicker-calendar')]//tbody//td"
    _left_windows_dates_xpath = "(//table[contains(@class, 'ui-datepicker-calendar')])[1]//tbody//td"
    _right_windows_dates_xpath = "(//table[contains(@class, 'ui-datepicker-calendar')])[2]//tbody//td"
    _left_btn = "//span[contains(@class, 'ui-datepicker-prev-icon pi pi-chevron-left')]"
    _right_btn = "//span[contains(@class, 'ui-datepicker-next-icon pi pi-chevron-right')]"
    # _month_name_xpath = "//span[contains(text(),'November')]"
    # _month_name_xpath = "//div[contains(@class,'ui-datepicker-title')]//span[contains(text(),'')]"
    # _month_name_xpath = "//div[contains(@class,'ui-datepicker-title')]//span[contains(text(),'')][1]//[1]"
    _left_window_month_xpath = "(//div[contains(@class,'ui-datepicker-title')]//span[contains(text(),'')])[1]"
    _left_window_year_xpath = "(//div[contains(@class,'ui-datepicker-title')]//span[contains(text(),'')])[2]"
    _right_window_month_xpath = "(//div[contains(@class,'ui-datepicker-title')]//span[contains(text(),'')])[3]"
    _right_window_year_xpath = "(//div[contains(@class,'ui-datepicker-title')]//span[contains(text(),'')])[4]"

    _start_time_xpath = "//input[@formcontrolname='startTime']"
    _end_time_xpath = "//input[@formcontrolname='endTime']"

    _click_add_btn_xpath = "//div[@class='timerange-footer']//span[contains(text(),'Add')]"

    _click_search_btn_xpath = "//div[@class='mov-input']//span[contains(text(),'Search')]"

    def select_start_date(self, desired_start_date):
        all_dates = self.getElements(self._left_windows_dates_xpath, locatorType="xpath")
        for date_element in all_dates:
            date = date_element.text
            print(date)
            if date == desired_start_date:
                date_element.click()
                self.hold_wait()
                self.hold_wait()
                print(f"start date is selected----")
                break

    def select_end_date(self, desired_end_date):
        all_dates = self.getElements(self._right_windows_dates_xpath, locatorType="xpath")
        for date_element in all_dates:
            date = date_element.text
            print(date)
            if date == desired_end_date:
                date_element.click()
                self.hold_wait()
                self.hold_wait()
                print(f"end date is selected----")
                break

    def select_year_month(self, desired_start_year, desired_start_month, desired_start_date, desired_end_year,
                          desired_end_month, desired_end_date):
        print("We are selecting start/end year to make sure in which side we want to navigate")
        left_window_year_web_element = self.getElement(self._left_window_year_xpath, locatorType="xpath")
        left_window_year_value = int(left_window_year_web_element.text)
        print(f"left year value: {left_window_year_value}")
        print(type(left_window_year_value))

        right_window_year_web_element = self.getElement(self._right_window_year_xpath, locatorType="xpath")
        right_window_year_value = int(right_window_year_web_element.text)
        print(f"right year value: {right_window_year_value}")
        # print(type(right_window_year_value))

        print("We are selecting start/end month to make sure in which side we want to navigate")
        left_window_month_web_element = self.getElement(self._left_window_month_xpath, locatorType="xpath")
        left_window_month_value = left_window_month_web_element.text
        print(f"left month value: {left_window_month_value}")

        right_window_month_web_element = self.getElement(self._right_window_month_xpath, locatorType="xpath")
        right_window_month_value = right_window_month_web_element.text
        print(f"right month value: {right_window_month_value}")

        if (desired_start_year == left_window_year_value) and (desired_start_month == left_window_month_value):
            self.select_start_date(desired_start_date)
        else:
            while (desired_start_year != left_window_year_value) or (desired_start_month != left_window_month_value):
                print(f"while loop before click: {left_window_year_value}")
                print(f"while loop before click: {left_window_month_value}")
                self.elementClick(self._left_btn, locatorType="xpath") # OR condition for right values btn
                self.hold_wait()
                left_window_year_web_element = self.getElement(self._left_window_year_xpath, locatorType="xpath")
                left_window_year_value = int(left_window_year_web_element.text)

                left_window_month_web_element = self.getElement(self._left_window_month_xpath, locatorType="xpath")
                left_window_month_value = left_window_month_web_element.text

                print(f"while loop after click: {left_window_year_value}")
                print(f"while loop after click: {left_window_month_value}")
                print("left click done")
                # if (desired_start_year <= left_window_year_value) or (left_window_month_value != desired_start_month):
                #     self.elementClick(self._left_btn, locatorType="xpath")
                #     if (desired_start_year == left_window_year_value) and (
                #             desired_start_month == left_window_month_value):
                #         print(
                #             f"if left_window_year_value: {left_window_year_value}, left_window_month_value: {left_window_month_value}")
                #         self.select_start_date(desired_start_date)
                # else:
                #     self.elementClick(self._right_btn, locatorType="xpath")
                if (desired_start_year == left_window_year_value) and (desired_start_month == left_window_month_value):
                    print( f"if left_window_year_value: {left_window_year_value}, left_window_month_value: {left_window_month_value}")
                    self.select_start_date(desired_start_date)

            print("While loop done")
        self.hold_wait()

        # end year_month_date selection
        if (desired_end_year == right_window_year_value) and (desired_end_month == right_window_month_value):
            self.select_end_date(desired_end_date)

        else:

            while (desired_end_year != right_window_year_value) or (desired_end_month != right_window_month_value):
                print(f"while loop before click: {right_window_year_value}")
                print(f"while loop before click: {right_window_month_value}")
                self.elementClick(self._right_btn, locatorType="xpath")
                self.hold_wait()
                right_window_year_web_element = self.getElement(self._right_window_year_xpath, locatorType="xpath")
                right_window_year_value = int(right_window_year_web_element.text)

                right_window_month_web_element = self.getElement(self._right_window_month_xpath, locatorType="xpath")
                right_window_month_value = right_window_month_web_element.text

                print(f"while loop after click: {right_window_year_value}")
                print(f"while loop after click: {right_window_month_value}")
                print("left click done")
                if (desired_end_year == right_window_year_value) and (desired_end_month == right_window_month_value):
                    # if (desired_end_year == right_window_year_value) or (desired_end_month == right_window_month_value):
                    print(
                        f"if right_window_year_value: {right_window_year_value}, right_window_month_value: {right_window_month_value}")
                    # all_dates = self.getElements(self._left_windows_dates_xpath, locatorType="xpath")
                    # for date_element in all_dates:
                    #     date = date_element.text
                    #     print(date)
                    #     if date == desired_start_date:
                    #         self.hold_wait()
                    #         date_element.click()
                    #         self.hold_wait()
                    #         self.hold_wait()
                    #         print(f"start date is selected----")
                    #         break
                    self.select_end_date(desired_end_date)

            print("While loop done")
        self.hold_wait()


    # _checkbox_for_download = "//label[@for='mat-checkbox-1-input']"
    # def select_all_files(self):
    #     self.waitForElement(self._checkbox_for_download, locatorType="xpath")
    #     self.elementClick(self._checkbox_for_download, locatorType="xpath")
    #     self.hold_wait()
    #
    #
    # _download_button = "//span[normalize-space()='Download selected']"
    # def download_btn(self):
    #     self.elementClick(self._download_button, locatorType="xpath")
    #     self.hold_wait()
    #
