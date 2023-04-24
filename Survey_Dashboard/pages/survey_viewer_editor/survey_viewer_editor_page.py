import time

from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from screeninfo import get_monitors

class DisplayVenuePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        log = cl.customLogger(logging.DEBUG)
        # locators
        self._venue_search_field = "//input[@class='p-dropdown-filter p-inputtext p-component ng-tns-c43-2']"
        self._venue_select_button = "//div[@class='venue-select-wrapper']"
        self._dashboard_button = "//a[@class='al-sidebar-list-link group-title ng-star-inserted']"
        self._admin_button = "//span[@class='ion-gear-a menu-icon ng-star-inserted']"
        self._survey_viewer_button = "//a[@class='al-sidebar-list-link ng-star-inserted']"
        self._survey_editor_button = "//a[@href='#/pages/admin/surveymapauthoringtool']"
        self._venue_item = "//li[@aria-label='PLACEHOLDER']"
        self._zoom_in_btn = "//a[@class='leaflet-control-zoom-in']"
        self._zoom_out_btn = "//a[@class='leaflet-control-zoom-out']"

        # maps
        self._map_select = "//div[@class='leaflet-control-layers leaflet-control']"
        self._google_maps = "//span[contains(text(),'Google Maps')]"
        self._satellite_maps = "//span[contains(text(),'Google Satellite Maps')]"
        self._street_maps = "//span[contains(text(),'Open Street Maps')]"
        self._none_maps = "//span[contains(text(),'None')]"

        # Options
        self._options_cog = "//div[@class='leaflet-control-layers leaflet-control map-options-control']"
        self._mag_wifi = "//span[contains(text(),'Estimated Mag+Wi-Fi Position Accuracy')]"
        self._mag_pos = "//span[contains(text(),'Estimated Magnetic Position Accuracy')]"
        self._coverage = "//span[contains(text(),'Coverage')]"
        self._saved_routes = "//span[contains(text(),'Saved Routes')]"


        #Route
        self._create_route = "//a[@class='leaflet-draw-draw-polyline']"
        self._normal_route = "//li[@aria-label='Normal']"
        
        # Access
        self._access_point_list = "//button[contains(text(),'Access points lists')]"
        # self._source_list = "//ul[@class='pick-list']"
        self._source_list_xpath = "(//three-pick-list//div[@class='pick-list-wrapper'])[2]//ul//li"
        self._source_list_delete_btn = "(//three-pick-list//div[@class='pick-list-wrapper'])[2]//ul//button"

    def enter_venue_search(self, search_term):
        self.sendKeys(search_term, self._venue_search_field, locatorType="xpath")

    def delete_all_sources(self):
        # src_list = self.getElement(self._source_list, locatorType="xpath")
        # sources = src_list.find_elements_by_tag_name("li")
        # for source in sources:
        #     print(source.text)
        time.sleep(1)
        src_list_elements = self.getElements(self._source_list_xpath, locatorType="xpath")
        for click in src_list_elements:
            self.elementClick(self._source_list_xpath, locatorType="xpath")
            self.elementClick(self._source_list_delete_btn, locatorType="xpath")


    def select_access_point_list(self):
        time.sleep(1)
        self.elementClick(locator=self._access_point_list, locatorType="xpath")

    def create_route(self):
        (center_x, center_y) = self.get_screen_center()
        self.click_and_drag((center_x+200, center_y))

    def select_normal_route(self):
        self.elementClick(locator=self._normal_route, locatorType="xpath")

    def select_create_route(self):
        self.elementClick(locator=self._create_route, locatorType="xpath")

    def select_saved_routes(self):
        self.hold_wait()
        self.elementClick(locator=self._options_cog, locatorType="xpath")
        self.elementClick(locator=self._saved_routes, locatorType="xpath")

    def select_mag_wifi(self):
        self.hold_wait()
        self.elementClick(locator=self._options_cog, locatorType="xpath")
        self.elementClick(locator=self._mag_wifi, locatorType="xpath")

    def select_mag_pos(self):
        self.hold_wait()
        self.elementClick(locator=self._options_cog, locatorType="xpath")
        self.elementClick(locator=self._mag_pos, locatorType="xpath")

    def select_coverage(self):
        self.hold_wait()
        self.elementClick(locator=self._options_cog, locatorType="xpath")
        self.elementClick(locator=self._coverage, locatorType="xpath")
        self.hold_wait()

    def select_satellite_maps(self):
        self.hold_wait()
        self.hold_wait()
        self.elementClick(locator=self._map_select, locatorType="xpath")
        self.elementClick(locator=self._satellite_maps, locatorType="xpath")

    def select_street_maps(self):
        self.hold_wait()
        self.hold_wait()
        self.elementClick(locator=self._map_select, locatorType="xpath")
        self.elementClick(locator=self._street_maps, locatorType="xpath")

    def select_none(self):
        self.hold_wait()
        self.hold_wait()
        self.elementClick(locator=self._map_select, locatorType="xpath")
        self.elementClick(locator=self._none_maps, locatorType="xpath")

    def select_settings_none(self):
        self.hold_wait()
        self.hold_wait()
        self.elementClick(locator=self._options_cog, locatorType="xpath")
        self.elementClick(locator=self._none_maps, locatorType="xpath")

    _click_survey_editor = "//div[@id='surveyEditorMap']"
    _dir = "//img[@id='northArrow']"
    def pan_up(self):
        (x_center, y_center) = self.get_screen_center()
        to_pos = (x_center+100, y_center)
        self.click_and_drag(to_pos)

    # def pan_up(self):
    #     time.sleep(1)
    #     # middle_of_screen = self.driver.execute_script("return window.innerHeight/2")
    #     # time.sleep(5)
    #     # print(f"-----middle of the screen: ---- {middle_of_screen}")
    #     # self.driver.execute_script("window.scrollBy(0, {});".format(middle_of_screen + 80))
    #     # time.sleep(5)
    #     window_width = self.driver.execute_script('return window.innerWidth')
    #     scroll_x = window_width / 2 - 80
    #     print(scroll_x)
    #     self.driver.execute_script('window.scrollTo(arguments[0], 0);', scroll_x)
    #     time.sleep(5)

    def pan_down(self):
        (x_center, y_center) = self.get_screen_center()
        to_pos = (x_center, y_center-100)
        self.click_and_drag(to_pos)

    def pan_left(self):
        (x_center, y_center) = self.get_screen_center()
        to_pos = (x_center, y_center-100)
        self.click_and_drag(to_pos)

    def pan_right(self):
        (x_center, y_center) = self.get_screen_center()
        to_pos = (x_center, y_center+100)
        self.click_and_drag(to_pos)

    def click_zoom_in(self):
        self.hold_wait()
        self.elementClick(self._zoom_in_btn, locatorType="xpath")

    def zoom_in_3x(self):
        self.click_zoom_in()
        self.click_zoom_in()
        self.click_zoom_in()

    def click_zoom_out(self):
        self.hold_wait()
        self.elementClick(self._zoom_out_btn, locatorType="xpath")
    
    def zoom_out_3x(self):
        self.click_zoom_out()
        self.click_zoom_out()
        self.click_zoom_out()

    def click_search_result(self, search_term):
        element = self._venue_item.replace("PLACEHOLDER", search_term)
        self.elementClick(element, locatorType="xpath")

    def click_dashboard(self):
        self.elementClick(self._dashboard_button, locatorType="xpath")

    def click_admin(self):
        self.elementClick(self._admin_button, locatorType="xpath")

    def click_survey_viewer(self):
        self.elementClick(self._survey_viewer_button, locatorType="xpath")

    def click_survey_editor(self):
        self.elementClick(self._survey_editor_button, locatorType="xpath")

    def click_select_venue(self):
        self.elementClick(self._venue_select_button, locatorType="xpath")

    def clear_search_box(self):
        self.backspace_clear(locator=self._venue_search_field, locatorType="xpath")
        # self.getElement(locator=self._venue_search_field, locatorType="xpath").clear()

    _email_field = "//input[@type='email']"
    _password_field = "//input[@id='inputPassword3']"
    def clear_fields(self):
        # self.getElement(locator=self._email_field).clear()
        # self.getElement(locator=self._password_field).clear()
        self.backspace_clear(self._email_field, locatorType="xpath")
        self.backspace_clear(self._password_field, locatorType="xpath")


    _click_cancel_button = "//span[contains(@class, 'p-dialog-header-close-icon')]"
    def cancel_btn(self):
        self.elementClick(self._click_cancel_button, locatorType="xpath")
 
    def get_screen_center(self):
        x_offset = None
        y_offset = None
        for m in get_monitors():
            if m.is_primary:
                x_offset = m.width/2
                y_offset = m.height/2
        return (x_offset, y_offset)