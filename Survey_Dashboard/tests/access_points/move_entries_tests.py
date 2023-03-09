import time

import pytest

from pages.access_points.move_entries_page import MoveEntriesPage
from pages.home.login_page import LoginPage
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class MoveEntriesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.move_entries_page = MoveEntriesPage(self.driver)

        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

        self.move_entries_page.click_admin()
        self.move_entries_page.click_survey_editor()
        self.move_entries_page.enter_venue()
        self.move_entries_page.select_floor()

    @pytest.mark.skip
    # @pytest.mark.run(20)
    def test_3_6_2_1_without_arrow_source_to_white_move_mac(self):
        "drag and drop functionality not working: test case skip/commented"
        self.move_entries_page.without_arrow_source_to_white()


    @pytest.mark.skip
    # @pytest.mark.run(21)
    def test_3_6_2_2_without_arrow_source_to_ignore_move_mac(self):
        "drag and drop functionality not working: test case skip/commented"
        self.move_entries_page.without_arrow_source_to_ignore()


    @pytest.mark.run(22)
    def test_3_6_2_3_arrow_source_to_white_move_mac(self):
        self.move_entries_page.click_access_point_btn()
        self.move_entries_page.click_wifi_btn()
        self.move_entries_page.move_mac_from_source_to_white()
        self.move_entries_page.cancel_btn()
        time.sleep(1)
        self.loginpage.sign_out()
        time.sleep(1)

    @pytest.mark.run(23)
    def test_3_6_2_4_all_mac_move_to_source(self):
        self.move_entries_page.click_access_point_btn()
        self.move_entries_page.click_wifi_btn()
        self.move_entries_page.all_mac_move_to_source()
        self.move_entries_page.cancel_btn()
        time.sleep(1)
        self.loginpage.sign_out()
        time.sleep(1)

    @pytest.mark.run(24)
    def test_3_6_2_5_arrow_source_to_white_move_mac(self):
        self.move_entries_page.click_access_point_btn()
        self.move_entries_page.click_wifi_btn()
        self.move_entries_page.move_mac_from_source_to_white()
        self.move_entries_page.cancel_btn()
        time.sleep(1)
        self.loginpage.sign_out()
        time.sleep(1)

    @pytest.mark.run(25)
    def test_3_6_2_6_arrow_source_to_ignore_move_mac(self):
        self.move_entries_page.click_access_point_btn()
        self.move_entries_page.click_wifi_btn()
        self.move_entries_page.move_mac_from_source_to_ignore()
        self.move_entries_page.cancel_btn()
        time.sleep(1)
        self.loginpage.sign_out()
        time.sleep(1)