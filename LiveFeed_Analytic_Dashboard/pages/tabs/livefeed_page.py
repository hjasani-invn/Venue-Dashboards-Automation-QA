from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging


class LiveFeedTabPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    _venue_drop_down = "//mat-select[@placeholder='Venue']"

    # _expand_list = "//div[@role='listbox']"
    _select_venue_ica_2021 = "//span[@class='mat-option-text'][normalize-space()='ICA_2021']"
    _select_venue_Cambrian_P2_1x1 = "//span[@class='mat-option-text'][normalize-space()='Cambrian_P2-1x1']"

    _show_online_users = "//span[contains(text(),'Show only online')]"

    _group_sort = "//mat-icon[contains(text(),'expand_more')]"
    _collapse_grp = "//mat-icon[contains(text(),'expand_more')]"

    _change_floor = "//label[@class='map-selected-floor']" #xpath
    _c_path = ".." #xpath
    _d_path = "label" #css

    _click_out = "//body"


    def click_drop_down(self):
        self.hold_wait()
        self.elementClick(self._venue_drop_down, locatorType="xpath")
        self.hold_wait()

    # def expand_list(self, select_venue):
    #     self.hold_wait()
    #     self.sendKeys(self._expand_list, locatorType="xpath")

    def click_out(self):
        self.elementClick(self._click_out, locatorType="xpath")


    def select_venue(self):
        self.click_drop_down()
        self.elementClick(self._select_venue_ica_2021, locatorType="xpath")
        self.hold_wait()
        self.click_out()
        self.hold_wait()

    def toggle_online_user_btn(self):
        self.hold_wait()
        self.elementClick(self._show_online_users, locatorType="xpath")
        self.hold_wait()

    def grp_srt(self):
        self.elementClick(self._group_sort, locatorType="xpath")
        self.hold_wait()

    def collapse_grp(self):
        self.elementClick(self._collapse_grp, locatorType="xpath")
        self.hold_wait()


    _select_floor = "//div[@class='leaflet-control-layers-base']/label//div//span[contains(text(), ' 4')]"

    def change_venue_floor(self, floor_to_select=None):
        # # Find the floor currently selected to overlay.
        # selected_floor_element = self.getElement(self._change_floor, locatorType="xpath")
        # selected_floor = selected_floor_element.text
        #
        # # Find all floors with maps.
        # floors_parent = selected_floor_element.getElement.self._c_path, locatorType="xpath"
        # all_floors = floors_parent.getElements.self._d_path, locatorType="xpath"
        self.elementClick(self._select_floor, locatorType="xpath")
        self.hold_wait()





