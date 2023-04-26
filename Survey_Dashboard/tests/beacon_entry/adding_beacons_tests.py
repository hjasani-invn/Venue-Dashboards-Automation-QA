import time

import pytest

from base.selenium_driver import SeleniumDriver
from pages.beacon_entry.adding_beacons_page import AddBeaconPage
from pages.home.login_page import LoginPage
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AddBeaconTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.addbeaconpage = AddBeaconPage(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)

        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

        self.addbeaconpage.click_admin()
        self.addbeaconpage.click_survey_editor()
        self.addbeaconpage.enter_venue()
        self.addbeaconpage.select_floor()
        self.addbeaconpage.click_zoom_in()

    @pytest.mark.run(1)
    def test_3_7_1_beacon_control_status_check(self):
        print("I'm beacon Adding test")
        self.addbeaconpage.select_none()
        self.addbeaconpage.select_beacons_box()
        beacon_status = self.addbeaconpage.beacon_status()
        assert beacon_status == True
        time.sleep(1)
        self.loginpage.sign_out()
        time.sleep(1)

    @pytest.mark.run(2)
    def test_3_7_2_click_beacon_icon(self):
        print("I'm beacon Adding test")
        self.addbeaconpage.select_none()
        self.addbeaconpage.select_beacons_box()
        beacon_status = self.addbeaconpage.beacon_status()
        assert beacon_status == True
        self.addbeaconpage.click_beacon_controller()
        time.sleep(1)
        self.loginpage.sign_out()
        time.sleep(1)

    @pytest.mark.run(2)
    def test_3_7_3_add_beacon_data(self):
        print("I'm beacon Adding test")
        self.addbeaconpage.select_none()
        self.addbeaconpage.select_beacons_box()
        beacon_status = self.addbeaconpage.beacon_status()
        assert beacon_status == True
        self.addbeaconpage.click_beacon_controller()
        self.addbeaconpage.add_beacon_uuid(beacon_uuid="f7826da6-4fa2-4e98-8024-bc5b71e0893e")
        self.addbeaconpage.add_beacon_minor(beacon_minor=21)
        self.addbeaconpage.add_beacon_major(beacon_major=4)
        self.addbeaconpage.add_beacon_power(beacon_power=-77)
        self.addbeaconpage.add_beacon_altitude(beacon_altitude=4)
        self.addbeaconpage.add_beacon_type_7()  # value provides in page method
        self.addbeaconpage.add_beacon_brand()  # value provides in page method
        self.addbeaconpage.click_save_button()
        self.addbeaconpage.place_beacon(xoffset=120, yoffset=120)
        time.sleep(10)

        # second data set
        self.addbeaconpage.click_beacon_controller()
        self.addbeaconpage.add_beacon_uuid(beacon_uuid="f7826da6-4fa2-4e98-8024-bc5b71e0893e")
        self.addbeaconpage.add_beacon_minor(beacon_minor=22)
        self.addbeaconpage.add_beacon_major(beacon_major=4)
        self.addbeaconpage.add_beacon_power(beacon_power=-77)
        self.addbeaconpage.add_beacon_altitude(beacon_altitude=4)
        self.addbeaconpage.add_beacon_type_1()  # value provides in page method
        self.addbeaconpage.add_beacon_brand()  # value provides in page method
        self.addbeaconpage.click_save_button()
        self.addbeaconpage.place_beacon(xoffset=150, yoffset=150)
        time.sleep(5)


        # third data set
        self.addbeaconpage.click_beacon_controller()
        self.addbeaconpage.add_beacon_uuid(beacon_uuid="f7826da6-4fa2-4e98-8024-bc5b71e0893e")
        self.addbeaconpage.add_beacon_minor(beacon_minor=21)
        self.addbeaconpage.add_beacon_major(beacon_major=4)
        self.addbeaconpage.add_beacon_power(beacon_power=-77)
        self.addbeaconpage.add_beacon_altitude(beacon_altitude=4)
        self.addbeaconpage.add_beacon_type_1()  # value provides in page method
        self.addbeaconpage.add_beacon_brand()  # value provides in page method
        self.addbeaconpage.click_save_button()
        self.addbeaconpage.place_beacon(xoffset=190, yoffset=190)

        self.addbeaconpage.save_all()

        time.sleep(5)

        time.sleep(1)
        self.loginpage.sign_out()
        time.sleep(1)
