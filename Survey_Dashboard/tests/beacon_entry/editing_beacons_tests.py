import time

import pytest

from base.selenium_driver import SeleniumDriver
from pages.beacon_entry.editing_beacons_page import EditBeaconPage
from pages.home.login_page import LoginPage
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class EditBeaconTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.editbeaconpage = EditBeaconPage(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)

        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

        self.editbeaconpage.click_admin()
        self.editbeaconpage.click_survey_editor()
        self.editbeaconpage.enter_venue()
        self.editbeaconpage.select_floor()
        self.editbeaconpage.click_zoom_in()
        # self.editbeaconpage.click_zoom_in()

    # @pytest.mark.run(32)
    @pytest.mark.skip()
    def test_3_7_2_1_change_beacon_power_from_previous_test_and_move(self):
        print("I'm beacon edit test")
        self.editbeaconpage.select_none()
        self.editbeaconpage.select_beacons_box()
        self.editbeaconpage.beacon_1_double_click()
        time.sleep(1)
        self.editbeaconpage.add_beacon_power(beacon_power=-69)
        time.sleep(1)
        self.editbeaconpage.click_save_button()
        time.sleep(1)

        # move beacon
        self.editbeaconpage.beacon_2_double_click()
        time.sleep(2)
