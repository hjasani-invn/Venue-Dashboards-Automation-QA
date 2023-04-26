import time

from selenium.webdriver import ActionChains

from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class EditBeaconPage(SeleniumDriver):

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

    _beacon_power = "//input[@id='beaconPower']"

    def add_beacon_power(self, beacon_power):
        self.backspace_clear(self._beacon_power, locatorType="xpath")
        self.sendKeys(beacon_power, self._beacon_power, locatorType="xpath")

    _survey_editor_space = "//div[@id='surveyEditorMap']"
    _beacon_leaflet_popup = "//div[@class='leaflet-popup-content']"
    _uuid_1_not_null = "//div[contains(text(),'Proximity UUID: f7826da6-4fa2-4e98-8024-bc5b71e089')]"

    # find beacon by x,y and double click
    def beacon_1_double_click(self):
        get_ele = self.getElement(self._survey_editor_space, locatorType="xpath")
        xoffset_1 = 120
        yoffset_1 = 120
        actions = ActionChains(self.driver)
        # actions.move_to_element_with_offset(get_ele, xoffset_1, yoffset_1).double_click().perform()
        actions.move_to_element_with_offset(get_ele, xoffset_1, yoffset_1).click().perform()
        get_element = self.getElement(self._uuid_1_not_null, locatorType="xpath")
        get_element_txt = get_element.text
        print(get_element_txt)
        if "Proximity UUID: f7826da6-4fa2-4e98-8024-bc5b71e0893e" in get_element_txt:
            actions.move_to_element_with_offset(get_ele, xoffset_1, yoffset_1).double_click().perform()
        else:
            print("Wrong Beacon Selected")

    # def beacon_2_double_click(self):
    #     get_ele = self.getElement(self._survey_editor_space, locatorType="xpath")
    #     xoffset_1 = 100
    #     yoffset_1 = 70
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element_with_offset(get_ele, xoffset_1, yoffset_1).double_click().perform()
    #
    # def beacon_3_double_click(self):
    #     get_ele = self.getElement(self._survey_editor_space, locatorType="xpath")
    #     xoffset_1 = 30
    #     yoffset_1 = 80
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element_with_offset(get_ele, xoffset_1, yoffset_1).double_click().perform()

    _uuid_2_not_null = "//div[contains(text(),'Proximity UUID: f7826da6-4fa2-4e98-8024-bc5b71e0893e')]"
    def beacon_2_double_click(self):
        get_ele = self.getElement(self._survey_editor_space, locatorType="xpath")
        xoffset_2 = 150
        yoffset_2 = 150
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(get_ele, xoffset_2, yoffset_2).click().perform()
        time.sleep(10)
        # actions.move_to_element_with_offset(get_ele, xoffset_2, yoffset_2).click().perform()
        time.sleep(10)
        get_element = self.getElement(self._uuid_2_not_null, locatorType="xpath")
        get_element_txt = get_element.text
        print(get_element_txt)
        if "Proximity UUID: f7826da6-4fa2-4e98-8024-bc5b71e0893e" in get_element_txt:
            print("matched")
            # actions.move_to_element_with_offset(get_ele, xoffset_2, yoffset_2).double_click().perform()
            # actions.move_to_element_with_offset(get_ele, xoffset_2, yoffset_2).click().perform()
            # actions.move_by_offset(200, 200).click().perform()
            # b_2 = actions.move_to_element_with_offset(get_ele, xoffset_2, yoffset_2)
            # actions.drag_and_drop_by_offset(b_2, 210, 210)
            time.sleep(5)
        else:
            print("Wrong Beacon Selected")





    _save_btn = "//button[normalize-space()='Save']"
    # _save_btn = "//button[@ptooltip='Save beacons csv to cloud']"

    def click_save_button(self):
        self.elementClick(self._save_btn, locatorType="xpath")
        time.sleep(2)
