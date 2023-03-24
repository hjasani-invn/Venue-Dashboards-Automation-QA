from selenium.webdriver import Keys

from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging
import os.path


class ContactAnalyticsPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _click_contact_analytics = "//span[normalize-space()='Contact Analytics']"
    # _select_venue = "//input[@placeholder='Search']"
    # _select_venue = '//mat-expansion-panel-header[@role="button"]'
    # _select_venue = "//mat-select[@id='mat-select-0']"
    # _select_venue = "//span[@class='mat-option-text' and contains(text(), 'ICA Calgary')]"
    # _select_venue = "//div[@id='mat-select-value-9']"
    # _select_venue = "//mat-select[@role='combobox']"
    _choose_venue = "//input[@placeholder='Search']"
    #_select_venue_it = "//span[@class='mat-option-text'][normalize-space()='ICA Calgary']"
    _select_venue_it = "//span[@class='mat-option-text'][normalize-space()='ICA_2021']"
    # _start_date = "//div[@class='mat-calendar-body-cell-content mat-focus-indicator'][normalize-space()='1']"
    _start_date = "//input[@id='mat-input-2']"
    _find_s_date = "//input[@aria-haspopup='dialog']"
    _dp_date = "../.."

    _click_out = "//body"

    def click_out(self):
        self.elementClick(self._click_out, locatorType="xpath")

    def open_contact_analytics_tab(self):
        self.elementClick(self._click_contact_analytics, locatorType="xpath")
        self.hold_wait()

    # def enter_venue(self, v_n):
    #     self.hold_wait()
    #     self.elementClick(self._select_venue, locatorType="xpath")
    #     self.hold_wait()
    #     # self.backspace_clear(self._select_venue, locatorType="xpath")
    #     self.hold_wait()
    #     self.sendKeys(v_n, self._choose_venue, locatorType="xpath")
    #     self.hold_wait()
    #     self.elementClick(self._select_venue_it, locatorType="xpath")
    #     self.click_out()
    #     self.hold_wait()

    _select_venue = "(//mat-select[@role='combobox'])[1]"
    def enter_venue(self, v_n):
        self.hold_wait()
        self.elementClick(self._select_venue, locatorType="xpath")
        self.hold_wait()
        # self.elementClick(self._select_venue_it, locatorType="xpath")
        self.sendKeys(v_n, self._select_venue, locatorType="xpath")
        self.click_out()
        self.hold_wait()


    def chose_start_date(self, s_date):
        self.backspace_clear(self._start_date, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._start_date, locatorType="xpath")
        self.hold_wait()
        self.sendKeys(s_date, self._start_date, locatorType="xpath")
        self.hold_wait()
        self.click_out()
        # date_pickers = self.getElements(self._find_s_date, locatorType="xpath")
        # for date_picker in date_pickers:
        #     selection = date_picker.getElement(self._dp_date, locatorType="xpath")
        #     selection_text = selection.get_attribute("innerText")
        #     if 'START' in date_type.upper() and 'START DATE' in selection_text.upper():
        #         date_picker.sendKeys(Keys.CONTROL, 'a')
        #         date_picker.sendKeys(Keys.BACKSPACE)
        #         date_picker.sendKeys(date)
        #

    def clear_fields(self):
        # self.backspace_clear(self._start_date, locatorType="xpath")
        # self.backspace_clear(self._end_date, locatorType="xpath")
        self.backspace_clear(self._max_distance, locatorType="xpath")
        self.backspace_clear(self._min_duration, locatorType="xpath")

        self.hold_wait()

    _end_date = "//input[@id='mat-input-3']"

    def choose_end_date(self, e_date):
        self.backspace_clear(self._end_date, locatorType="xpath")
        self.elementClick(self._end_date, locatorType="xpath")
        self.hold_wait()
        self.sendKeys(e_date, self._end_date, locatorType="xpath")
        self.hold_wait()
        self.click_out()
        self.hold_wait()

    #_max_distance = "//input[@id='mat-input-7']"
    _max_distance = "// input[ @ type = 'number']"
    def select_max_distance(self, enter_max_distance):
        self.backspace_clear(self._max_distance, locatorType="xpath")
        self.sendKeys(enter_max_distance, self._max_distance, locatorType="xpath")
        self.hold_wait()
        self.click_out()
        self.hold_wait()

    _reverse_time_range_snackbar_xpath = "//span[contains(text(),'Time Range is Incorrect!')]"
    def verify_reverse_time_range_message(self):
        snackbar_element = self.getElement(self._reverse_time_range_snackbar_xpath, locatorType="xpath")
        snackbar_text = snackbar_element.text
        print(snackbar_text)
        return snackbar_text


    _time_range_no_morethan_2_months_snackbar_xpath = "//span[contains(text(),'Timerange can not be more than 2 months')]"
    def verify_time_range_no_morethan_2_months_message(self):
        snackbar_element = self.getElement(self._time_range_no_morethan_2_months_snackbar_xpath, locatorType="xpath")
        snackbar_text = snackbar_element.text
        print(snackbar_text)
        return snackbar_text

    _verify_distance_error_message = "//mat-error[@role='alert']"
    def verify_max_distance_message(self):
        snackbar_element = self.getElement(self._verify_distance_error_message, locatorType="xpath")
        snackbar_text = snackbar_element.text
        print(snackbar_text)
        return snackbar_text


    _verify_distance_error_message_if_words = "//mat-error[@role='alert']"
    def verify_max_distance_message_if_words(self):
        snackbar_element = self.getElement(self._verify_distance_error_message_if_words, locatorType="xpath")
        snackbar_text = snackbar_element.text
        print(snackbar_text)
        return snackbar_text


    # _query_id_xpath = "//tbody/tr//td[1]"
    #
    #
    # def get_list_before_search(self):
    #     list_1 = []
    #     queries = self.getElements(self._query_id_xpath, locatorType="xpath")
    #     for query in queries:
    #         print(query.text)
    #         list_1.append(query.text)
    #
    # def get_list_after_search(self):
    #     list_2 = []
    #     queries = self.getElements(self._query_id_xpath, locatorType="xpath")
    #     for query in queries:
    #         print(query.text)
    #         list_2.append(query.text)

    # list_1 = get_list_before_search()
    # list_2 = get_list_after_search()
    #
    # global_list_1 = []
    # global_list_2 = []
    # def make_global(self):
    #     global global_list_1
    #     global global_list_2
    # make_global()
    #
    # def print_list(self):
    #     print(global_list_1)
    #     print(global_list_2)



    _min_duration = "//input[@id='mat-input-8']"

    _update_query = "//input[@maxlength='256']"

    def update_query_name(self, query):
        self.open_contact_analytics_tab()
        self.backspace_clear(self._update_query, locatorType="xpath")
        self.sendKeys(query, self._update_query, locatorType="xpath")
        self.hold_wait()
        self.click_out()


    _click_search_btn = "//button[normalize-space()='Search']"
    def click_search_btn(self):
        self.elementClick(self._click_search_btn, locatorType="xpath")
        self.hold_wait()
        self.hold_wait()


    _pop_msg = "//span[contains(text(),'No Contact Data found for the given Search conditi')]"
    _query_generated_xpath = "//span[contains(text(),'Query')]"
    _query_field = "//tbody/tr[1]//td[2]"
    def is_popup(self,query_name):
        try: # query not generated
            visible = self.getElement(self._pop_msg, locatorType="xpath")
            self.driver.execute_script('arguments[0].dispatchEvent(new Event("click"))', visible)
            print(visible.text)
            return visible.text
        except: # Query Generated
            # snackbar_msg = self.getElement(self._query_generated_xpath, locatorType="xpath")
            # snackbar_msg_txt = snackbar_msg.text
            # starts_with = snackbar_msg_txt[:5]
            # ends_with = snackbar_msg_txt[-9:]
            # print(starts_with)
            # print(ends_with)
            #
            # print(snackbar_msg_txt)
            self.hold_wait()
            self.hold_wait()
            # self.update_query_name(query="overwrite")
            self.backspace_clear(self._update_query, locatorType="xpath")
            self.sendKeys(query_name, self._update_query, locatorType="xpath")
            self.hold_wait()
            self.click_out()
            self.hold_wait()
            # return starts_with

    def snack_bar_message(self):
        snackbar_msg = self.getElement(self._query_generated_xpath, locatorType="xpath")
        print(snackbar_msg)
        snackbar_msg_txt = snackbar_msg.text
        print(snackbar_msg_txt)
        if "Query" in snackbar_msg_txt:  #if query generated
            starts_with = snackbar_msg_txt[:5]
            ends_with = snackbar_msg_txt[-9:]
            print(starts_with)
            print(ends_with)
            return starts_with
        elif "No Contact Data found" in snackbar_msg_txt:  # if not generated
            starts_with = snackbar_msg_txt[:21]
            # ends_with = snackbar_msg_txt[-9:]
            print(starts_with)
            # print(ends_with)
            return starts_with


    def is_pop_up_2(self):
        # snackbar_msg = self.getElement(self._query_generated_xpath, locatorType="xpath")
        snackbar_msg = self.getElement(self._pop_msg, locatorType="xpath")
        snackbar_msg_txt = snackbar_msg.text
        # starts_with = snackbar_msg_txt[:5]
        starts_with = snackbar_msg_txt[:21]

        ends_with = snackbar_msg_txt[-9:]
        print(starts_with)
        print(ends_with)

        print(snackbar_msg_txt)
        # self.hold_wait()
        # self.hold_wait()
        # # self.update_query_name(query="overwrite")
        # self.backspace_clear(self._update_query, locatorType="xpath")
        # self.sendKeys(query_name, self._update_query, locatorType="xpath")
        # self.hold_wait()
        # self.click_out()
        # self.hold_wait()
        return starts_with
