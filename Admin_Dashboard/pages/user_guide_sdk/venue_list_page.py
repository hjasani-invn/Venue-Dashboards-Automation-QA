import time

import selenium.common.exceptions

from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging
import os.path


class VenueListPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _click_venue_list = "//span[normalize-space()='Venue List']"

    _table_rows_xpath = "//table[@aria-describedby='venueListTable']//tr"

    _table_td_xpath = "//table[@aria-describedby='venueListTable']//tr//td"

    def open_venue_list(self):
        global table_td
        self.elementClick(self._click_venue_list, locatorType="xpath")
        self.hold_wait()
        self.hold_wait()

    _find_venues_name = "//h3[contains(text(),'Venues')]"
    def verify_list_opens(self):
        get_venues_name = self.getElement(self._find_venues_name, locatorType="xpath")
        return get_venues_name.text



"""
        # get the table rows elements
        table_rows = self.getElements(self._table_rows_xpath, locatorType="xpath")
        # print(table_rows)


        # get the table rows elements
        table_tds = self.getElements(self._table_td_xpath, locatorType="xpath")

        # iterate over the rows and get the data from each cell
        # for row in table_rows:
        #     # cells = row.table_tds
        #     # for cell in cells:
        #     #     data = cell.text
        #     #     # perform your verification logic on the data here
        #     #     print(data)
        #     print(row.text)
        for row in table_rows:
            cells = self.getElements(self._table_td_xpath, locatorType="xpath")
            # text = table_tds.txt
            # print(text)
            # print("\n")
            for cell in cells:
                print(cell.text, end="\t")
            break

            #
            # for table_td in cells:
            #     print(table_td.text)
            # print()
            # print(table_td.text)
"""

