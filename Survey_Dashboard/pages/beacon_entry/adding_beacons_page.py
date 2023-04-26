import time

from screeninfo import get_monitors
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class AddBeaconPage(SeleniumDriver):

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

    _zoom_in_btn = "//a[@class='leaflet-control-zoom-in']"

    def click_zoom_in(self):
        self.hold_wait()
        self.elementClick(self._zoom_in_btn, locatorType="xpath")

    _options_cog = "//div[@class='leaflet-control-layers leaflet-control map-options-control']"
    _beacons = "//span[contains(text(),'Beacons')]"

    def select_beacons_box(self):
        self.hold_wait()
        self.elementClick(locator=self._options_cog, locatorType="xpath")
        self.elementClick(locator=self._beacons, locatorType="xpath")

    _map_select = "//div[@class='leaflet-control-layers leaflet-control']"
    _none_maps = "//span[contains(text(),'None')]"

    def select_none(self):
        self.hold_wait()
        self.hold_wait()
        self.elementClick(locator=self._map_select, locatorType="xpath")
        self.elementClick(locator=self._none_maps, locatorType="xpath")

    _beacon_control_status = "//a[@title='Setup beacon']"

    def beacon_status(self):
        beacon_status_true = self.isElementPresent(self._beacon_control_status, locatorType="xpath")
        return beacon_status_true

    def click_beacon_controller(self):
        self.elementClick(self._beacon_control_status, locatorType="xpath")

    _beacon_UUID = "//input[@id='beaconUuid']"

    def add_beacon_uuid(self, beacon_uuid):
        self.backspace_clear(self._beacon_UUID, locatorType="xpath")
        self.sendKeys(beacon_uuid, self._beacon_UUID, locatorType="xpath")

    _beacon_minor = "//input[@id='beaconMinor']"

    def add_beacon_minor(self, beacon_minor):
        self.backspace_clear(self._beacon_minor, locatorType="xpath")
        self.sendKeys(beacon_minor, self._beacon_minor, locatorType="xpath")

    _beacon_major = "//input[@id='beaconMajor']"

    def add_beacon_major(self, beacon_major):
        self.backspace_clear(self._beacon_major, locatorType="xpath")
        self.sendKeys(beacon_major, self._beacon_major, locatorType="xpath")

    _beacon_power = "//input[@id='beaconPower']"

    def add_beacon_power(self, beacon_power):
        self.backspace_clear(self._beacon_power, locatorType="xpath")
        self.sendKeys(beacon_power, self._beacon_power, locatorType="xpath")

    _beacon_altitude = "//input[@id='beaconAltitude']"

    def add_beacon_altitude(self, beacon_altitude):
        self.sendKeys(beacon_altitude, self._beacon_altitude, locatorType="xpath")

    _beacon_type_dropdown = "//span[@id='pr_id_5_label']"
    _beacon_type_value_7 = "//span[normalize-space()='Restricted Area Assistance (7)']"

    def add_beacon_type_7(self):
        self.elementClick(self._beacon_type_dropdown, locatorType="xpath")
        time.sleep(1)
        self.elementClick(self._beacon_type_value_7, locatorType="xpath")

    _beacon_type_value_1 = "//span[contains(text(),'General Proximity (1)')]"

    def add_beacon_type_1(self):
        self.elementClick(self._beacon_type_dropdown, locatorType="xpath")
        time.sleep(1)
        self.elementClick(self._beacon_type_value_1, locatorType="xpath")

    _beacon_brand_dropdown = "//span[@id='pr_id_6_label']"
    _beacon_brand_value = "//span[@class='ng-star-inserted'][normalize-space()='Aplix']"

    def add_beacon_brand(self):
        self.elementClick(self._beacon_brand_dropdown, locatorType="xpath")
        time.sleep(1)
        self.elementClick(self._beacon_brand_value, locatorType="xpath")

    _save_btn = "//button[normalize-space()='Save']"

    def click_save_button(self):
        self.elementClick(self._save_btn, locatorType="xpath")
        time.sleep(2)

    _survey_editor_space = "//div[@id='surveyEditorMap']"

    def place_beacon(self, xoffset, yoffset):
        get_ele = self.getElement(self._survey_editor_space, locatorType="xpath")
        print(f"get_ele: {get_ele}")

        # self.offset_click(self._survey_editor_space, locatorType="xpath", xoffset=50, yoffset=100)
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(get_ele, xoffset, yoffset).click().perform()

    _save_all_beacons = "//button[@ptooltip='Save beacons csv to cloud']"

    def save_all(self):
        self.elementClick(self._save_all_beacons, locatorType="xpath")
