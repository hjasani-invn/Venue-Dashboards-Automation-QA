import os
import random
import time
import pyautogui

from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from screeninfo import get_monitors



class MoveEntriesPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.single = None
        log = cl.customLogger(logging.DEBUG)

    # LOCATORS:
    _admin_btn = "//span[contains(text(),'Admin')]"

    def click_admin(self):
        self.elementClick(self._admin_btn, locatorType="xpath")

    _drop_down = "//div[@title='Admin']//span[@class='fa toggle-expand fa-angle-down']"
    _expanded = "//div[@title='Admin']"

    def check_admin_dropdpwn(self):
        pass
        # get_element = self.getElement(self._drop_down, locatorType="xpath")
        # get_attribute = get_element.get_attribute("class")
        # print(f"attribute name:- {get_attribute}")
        # if "down" in get_attribute:
        # self.elementClick(self._drop_down, locatorType="xpath")
        # else:
        #     print("no need to click on drop down, admin is already open")

        # get_element_name = self.elementClick(self._expanded, locatorType="xpath")
        # # get_attribute_name = get_element_name.get_attribute("class")
        # # print(f"attribute name:- {get_attribute_name.text}")
        # txt = get_element_name.text
        # print(f"txt is:- {txt}")

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
        self.backspace_clear(self._search_venue_name, locatorType="xpath")
        self.sendKeys(venue_name, self._search_venue_name, locatorType="xpath")
        self.elementClick(self._select_venue, locatorType="xpath")
        self.hold_wait()

    _select_floor = "//span[contains(text(),'Fourth Floor')]"

    def select_floor(self):
        self.elementClick(self._select_floor, locatorType="xpath")
        self.hold_wait()

    _access_point_btn = "//button[contains(text(),'Access points lists')]"

    def click_access_point_btn(self):
        self.elementClick(self._access_point_btn, locatorType="xpath")

    _click_wifi_in_header = "//span[contains(text(),'Wifi')]"

    def click_wifi_btn(self):
        # el = self.elementClick(self._click_wifi_in_header, locatorType="xpath")
        el = self.getElement(self._click_wifi_in_header, locatorType="xpath")
        txt = el.text
        print(txt)
        self.elementClick(self._click_wifi_in_header, locatorType="xpath")

    _source_list_mac_xpath_1 = "(//three-pick-list//div[@class='pick-list-wrapper'])[2]//ul//li"
    # _white_list_space = "(//three-pick-list//div[@class='pick-list-wrapper'])[1]//ul"
    _white_list_space = "(//three-pick-list//div[@class='pick-list-wrapper'])[1]"
    _temp_source_list_xpath = "(//three-pick-list//div[@class='pick-list-wrapper'])[2]//ul//li[5]"
    # _temp_white_list_xpath = "(//three-pick-list//div[@class='pick-list-wrapper'])[1]//ul//li[1]"
    _temp_white_list_xpath = "(//ul[@class='pick-list'])[1]"

    def without_arrow_source_to_white(self):
        # sl_elements = self.getElements(self._source_list_mac_xpath_1, locatorType="xpath")
        # # for i in sl_elements:
        # #     txt = i.text
        # #     print(f"this is for loop mac text: {txt}")
        # #     time.sleep(2)
        # count = 2  # only two MAC Addresses will be moved as per requirement
        # s_1_list = []
        # while count >= 1:  # >=1
        #     s_1 = sl_elements[random.randint(0, len(sl_elements) - 1)]
        #     print(f"this is s_1:- {s_1}")
        #     print(s_1)
        #     s_1_list.append(s_1)
        #     # self.elementClick(self._source_list_mac_xpath_1, locatorType="xpath")
        #
        #
        #     # for element in s_1:
        #     #     # s_clicked = self.elementClick(self._source_list_mac_xpath_1, locatorType="xpath")
        #     #     print(element)
        #
        #     # clicked = s_1.click()
        #     # print(f"this is MAC: {s_clicked.text}")
        #     time.sleep(1)
        #     # self.elementClick(self._source_list_mac_xpath_1, locatorType="xpath")
        #     # self.click_and_drag(_white_list_space)
        #     # s_1 = self.getElement(self._source_list_mac_xpath_1, locatorType="xpath")
        #     # t_1 = self.getElement(self._white_list_space, locatorType="xpath")
        #
        #     # for i in sl_elements:
        #     #     i = self.getElement(self._white_list_space, locatorType="xpath")
        #     # self.click_and_drag(t_1)
        #     # self.drag_and_drop(s_1, t_1)
        #     # time.sleep(5)
        #     count -= 1
        # print(s_1_list)
        # target1 = self.getElement(self._white_list_space, locatorType="xpath")
        # for s_1_list_element in s_1_list:
        #     source1 = s_1_list_element.click()
        #     taext = s_1_list_element.text
        #     print(f"s_1_element_list: {taext}")
        #     time.sleep(1)
        #     self.drag_drop(s_1_list_element, target1)
        #     time.sleep(1)


        src = self.getElement(self._source_list_mac_xpath_1, locatorType="xpath")
        trg = self.getElement(self._white_list_space, locatorType="xpath")
        time.sleep(3)
        self.drag_drop(src, trg)
        time.sleep(5)


    _from_source_to_white = "(//div[@class='pick-list-buttons'])[1]//i[@class='fa fa-angle-left']"
    _source_list_mac_xpath = "(//three-pick-list//div[@class='pick-list-wrapper'])[2]//ul//li"

    def move_mac_from_source_to_white(self):
        sl_elements = self.getElements(self._source_list_mac_xpath, locatorType="xpath")
        '''
        sl_macs=[]
        for one in sl_elements:
            sl_macs.append(one.text)

        # chosen_mac = random.choices(sl_macs)
        chosen_mac = random.sample(sl_macs, k=2)
        print(f"random sl mac address: {chosen_mac}")
        print(f"{type(chosen_mac)}")
        for one in chosen_mac:
            print(f"my type: {type(one)}")

        chosen_element = random.sample(sl_elements, k=2)
        print(f"my type: {type(chosen_element)}")
        print(f"random sl mac address: {chosen_element}")
        '''
        # for single in chosen_element:
        #     self.elementClick(self.single, locatorType="xpath")
        #     print(f"element clicked {single}")

        count = 2  # only two MAC Addresses will be moved as per requirement
        while count >= 1:
            l = sl_elements[random.randint(0, len(sl_elements) - 1)]
            print(f"this is l:- {l}")
            l.click()
            time.sleep(3)
            self.elementClick(self._from_source_to_white, locatorType="xpath")
            time.sleep(3)
            count -= 1

    _from_source_to_ignore = "(//div[@class='pick-list-buttons'])[2]//i[@class='fa fa-angle-right']"

    def move_mac_from_source_to_ignore(self):
        sl_elements = self.getElements(self._source_list_mac_xpath, locatorType="xpath")

        count = 2  # only two MAC Addresses will be moved as per requirement
        while count >= 1:
            time.sleep(2)
            l = sl_elements[random.randint(0, len(sl_elements) - 1)]
            print(f"this is l:- {l}")
            l.click()
            time.sleep(3)
            self.elementClick(self._from_source_to_ignore, locatorType="xpath")
            time.sleep(3)
            count -= 1

    _white_to_source = "(//div[@class='pick-list-buttons'])[1]//i[@class='fa fa-angle-double-right']"
    _ignore_to_source = "(//div[@class='pick-list-buttons'])[2]//i[@class='fa fa-angle-double-left']"

    def all_mac_move_to_source(self):
        #   white to source
        time.sleep(2)
        self.elementClick(self._white_to_source, locatorType="xpath")
        time.sleep(2)
        #     ignore to source
        self.elementClick(self._ignore_to_source, locatorType="xpath")
        time.sleep(2)


    _save_btn = "//button[normalize-space()='Save']"
    def click_save_btn(self):
        self.elementClick(self._save_btn, locatorType="xpath")
        time.sleep(3)
