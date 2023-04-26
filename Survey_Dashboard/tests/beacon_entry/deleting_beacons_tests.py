import time

import pytest

from base.selenium_driver import SeleniumDriver
from pages.beacon_entry.deleting_beacons_page import DeleteBeaconPage
from pages.home.login_page import LoginPage
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DeleteBeaconTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.deletebeaconpage = DeleteBeaconPage(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)

        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

        self.deletebeaconpage.click_admin()
        self.deletebeaconpage.click_survey_editor()
        self.deletebeaconpage.enter_venue()
        self.deletebeaconpage.select_floor()
        self.deletebeaconpage.click_zoom_in()

    @pytest.mark.run(33)
    def test_3_7_3_1_delete_generated_beacons_during_test(self):
        print("I'm beacon delete test")
        self.deletebeaconpage.select_none()
        self.deletebeaconpage.select_beacons_box()
        self.deletebeaconpage.delete_beacons()
        self.seleniumdriver.screen_shot(file="test_3_7_3_1_delete_generated_beacons_during_test")
        self.deletebeaconpage.save_all()
