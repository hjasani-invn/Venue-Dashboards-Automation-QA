from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging


class MovementAnalyticsTabPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _select_analytics_tab = "//span[contains(text(),'Analytics')]"
    _select_movement_analytic_tab = "//a[contains(text(),'Movement Analytics')]"

    def select_analytic_movement_analytic_tab(self):
        self.elementClick(self._select_analytics_tab, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_movement_analytic_tab, locatorType="xpath")
        # self.hold_wait()

    _select_venue = "//mat-select[@placeholder='Venue']"

    # _select_venue_it = "//span[@class='mat-option-text'][normalize-space()='ICA_2021']"

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

    _select_floor = "//mat-select[@placeholder='Floor']"

    # _select_floor_name = "//mat-select[@placeholder='Floor']/div//span[contains(text(),'Fourth Floor')]"
    def select_floor(self, f_n):
        # self.hold_wait()
        self.sendKeys(f_n, self._select_floor, locatorType="xpath")
        self.hold_wait()

    _add_time_range = "//div[@class='mov-input']//span[contains(text(),'Add timerange')]"

    def add_time_range(self):
        self.elementClick(self._add_time_range, locatorType="xpath")
        self.hold_wait()

    # _dates_xpath = "//table[starts-with(@class,'ui-datepicker-calendar')]//a"
    # def sel_dates(self):
    #     all_dates = self.getElements(self._dates_xpath, locatorType="xpath")
    #     for date_element in all_dates:
    #         data = date_element.text
    #         # data = self.get_text(self._dates_xpath, locatorType="xpath")
    #         print(data)
    #         if data == '25':
    #             date_element.click()
    #             break

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
                          desired_end_month, desired_end_date, start_time, end_time):
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

        # if: 21 January 2023
        # else: 21 December 2022
        # desired_start_year = 2022
        # desired_start_month = "November"
        # desired_start_year = 2022
        # desired_start_month = "November"
        # desired_start_date = 1

        if desired_start_year == left_window_year_value and (desired_start_month == left_window_month_value):
            # all_dates = self.getElements(self._left_windows_dates_xpath, locatorType="xpath")
            # for date_element in all_dates:
            #     date = date_element.text
            #     print(date)
            #     if date == desired_start_date:
            #         date_element.click()
            #         self.hold_wait()
            #         self.hold_wait()
            #         print(f"start date is selected----")
            #         break
            self.select_start_date(desired_start_date)
        else:

            while (desired_start_year != left_window_year_value) or (desired_start_month != left_window_month_value):
                print(f"while loop before click: {left_window_year_value}")
                print(f"while loop before click: {left_window_month_value}")
                self.elementClick(self._left_btn, locatorType="xpath")
                self.hold_wait()
                left_window_year_web_element = self.getElement(self._left_window_year_xpath, locatorType="xpath")
                left_window_year_value = int(left_window_year_web_element.text)

                left_window_month_web_element = self.getElement(self._left_window_month_xpath, locatorType="xpath")
                left_window_month_value = left_window_month_web_element.text

                print(f"while loop after click: {left_window_year_value}")
                print(f"while loop after click: {left_window_month_value}")
                print("left click done")
                if (desired_start_year == left_window_year_value) and (desired_start_month == left_window_month_value):
                    print(
                        f"if left_window_year_value: {left_window_year_value}, left_window_month_value: {left_window_month_value}")
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
                    self.select_start_date(desired_start_date)

            print("While loop done")
        self.hold_wait()

        # end month working code:
        # 13 February 2023
        # desired_end_year = 2023
        # desired_end_month = "February"
        if (desired_end_year == right_window_year_value) and (desired_end_month == right_window_month_value):
            # all_dates = self.getElements(self._right_windows_dates_xpath, locatorType="xpath")
            # for date_element in all_dates:
            #     date = date_element.text
            #     print(date)
            #     if date == '13':
            #         date_element.click()
            #         self.hold_wait()
            #         self.hold_wait()
            #         print(f"end date is selected----")
            #         break
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

        # select time range
        self.backspace_clear(self._start_time_xpath, locatorType="xpath")
        self.sendKeys(start_time, self._start_time_xpath, locatorType="xpath")
        self.backspace_clear(self._end_time_xpath, locatorType="xpath")
        self.sendKeys(end_time, self._end_time_xpath, locatorType="xpath")

        self.elementClick(self._click_add_btn_xpath, locatorType="xpath")
        self.hold_wait()

        self.elementClick(self._click_search_btn_xpath, locatorType="xpath")
        self.hold_wait()
        self.hold_wait()


    _drop_down_xpath_for_by_date_test_case = "//div[@class='inputs-group']//mat-select[@role='combobox']"
    _user_text_element = "//span[@class='mat-option-text']"
    _by_date_toggle_xpath = "//div[@class='mat-slide-toggle-bar']"
    def select_user_drop_down_for_users(self):

        self.elementClick(self._drop_down_xpath_for_by_date_test_case, locatorType="xpath")
        users = self.getElements(self._user_text_element, locatorType="xpath")
        user_list = []
        for user in users:
            # print(f" All Us: {user.text}")
            user_list.append(user.text)
        self.hold_wait()
        # print(f"list: - {user_list}")
        self.click_out()

        if not user_list:
            print("List is empty")
        else:
            print(f"there are {len(user_list)} number of users available")

        # make sure "Khendrickson" user available in list
        try:
            assert "Khendrickson" in user_list
            print("user with name 'Khendrickson' is available in list of Users")
        except:
            print("user with name 'Khendrickson' are not available in list of Users")

        # toggle bydate
        self.elementClick(self._by_date_toggle_xpath, locatorType="xpath")
        self.hold_wait()
        self.hold_wait()
        self.hold_wait()

    def screen_shot_for_test_3_6_1_populate_movement_analytic_time_filter(self):
        self.screen_shot(file="test_3_6_1_populate_movement_analytic_time_filter")

    def screen_shot_for_test_3_6_2_movement_analytics_by_date(self):
        self.screen_shot(file="test_3_6_2_movement_analytics_by_date")


