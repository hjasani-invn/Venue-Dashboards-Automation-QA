import time

import pytest

from pages.access_points.move_entries_page import MoveEntriesPage
from pages.login_page import LoginPage
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
        self.move_entries_page.click_access_point_btn()
        self.move_entries_page.click_wifi_btn()



    @pytest.mark.run(1)
    def test_3_6_2_1_without_arrow_source_to_white_move_mac(self):
        self.move_entries_page.without_arrow_source_to_white()

    # @pytest.mark.run(2)
    # def test_3_6_2_4_arrow_source_to_white_move_mac(self):
    #     self.move_entries_page.move_mac_from_source_to_white()
    #
    # @pytest.mark.run(3)
    # def test_3_6_2_3_all_mac_move_to_source(self):
    #     self.move_entries_page.all_mac_move_to_source()
    #
    # @pytest.mark.run(4)
    # def test_3_6_2_4_arrow_source_to_white_move_mac(self):
    #     self.move_entries_page.move_mac_from_source_to_white()
    #     # self.move_entries_page.click_save_btn()
    #
    # @pytest.mark.run(5)
    # def test_3_6_2_5_arrow_source_to_ignore_move_mac(self):
    #     self.move_entries_page.move_mac_from_source_to_ignore()

