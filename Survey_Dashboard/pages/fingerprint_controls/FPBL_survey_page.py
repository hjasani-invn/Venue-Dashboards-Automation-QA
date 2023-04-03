import time

from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class FPBLSurveyPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        log = cl.customLogger(logging.DEBUG)

    # LOCATORS:
    _admin_btn = "//span[contains(text(),'Admin')]"
    def click_admin(self):
        self.elementClick(self._admin_btn, locatorType="xpath")

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
        self.sendKeys(venue_name, self._search_venue_name, locatorType="xpath")
        self.elementClick(self._select_venue, locatorType="xpath")
        self.hold_wait()

    _select_floor = "//span[contains(text(),'Fourth Floor')]"
    def select_floor(self):
        self.elementClick(self._select_floor, locatorType="xpath")
        self.hold_wait()

    _fingerprint_btn = "//button[contains(text(),'Fingerprint builder')]"
    def click_fingerprint_btn(self):
        self.elementClick(self._fingerprint_btn, locatorType="xpath")

    _fpbl_survey = "//span[contains(text(),'FPBL - Survey')]"
    _fpbl_beacon_recommendation = "//span[contains(text(),'Beacon Recommendation')]"
    _processing_mode = "//p-dropdown[@placeholder='Select processing mode']"
    def select_fpbl_survey(self, processing_mode=""):
        self.elementClick(self._processing_mode, locatorType="xpath")
        if processing_mode == "Survey":
            self.elementClick(self._fpbl_survey, locatorType="xpath")
        elif processing_mode == "Beacon Recommendation":
            self.elementClick(self._fpbl_beacon_recommendation, locatorType="xpath")

    _click_reprocess_btn = "//div//button[@class='btn btn-success']"
    def click_reprocess(self):
        self.elementClick(self._click_reprocess_btn, locatorType="xpath")
        time.sleep(900)
        # time.sleep(30)
        # self.refresh_page()
        # time.sleep(60)

    # _verify_fingerprint_message = "//span[contains(text(),'Fingerprint generated on:')]"
    # def verify_fingerprint_timestamp(self):
    #     "before refresh page, get the fingerprint timestamp"
    #     before_stamp_element = self.getElement(self._verify_fingerprint_message, locatorType="xpath")
    #     before_stamp_text = before_stamp_element.text
    #     print(before_stamp_text)
    #
    #     "refresh page to get new time stamp"
    #     self.refresh_page()
    #
    #     "all values will be gone due to refresh, search for values again"
    #     self.enter_venue()
    #     self.select_floor()
    #     time.sleep(5)
    #
    #     "after refresh page, get the fingerprint timestamp"
    #     after_stamp_element = self.getElement(self._verify_fingerprint_message, locatorType="xpath")
    #     after_stamp_text = after_stamp_element.text
    #     print(after_stamp_text)
    #     time.sleep(10)
    #
    #     "compare both stamps"
    #     if before_stamp_text != after_stamp_text:
    #         print(f"Finger Print Verified by Generated Time Stamp: before_reprocess:-{before_stamp_text}, after_reprocess:-{after_stamp_text} ")
    #     #     return True
    #     # else:
    #     #     return False


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


    def refresh(self):
        self.refresh_page()

    _checkbox = "//label[contains(text(),'Default max beacons config')]"
    # aria-checked="false"
    # element.get_attribute("attribute name")
    _fourth_floor = "(//div//input[@label='Max beacons'])[1]"
    _first_floor = "(//div//input[@label='Max beacons'])[2]"
    def checkbox(self, number_of_beacons_on_4th_floor, number_of_beacons_on_1st_floor):
        self.elementClick(self._checkbox, locatorType="xpath")

        self.backspace_clear(self._fourth_floor, locatorType="xpath")
        self.sendKeys(number_of_beacons_on_4th_floor, self._fourth_floor, locatorType="xpath")

        self.backspace_clear(self._first_floor, locatorType="xpath")
        self.sendKeys(number_of_beacons_on_1st_floor, self._first_floor, locatorType="xpath")
