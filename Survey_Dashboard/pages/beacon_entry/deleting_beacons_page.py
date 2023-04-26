import time

from selenium.webdriver import ActionChains

from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class DeleteBeaconPage(SeleniumDriver):

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

    _survey_editor_space = "//div[@id='surveyEditorMap']"
    _delete_beacon = "//button[normalize-space()='Delete']"
    _beacon_leaflet_popup = "//div[@class='leaflet-popup-content']"
    _uuid_1_not_null = "//div[contains(text(),'Proximity UUID: f7826da6-4fa2-4e98-8024-bc5b71e089')]"
    "if UUID changed in future, introduced separate variables like below"

    # _uuid_2_not_null = "//div[contains(text(),'Proximity UUID: f7826da6-4fa2-4e98-8024-bc5b71e089')]"
    # _uuid_3_not_null = "//div[contains(text(),'Proximity UUID: f7826da6-4fa2-4e98-8024-bc5b71e089')]"

    # find beacon by x,y and double click
    def delete_beacons(self):
        get_ele = self.getElement(self._survey_editor_space, locatorType="xpath")

        # delete beacon_1
        xoffset_1 = 120
        yoffset_1 = 120
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(get_ele, xoffset_1, yoffset_1).double_click().perform()
        get_element = self.getElement(self._uuid_1_not_null, locatorType="xpath")
        get_element_txt = get_element.text
        print(get_element_txt)
        if "Proximity UUID: f7826da6-4fa2-4e98-8024-bc5b71e0893e" in get_element_txt:
            self.elementClick(self._delete_beacon, locatorType="xpath")
            print("beacon_1 deleted")
        else:
            print("Wrong Beacon Selected")

        # delete beacon_2
        xoffset_1 = 150
        yoffset_1 = 150
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(get_ele, xoffset_1, yoffset_1).double_click().perform()
        get_element = self.getElement(self._uuid_1_not_null, locatorType="xpath")
        get_element_txt = get_element.text
        print(get_element_txt)
        if "Proximity UUID: f7826da6-4fa2-4e98-8024-bc5b71e0893e" in get_element_txt:
            self.elementClick(self._delete_beacon, locatorType="xpath")
            print("beacon_2 deleted")
        else:
            print("Wrong Beacon Selected")

        # delete beacon_3
        xoffset_1 = 190
        yoffset_1 = 190
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(get_ele, xoffset_1, yoffset_1).double_click().perform()
        get_element = self.getElement(self._uuid_1_not_null, locatorType="xpath")
        get_element_txt = get_element.text
        print(get_element_txt)
        if "Proximity UUID: f7826da6-4fa2-4e98-8024-bc5b71e0893e" in get_element_txt:
            self.elementClick(self._delete_beacon, locatorType="xpath")
            print("beacon_3 deleted")
        else:
            print("Wrong Beacon Selected")

    _save_all_beacons = "//button[@ptooltip='Save beacons csv to cloud']"

    def save_all(self):
        self.elementClick(self._save_all_beacons, locatorType="xpath")
