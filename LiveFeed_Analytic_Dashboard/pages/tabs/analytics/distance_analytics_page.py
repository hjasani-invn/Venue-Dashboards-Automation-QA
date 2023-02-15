from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging


class DistanceAnalyticsTabPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _select_analytics_tab = "//span[contains(text(),'Analytics')]"
    _select_distance_analytics_tab = "//a[contains(text(),'Distance Analytics')]"

    def select_analytic_distance_analytics_tab(self):
        self.elementClick(self._select_analytics_tab, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_distance_analytics_tab, locatorType="xpath")
        self.hold_wait()

    _select_floor = "//mat-select[@placeholder='Floor']"

    def select_floor(self, f_n):
        self.hold_wait()
        self.sendKeys(f_n, self._select_floor, locatorType="xpath")
        self.hold_wait()
        # if self.waitForElement(self._select_floor, locatorType="xpath"):
        #     self.sendKeys(f_n, self._select_floor, locatorType="xpath")
        #     self.hold_wait()
        # else:
        #     self.hold_wait()

    _select_venue = "//mat-select[@placeholder='Venue']"

    # _select_venue_it = "//span[@class='mat-option-text'][normalize-space()='ICA_2021']"

    def enter_venue_name(self, v_n):
        self.hold_wait()
        self.elementClick(self._select_venue, locatorType="xpath")
        self.hold_wait()
        self.sendKeys(v_n, self._select_venue, locatorType="xpath")
        # self.elementClick(self._select_venue_it, locatorType="xpath")
        self.click_out()
        self.hold_wait()

    _click_out = "//body"

    def click_out(self):
        self.elementClick(self._click_out, locatorType="xpath")

    _start_date = "//input[@data-placeholder='Start Date']"
    _start_time = "//input[@data-placeholder='Start time']"

    _end_date = "//input[@data-placeholder='End Date']"
    _end_time = "//input[@data-placeholder='End time']"

    def choose_date_and_time(self, s_date, s_time, e_date, e_time):
        self.backspace_clear(self._start_date, locatorType="xpath")
        self.sendKeys(s_date, self._start_date, locatorType="xpath")
        self.hold_wait()
        self.backspace_clear(self._start_time, locatorType="xpath")
        self.sendKeys(s_time, self._start_time, locatorType="xpath")

        self.backspace_clear(self._end_date, locatorType="xpath")
        self.sendKeys(e_date, self._end_date, locatorType="xpath")
        self.hold_wait()
        self.backspace_clear(self._end_time, locatorType="xpath")
        self.sendKeys(e_time, self._end_time, locatorType="xpath")


    _time_zone = "//input[@data-placeholder='Timezone']"

    def select_timezone(self, country_name):
        self.hold_wait()
        self.backspace_clear(self._time_zone, locatorType="xpath")
        self.hold_wait()
        self.sendKeys(country_name, self._time_zone, locatorType="xpath")
        self.hold_wait()
        self.click_out()

    _search_ = "//span[contains(text(),'Search')]"

    def click_search(self):
        self.elementClick(self._search_, locatorType="xpath")
        self.hold_wait()
        self.hold_wait()



    _map_diagram_xpath = "//p-accordiontab[@header='Map/Diagram']//a[@role='tab']"
    _comman_xpath = "//div[starts-with(@class, 'ui-accordion-header')]//a[@role='tab']"
    _map_diagram_1 = "(//div[starts-with(@class, 'ui-accordion-header')]//a[@role='tab'])[1]"
    _graph_diagram_2 = "(//div[starts-with(@class, 'ui-accordion-header')]//a[@role='tab'])[2]"
    _table_diagram_3 = "(//div[starts-with(@class, 'ui-accordion-header')]//a[@role='tab'])[3]"

    # _graph_frame = "(//div[@class='graph-container'])[1]"
    # _graph_frame = "(//div[@class='distance-graph'])[1]"
    _map_frame = "(//div[@role='region'])[1]"
    _graph_frame = "(//div[@role='region'])[2]"
    _tables_frame = "(//div[@role='region'])[3]"

    _remove_chevron = "//button[@class='assets-tree-collapse-btn collapse-btn']"

    def take_screenshot_for_all(self):

        self.elementClick(self._remove_chevron, locatorType="xpath")
        self.hold_wait()


        map_element = self.getElement(self._map_diagram_1, locatorType="xpath")
        map_element_attribute_value = map_element.get_attribute("aria-expanded")
        print(f"Map attribute value is: {map_element_attribute_value}")
        if map_element_attribute_value == "true":
            self.move_to_element(self._map_frame, locatorType="xpath")
            self.hold_wait()
            self.screen_shot(file="map_screenshot")

        graph_element = self.getElement(self._graph_diagram_2, locatorType="xpath")
        graph_element_attribute_value = graph_element.get_attribute("aria-expanded")
        print(f"Graph attribute value is: {graph_element_attribute_value}")
        if graph_element_attribute_value == "true":
            print("if block for graph element")
            self.screen_shot(file="graph_screenshot")
        else:
            print("else block for graph element")
            self.scroll_to_element(self._graph_diagram_2, locatorType="xpath")
            self.elementClick(self._graph_diagram_2, locatorType="xpath")
            self.hold_wait()
            graph_element = self.getElement(self._graph_diagram_2, locatorType="xpath")
            graph_element_attribute_value = graph_element.get_attribute("aria-expanded")
            print(f"Graph attribute else block value is: {graph_element_attribute_value}")
            self.move_to_element(self._graph_frame, locatorType="xpath")
            self.hold_wait()
            self.screen_shot(file="graph_screenshot")

        # Table Screen shot
        self.scroll_to_element(self._table_diagram_3, locatorType="xpath")
        self.elementClick(self._table_diagram_3, locatorType="xpath")
        self.hold_wait()
        self.move_to_element(self._tables_frame, locatorType="xpath")
        self.hold_wait()
        self.screen_shot(file="table_screenshot")