# 21 November 2022
#     def sel_month(self):
#         pass
# desired_month = 'November'
# desired_year = 2022
# global chopped_month_list, start_current_year, get_start_month
# start_year = self.getElement(self._year_name_xpath_1, locatorType="xpath")
# start_current_year = int(start_year.text)
# print(f"year: {start_current_year}")
#
# month_list = []
# print(f"1-list {month_list}")


# while 'November' not in month_list:
#     # self.elementClick(self._left_btn, locatorType="xpath")
#     months_name = self.getElements(self._month_name_xpath_1, locatorType="xpath")
#     for m in months_name:
#         month_list.append(m.text)
#         print(f"2-list {month_list}")
#     # self.elementClick(self._left_btn, locatorType="xpath")
#     self.hold_wait()
#     self.hold_wait()
#
# print(f" this is month list:: {month_list}")

# start_current_year = int(month_list[1])
# end_current_year = int(month_list[3])
# print(f"start_current_year: {start_current_year}")
# # print(f"start_current_year_type: {type(start_current_year)}")
# print(f"end_current_year: {end_current_year}")

# while desired_year < start_current_year:


# chopped_month_list = month_list[-4:]
# print(f"chopped_month_list: {chopped_month_list}")
#
# get_start_month = chopped_month_list[0]
# get_end_month = chopped_month_list[2]
# print(f"get_start_year: {get_start_month}")
# print(f"get_end_year: {get_end_month}")
#
# get_start_year = chopped_month_list[1]
# get_end_year = chopped_month_list[3]
# print(f"get_start_year: {get_start_year}")
# print(f"get_end_year: {get_end_year}")

# while desired_year < start_current_year:
#     self.elementClick(self._left_btn, locatorType="xpath")
#     if (desired_year == start_current_year):
#         print(f"desired year={desired_year} and start_current_year={start_current_year}")
#         self.hold_wait()


"""

        all_dates = self.getElements(self._all_dates_xpath, locatorType="xpath")
        for date_element in all_dates:
            date = date_element.text
            if date == '21':
                date_element.click()
                self.hold_wait()
                self.hold_wait()
                break
"""

# chopped_month_list = month_list[-4:]
# print(f"chopped_month_list: {chopped_month_list}")
# get_start_year = chopped_month_list[1]
# get_end_year = chopped_month_list[3]
# print(f"get_start_year: {get_start_year}")
# print(f"get_end_year: {get_end_year}")
