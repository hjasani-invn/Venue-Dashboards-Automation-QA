import os
import time
import pyautogui
pyautogui.FAILSAFE = False

from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class SourceWhiteIgnoreListPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
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

        # _x = "//body/app/main/pages[@class='ng-star-inserted']/div[@class='al-main']/div[@class='al-content padding']/survey-editor[@class='ng-star-inserted']/p-dialog[@class='ng-tns-c72-8 ng-star-inserted']/div[@class='ng-tns-c72-8 p-dialog-mask p-component-overlay p-dialog-mask-scrollblocker ng-star-inserted']/div[@role='dialog']/div[@class='ng-tns-c72-8 p-dialog-content']/ap-list[@class='ng-tns-c72-8 ng-star-inserted']/p-tabview/div[@class='p-tabview p-component']/div[@class='p-tabview-panels']/p-tabpanel[@header='Wifi']/div[@id='p-tabpanel-0']/div[@class='wifi-list-container']/three-pick-list/div[@class='list-container']/div[1]"
        # _new = "(//p-tabpanel[@header='Wifi']//div[@role='tabpanel']//div[@class='wifi-list-container']//three-pick-list//div)[1]"
    _source_list_xpath = "(//three-pick-list//div[@class='pick-list-wrapper'])[2]//ul//li"
    def get_source_list_mac_addresses(self):
        time.sleep(1)
        source_list_mac_addresses_elements = self.getElements(self._source_list_xpath, locatorType="xpath")
        for mac_address in source_list_mac_addresses_elements:
            mac_address_text = mac_address.text
            print(mac_address_text)

    _source_list_delete_btn = "(//three-pick-list//div[@class='pick-list-wrapper'])[2]//ul//button"

    def delete_source_mac_addresses(self):
        # get_all_delete_btns = self.getElements(self._source_list_delete_btn, locatorType="xpath")
        # count_ele = len(get_all_delete_btns)
        # print(count_ele)
        # while count_ele >= 0:
        #     self.elementClick(self._source_list_delete_btn, locatorType="xpath")


        list_clicks = self.getElements(self._source_list_xpath, locatorType="xpath")
        # if not list_clicks:
        #     print(f"-x-x-x-x-x-x-x-x--x-:{list_clicks}")
        #     self.cancel_btn()
        # else:
        #     print(f"-x-x-x-x-x-x-x-x--x-:{list_clicks}")
        for click in list_clicks:
            time.sleep(0.5)
        # while len(list_clicks) >= 0:
            self.elementClick(self._source_list_xpath, locatorType="xpath")
            self.elementClick(self._source_list_delete_btn, locatorType="xpath")
                # self.click_save_btn()

            # source_list_mac_addresses_elements = self.getElements(self._source_list_xpath, locatorType="xpath")
            # for mac_address in source_list_mac_addresses_elements:
            #     mac_address_text = mac_address.text
            #     print(f"mac address deleted: {mac_address_text}")

    def verify_source_macs_deleted(self):
        source_mac_delete = self.isElementPresent(self._source_list_xpath, locatorType="xpath")
        return source_mac_delete

    _save_btn = "//button[normalize-space()='Save']"
    def click_save_btn(self):
        self.elementClick(self._save_btn, locatorType="xpath")

    _white_list_xpath = "(//three-pick-list//div[@class='pick-list-wrapper'])[1]//ul//li"
    _white_list_delete_btn = "(//three-pick-list//div[@class='pick-list-wrapper'])[1]//ul//button"

    _click_cancel_button = "//span[contains(@class, 'p-dialog-header-close-icon')]"
    def cancel_btn(self):
        self.elementClick(self._click_cancel_button, locatorType="xpath")


    def delete_white_mac_addresses(self):
        list_clicks = self.getElements(self._white_list_xpath, locatorType="xpath")
        for click in list_clicks:
            self.elementClick(self._white_list_xpath, locatorType="xpath")
            time.sleep(1)
            self.elementClick(self._white_list_delete_btn, locatorType="xpath")

        if list_clicks is None:
            return None


    _ignore_list_xpath = "(//three-pick-list//div[@class='pick-list-wrapper'])[3]//ul//li"
    _ignore_list_delete_btn = "(//three-pick-list//div[@class='pick-list-wrapper'])[3]//ul//button"
    def delete_ignore_mac_addresses(self):
        list_clicks = self.getElements(self._ignore_list_xpath, locatorType="xpath")
        # if list_clicks is None:
        #     return None
        # else:
        for click in list_clicks:
            self.elementClick(self._ignore_list_xpath, locatorType="xpath")
            time.sleep(1)
            self.elementClick(self._ignore_list_delete_btn, locatorType="xpath")

        if list_clicks is None:
            return None



    _white_list_mac_address_textbox_xpath = "(//three-pick-list//div[@class='pick-list-wrapper'])[1]//input[@placeholder='Enter ID']"
    _click_plus_btn = "(//three-pick-list//div[@class='pick-list-wrapper'])[1]//button[@type='submit']"
    def enter_whitelist_mac(self, white_list):
        # white_list = ["A1:B2:C3:D4:E5:F6", "A1:B2:C3:D4:E5:XX", "a1:b2:c3:d4:xx:xx", "A1:B2:C3:XX:xx:1E", "A1:B2:C3:XX:E5:XX", "C3:D4:E5:F6:A7:B8"]
        for i in white_list:
            print(i)
            self.backspace_clear(self._white_list_mac_address_textbox_xpath, locatorType="xpath")
            self.sendKeys(i, self._white_list_mac_address_textbox_xpath, locatorType="xpath")
            time.sleep(2)
            self.elementClick(self._click_plus_btn, locatorType="xpath")
            time.sleep(2)



    _verify_fingerprint_message = "//span[contains(text(),'Fingerprint generated on:')]"
    def verify_fingerprint_timestamp(self):
        "before refresh page, get the fingerprint timestamp"
        before_stamp_element = self.getElement(self._verify_fingerprint_message, locatorType="xpath")
        before_stamp_text = before_stamp_element.text
        print(before_stamp_text)

        "refresh page to get new time stamp"
        self.refresh_page()

        "all values will be gone due to refresh, search for values again"
        self.enter_venue()
        self.select_floor()
        time.sleep(5)

        "after refresh page, get the fingerprint timestamp"
        after_stamp_element = self.getElement(self._verify_fingerprint_message, locatorType="xpath")
        after_stamp_text = after_stamp_element.text
        print(after_stamp_text)
        time.sleep(10)

        "compare both stamps"
        if before_stamp_text != after_stamp_text:
            print(f"Finger Print Verified by Generated Time Stamp: before_reprocess:-{before_stamp_text}, after_reprocess:-{after_stamp_text} ")
            return True
        else:
            return False


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


    _ignore_list_mac_address_textbox_xpath = "(//three-pick-list//div[@class='pick-list-wrapper'])[3]//input[@placeholder='Enter ID']"
    _click_plus_btn_ignore_list = "(//three-pick-list//div[@class='pick-list-wrapper'])[3]//button[@type='submit']"
    def enter_ignorelist_mac(self, ignore_list):
        for i in ignore_list:
            print(i)
            self.backspace_clear(self._ignore_list_mac_address_textbox_xpath, locatorType="xpath")
            self.sendKeys(i, self._ignore_list_mac_address_textbox_xpath, locatorType="xpath")
            time.sleep(2)
            self.elementClick(self._click_plus_btn_ignore_list, locatorType="xpath")
            time.sleep(2)


    _ignore_list_upload_btn = "(//three-pick-list//div[@class='pick-list-wrapper'])[3]//div/button[contains(text(),' Upload ')]"
    def upload_ignore_list_csv(self):
        time.sleep(2)
        self.elementClick(self._ignore_list_upload_btn, locatorType="xpath")
        time.sleep(1)

        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
        print(ROOT_DIR)
        time.sleep(1)
        CONFIG_PATH = os.path.join(ROOT_DIR, 'ICA_MultiFloor_IL_2023-02-22T19_46_15.475Z.csv')
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
