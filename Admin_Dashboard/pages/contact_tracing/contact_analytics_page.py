import random
import time

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
    # _select_venue_it = "//span[@class='mat-option-text'][normalize-space()='ICA Calgary']"
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

    # _max_distance = "//input[@id='mat-input-7']"
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

    def is_popup(self, query_name):
        try:  # query not generated
            visible = self.getElement(self._pop_msg, locatorType="xpath")
            self.driver.execute_script('arguments[0].dispatchEvent(new Event("click"))', visible)
            print(visible.text)
            return visible.text
        except:  # Query Generated
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
        if "Query" in snackbar_msg_txt:  # if query generated
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

    # def check_order(self, lst):
    #     # Extract the numbers or floor names from the list items
    #     extracted = [i[1:] if i[0].isdigit() else i.split()[0] for i in lst]
    #
    #     # Check if the extracted items are sorted in reverse order
    #     # return extracted == sorted(extracted, reverse=True)
    #     # return extracted == sorted(extracted, key=lambda x: int(x[1:]) if x[0].isdigit() else x, reverse=True) # list2-wrong false-should true, list3 true
    #     # extracted = [i for i in extracted if i.isnumeric() or i.startswith('F')] # list2 true, list3 wrong true-should false
    #     # return extracted == sorted(extracted, reverse=True)

    def check_order(self, lst):
        # Define a dictionary to map floor names to integers
        floor_map = {"Main": 0, "P1": -1, "P2": -2}

        # Extract the floor numbers or floor names from the list items
        extracted = []
        for item in lst:
            if item[0].isdigit():
                extracted.append(int(item[:-1]))
            else:
                # Get the floor name prefix (e.g. F, B, P) and remove it from the item
                prefix = item[0]
                floor_name = item[len(prefix):].strip()

                # Map the floor name to an integer, or use 0 for "Main" floor and -1 for "P" floor
                if floor_name == "Main_Floor" or "Main":
                    floor_num = 0
                elif prefix == "P1":
                    floor_num = -1
                elif prefix == "P2":
                    floor_num = -2
                else:
                    floor_num = int(floor_name)

                extracted.append(floor_num)

        # Check if the extracted items are sorted in reverse order
        return extracted == sorted(extracted, reverse=True)


    _search_icon_xpath = "//button[contains(@class, 'btn-success')]"
    _paginator = "//button[contains(@class, 'paginator-navigation-next')]"
    _select_heatmap = "//div[contains(text(),'Heatmap')]"
    _span_txt = "//div[contains(@class, 'controls-group')][1]//button//span"

    def click_search_icon(self):
        """below commented code also works"""
        # number_of_searches_icons_elements = self.getElements(self._search_icon_xpath, locatorType="xpath")
        # print(f"Number of search icons available: {len(number_of_searches_icons_elements)}")
        # # choose_random_search_icon = random.choice(number_of_searches_icons_elements)
        # # print(f"chose random search icon: {choose_random_search_icon}")
        # # one = number_of_searches_icons_elements[0].click()
        # while len(number_of_searches_icons_elements) == 0:
        #     self.elementClick(self._paginator, locatorType="xpath")
        #     time.sleep(1)
        #     number_of_searches_icons_elements = self.getElements(self._search_icon_xpath, locatorType="xpath")
        #     time.sleep(1)
        #     print(f"found search btn")
        #     if len(number_of_searches_icons_elements) > 0:
        #         break

        """optimized code"""
        # Use a for loop to retry the search button click a maximum of 10 times
        global search_icon_elements
        for i in range(10):
            # Get the list of search icon elements
            search_icon_elements = self.getElements(self._search_icon_xpath, locatorType="xpath")
            # If the search icon elements are found, print the number of elements and break the loop
            if search_icon_elements:
                print(f"Number of search icons available: {len(search_icon_elements)}")
                break
            # If the search icon elements are not found, click the paginator and wait for 1 second
            self.elementClick(self._paginator, locatorType="xpath")
            time.sleep(1)

        # Print a message when the search icon is found
        if search_icon_elements:
            print("Search icon found!")
        else:
            print("Search icon not found after 10 retries.")

        # one = random.choice(number_of_searches_icons_elements).click()
        one = random.choice(search_icon_elements).click()
        # print(f"this is one: {one}")
        time.sleep(50)
        self.scroll_to_element(self._select_heatmap, locatorType="xpath")
        time.sleep(1)
        self.elementClick(self._select_heatmap, locatorType="xpath")
        time.sleep(5)
        scroll_to_vertical_floors = self.scroll_to_element(self._span_txt, locatorType="xpath")
        get_elements = self.getElements(self._span_txt, locatorType="xpath")
        floor_list = []
        for a in get_elements:
            get_elements_attribute = a.get_attribute("title")
            print(f"this is title: {get_elements_attribute}")
            floor_list.append(get_elements_attribute)
        time.sleep(5)
        print(floor_list)
        lst = floor_list
        result = self.check_order(lst)
        print(f"final result: {result}")
        return result
        # lst = ["F4", "F3", "F2", "F1", "P1", "P2"]
        # result = self.check_order(lst)
        # print(result)  # True
