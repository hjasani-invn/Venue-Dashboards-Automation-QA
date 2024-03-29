import os
import random
import time
import pyautogui
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By

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

    _click_cancel_button = "//span[contains(@class, 'p-dialog-header-close-icon')]"

    def cancel_btn(self):
        self.elementClick(self._click_cancel_button, locatorType="xpath")

    _white_list_upload_btn = "(//three-pick-list//div[@class='pick-list-wrapper'])[1]//div/button[contains(text(),' Upload ')]"

    def upload_white_list_csv(self):
        time.sleep(2)
        self.elementClick(self._white_list_upload_btn, locatorType="xpath")
        time.sleep(1)

        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
        print(ROOT_DIR)
        time.sleep(1)
        CONFIG_PATH = os.path.join(ROOT_DIR, 'ICA_MultiFloor_WL_2023-02-22T19_46_13.724Z.csv')
        print(CONFIG_PATH)
        time.sleep(1)
        pyautogui.typewrite(CONFIG_PATH, interval=0.10)
        time.sleep(1)
        pyautogui.press('return')

    _source_list_upload_btn = "(//three-pick-list//div[@class='pick-list-wrapper'])[2]//div/button[contains(text(),' Upload ')]"

    def upload_source_list_csv(self):
        time.sleep(2)
        self.elementClick(self._source_list_upload_btn, locatorType="xpath")
        time.sleep(1)

        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
        print(ROOT_DIR)
        time.sleep(1)
        CONFIG_PATH = os.path.join(ROOT_DIR, 'ICA_MultiFloor_SL_2023-02-22T19_20_32.647Z.csv')
        print(CONFIG_PATH)
        time.sleep(1)
        pyautogui.typewrite(CONFIG_PATH, interval=0.10)
        time.sleep(1)
        pyautogui.press('return')

    _ignore_list_upload_btn = "(//three-pick-list//div[@class='pick-list-wrapper'])[3]//div/button[contains(text(),' Upload ')]"

    def upload_ignore_list_csv(self):
        time.sleep(2)
        self.elementClick(self._ignore_list_upload_btn, locatorType="xpath")
        time.sleep(1)

        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
        print(ROOT_DIR)
        time.sleep(1)
        CONFIG_PATH = os.path.join(ROOT_DIR, 'ICA_MultiFloor_SL_2023-02-22T19_20_32.647Z.csv')
        print(CONFIG_PATH)
        time.sleep(1)
        pyautogui.typewrite(CONFIG_PATH, interval=0.10)
        time.sleep(1)
        pyautogui.press('return')

    _white_pick_list = "(//three-pick-list//div[@class='pick-list-wrapper'])[1]//ul//li"

    def check_white_macs_available(self):
        print("check white macs are available, if not available upload csv")
        white_li_tags = self.getElements(self._white_pick_list, locatorType="xpath")
        num_white_li_tags = len(white_li_tags)
        print(f"Number of white 'li' tags: {num_white_li_tags}")
        if num_white_li_tags == 0:
            self.upload_white_list_csv()
        else:
            print("MACS are available, test runs next step")

    _source_pick_list = "(//three-pick-list//div[@class='pick-list-wrapper'])[2]//ul//li"

    def check_source_macs_available(self):
        print("check source macs are available, if not available upload csv")
        source_li_tags = self.getElements(self._source_pick_list, locatorType="xpath")
        num_source_li_tags = len(source_li_tags)
        print(f"Number of 'li' tags: {num_source_li_tags}")
        if num_source_li_tags == 0:
            self.upload_source_list_csv()
        else:
            print("MACS are available, test runs next step")

    _ignore_pick_list = "(//three-pick-list//div[@class='pick-list-wrapper'])[3]//ul//li"

    def check_ignore_macs_available(self):
        print("check ignore macs are available, if not available upload csv")
        ignore_li_tags = self.getElements(self._ignore_pick_list, locatorType="xpath")
        num_ignore_li_tags = len(ignore_li_tags)
        print(f"Number of 'li' tags: {num_ignore_li_tags}")
        if num_ignore_li_tags == 0:
            self.upload_ignore_list_csv()
        else:
            print("MACS are available, test runs next step")


    _source_list_mac_xpath_1 = "(//three-pick-list//div[@class='pick-list-wrapper'])[2]//ul//li"
    # _white_list_space = "(//three-pick-list//div[@class='pick-list-wrapper'])[1]//ul"
    _white_list_space = "(//three-pick-list//div[@class='pick-list-wrapper'])[1]"
    _temp_source_list_xpath = "(//three-pick-list//div[@class='pick-list-wrapper'])[2]//ul//li[5]"
    # _temp_white_list_xpath = "(//three-pick-list//div[@class='pick-list-wrapper'])[1]//ul//li[1]"
    _temp_white_list_xpath = "(//ul[@class='pick-list'])[1]"

    _source_mac_1 = "//div[contains(text(),'34:A8:4E:E6:51:12')]"
    _white_destination = "(//three-pick-list//div[@class='pick-list-wrapper'])[1]//ul"

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

        # src = self.getElement(self._source_list_mac_xpath_1, locatorType="xpath")
        # trg = self.getElement(self._white_list_space, locatorType="xpath")
        # time.sleep(3)
        # self.drag_drop(src, trg)
        # time.sleep(5)

        print("drag and drop functionality")
        # source1 = self.getElement(self._source_mac_1, locatorType="xpath")
        source1 = self.driver.find_element(By.XPATH, "//div[contains(text(),'34:A8:4E:E6:51:12')]")
        time.sleep(1)
        # target1 = self.getElement(self._white_destination, locatorType="xpath")
        target1 = self.driver.find_element(By.XPATH, "(//three-pick-list//div[@class='pick-list-wrapper'])[1]")
        # action = ActionChains(self.driver)
        # action.drag_and_drop(source1, target1)
        # time.sleep(2)
        try:
            print("-------------inside try-------------")
            action = ActionChains(self.driver)
            action.drag_and_drop(source1, target1).perform()
            time.sleep(7)
            self.driver.close()
        except:
            print("-------------NOT WORKING-------------")

        # print("drag and drop functionality")
        # target1 = self.getElement(self._white_destination, locatorType="xpath")
        # time.sleep(1)
        # source1 = self.getElement(self._source_mac_1, locatorType="xpath")
        # action = ActionChains(self.driver)
        # time.sleep(2)
        # action.drag_and_drop(source1, target1).perform()
        # time.sleep(7)

    _ignore_destination = "(//three-pick-list//div[@class='pick-list-wrapper'])[3]//ul"

    def without_arrow_source_to_ignore(self):
        print("drag and drop functionality")
        target1 = self.getElement(self._ignore_destination, locatorType="xpath")
        # time.sleep(1)
        source1 = self.getElement(self._source_mac_1, locatorType="xpath")
        action = ActionChains(self.driver)
        # time.sleep(2)
        action.drag_and_drop(source1, target1).perform()
        # time.sleep(7)

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

    _white_list_mac_xpath = "(//three-pick-list//div[@class='pick-list-wrapper'])[1]//ul//li"
    _ignore_list_mac_xpath = "(//three-pick-list//div[@class='pick-list-wrapper'])[3]//ul//li"

    def all_mac_move_to_source(self):
        #   white to source
        time.sleep(2)
        self.elementClick(self._white_to_source, locatorType="xpath")
        time.sleep(2)
        #     ignore to source
        self.elementClick(self._ignore_to_source, locatorType="xpath")
        time.sleep(2)

        white_list_macs_moved = self.isElementPresent(self._white_list_mac_xpath, locatorType="xpath")
        ignore_list_macs_moved = self.isElementPresent(self._ignore_list_mac_xpath, locatorType="xpath")
        # if white_list_macs_moved and ignore_list_macs_moved is None:
        #     return True
        return white_list_macs_moved, ignore_list_macs_moved

    _save_btn = "//button[normalize-space()='Save']"

    def click_save_btn(self):
        self.elementClick(self._save_btn, locatorType="xpath")
        time.sleep(3)
