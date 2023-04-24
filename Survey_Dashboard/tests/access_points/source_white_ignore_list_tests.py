import time

import pytest

from base.selenium_driver import SeleniumDriver
from pages.access_points.source_white_ignore_list_page import SourceWhiteIgnoreListPage
from pages.home.login_page import LoginPage
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SourceWhiteIgnoreListTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.source_white_ignore_list_page = SourceWhiteIgnoreListPage(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)

        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

        self.source_white_ignore_list_page.click_admin()
        self.source_white_ignore_list_page.click_survey_editor()
        self.source_white_ignore_list_page.enter_venue()
        self.source_white_ignore_list_page.select_floor()

    @pytest.mark.run(13)
    def test_3_6_1_source_list_delete_macs(self):
        self.source_white_ignore_list_page.click_access_point_btn()
        self.source_white_ignore_list_page.click_wifi_btn()
        self.source_white_ignore_list_page.get_source_list_mac_addresses()
        self.seleniumdriver.screen_shot(file="test_3_6_1_source_list_delete_macs_shows_all_source_list_entries")
        self.source_white_ignore_list_page.delete_source_mac_addresses()
        self.seleniumdriver.screen_shot(file="test_3_6_1_source_list_delete_macs_delete_source_mac_addresses")
        r_1 = self.source_white_ignore_list_page.verify_source_macs_deleted()
        assert r_1 == False
        self.source_white_ignore_list_page.click_save_btn()
        # self.source_white_ignore_list_page.cancel_btn()
        time.sleep(1)
        self.loginpage.sign_out()
        time.sleep(1)

    # @pytest.mark.skip
    # def test_3_6_2_source_delete_entry_2(self):
    #     "This test need to regenerate fingerprint, need to discuss for flow, either upload deleted mac add or rebuild"
    #     # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
    #     self.source_white_ignore_list_page.click_admin()
    #     self.source_white_ignore_list_page.click_survey_editor()
    #     self.source_white_ignore_list_page.enter_venue()
    #     self.source_white_ignore_list_page.select_floor()
    #     self.source_white_ignore_list_page.click_access_point_btn()
    #     self.source_white_ignore_list_page.click_wifi_btn()

    @pytest.mark.run(14)
    def test_3_6_3_white_ignore_list_delete_macs(self):
        self.source_white_ignore_list_page.click_access_point_btn()
        self.source_white_ignore_list_page.click_wifi_btn()
        self.seleniumdriver.screen_shot(file="test_3_6_3_white_ignore_list_delete_macs_get_all_white_ignore_macs")
        r_1 = self.source_white_ignore_list_page.delete_white_mac_addresses()
        assert r_1 is None
        r_2 = self.source_white_ignore_list_page.delete_ignore_mac_addresses()
        assert r_2 is None
        self.seleniumdriver.screen_shot(file="test_3_6_3_white_ignore_list_delete_macs")
        self.source_white_ignore_list_page.click_save_btn()
        time.sleep(1)
        self.loginpage.sign_out()
        time.sleep(1)

    @pytest.mark.run(15)
    def test_3_6_4_manually_add_white_list_macs(self):
        self.source_white_ignore_list_page.click_access_point_btn()
        self.source_white_ignore_list_page.click_wifi_btn()
        self.source_white_ignore_list_page.enter_whitelist_mac(
            white_list=["A1:B2:C3:D4:E5:F6", "A1:B2:C3:D4:E5:XX", "a1:b2:c3:d4:xx:xx", "A1:B2:C3:XX:xx:1E",
                        "A1:B2:C3:XX:E5:XX", "C3:D4:E5:F6:A7:B8"])
        self.seleniumdriver.screen_shot(file="test_3_6_4_manually_add_white_list_macs")
        self.source_white_ignore_list_page.click_save_btn()
        time.sleep(900)  # wait 15 mins to build fingerprint
        r_1 = self.source_white_ignore_list_page.verify_fingerprint_timestamp()
        assert r_1 == True
        time.sleep(1)
        self.loginpage.sign_out()
        time.sleep(1)

    @pytest.mark.run(16)
    def test_3_6_5_upload_white_list_csv(self):
        self.source_white_ignore_list_page.click_access_point_btn()
        self.source_white_ignore_list_page.click_wifi_btn()
        self.source_white_ignore_list_page.delete_white_mac_addresses()
        self.source_white_ignore_list_page.upload_white_list_csv()
        self.seleniumdriver.screen_shot(file="test_3_6_5_upload_white_list_csv")
        self.source_white_ignore_list_page.click_save_btn()
        time.sleep(900)  # wait 15 mins to build fingerprint
        r_1 = self.source_white_ignore_list_page.verify_fingerprint_timestamp()
        assert r_1 == True
        time.sleep(1)
        self.loginpage.sign_out()
        time.sleep(1)

    @pytest.mark.run(17)
    def test_3_6_6_clear_ignore_list_manually_add_mac_ignore_list(self):
        self.source_white_ignore_list_page.click_access_point_btn()
        self.source_white_ignore_list_page.click_wifi_btn()
        self.source_white_ignore_list_page.delete_ignore_mac_addresses()
        self.source_white_ignore_list_page.enter_ignorelist_mac(
            ignore_list=["B1:B2:C3:D4:E5:F6", "B1:B2:C3:D4:E5:XX", "B1:b2:c3:d4:xx:xx", "B1:B2:C3:XX:xx:1E",
                         "B1:B2:C3:XX:E5:XX", "B3:D4:E5:F6:A7:B8"])
        self.seleniumdriver.screen_shot(file="test_3_6_6_clear_ignore_list_manually_add_mac_ignore_list")
        self.source_white_ignore_list_page.click_save_btn()
        time.sleep(900)  # wait 15 mins to build fingerprint
        r_1 = self.source_white_ignore_list_page.verify_fingerprint_timestamp()
        assert r_1 == True
        time.sleep(1)
        self.loginpage.sign_out()
        time.sleep(1)

    @pytest.mark.run(18)
    def test_3_6_7_upload_ignore_list_csv(self):
        self.source_white_ignore_list_page.click_access_point_btn()
        self.source_white_ignore_list_page.click_wifi_btn()
        self.source_white_ignore_list_page.delete_ignore_mac_addresses()
        self.source_white_ignore_list_page.upload_ignore_list_csv()
        self.seleniumdriver.screen_shot(file="test_3_6_7_upload_ignore_list_csv")
        self.source_white_ignore_list_page.click_save_btn()
        time.sleep(900)  # wait 15 mins to build fingerprint
        r_1 = self.source_white_ignore_list_page.verify_fingerprint_timestamp()
        assert r_1 == True
        time.sleep(1)
        self.loginpage.sign_out()
        time.sleep(1)

    @pytest.mark.run(19)
    def test_3_6_8_upload_white_ignore_list_csv(self):
        self.source_white_ignore_list_page.click_access_point_btn()
        self.source_white_ignore_list_page.click_wifi_btn()
        self.source_white_ignore_list_page.delete_white_mac_addresses()
        self.source_white_ignore_list_page.delete_ignore_mac_addresses()
        self.seleniumdriver.screen_shot(file="test_3_6_8_upload_white_ignore_list_csv_deleted_white_ignore")
        self.source_white_ignore_list_page.upload_white_list_csv()
        self.source_white_ignore_list_page.upload_ignore_list_csv()
        self.seleniumdriver.screen_shot(file="test_3_6_8_upload_white_ignore_list_csv_upload")
        self.source_white_ignore_list_page.click_save_btn()
        time.sleep(900)  # wait 15 mins to build fingerprint
        r_1 = self.source_white_ignore_list_page.verify_fingerprint_timestamp()
        assert r_1 == True
        time.sleep(1)
        self.loginpage.sign_out()
        time.sleep(1)
