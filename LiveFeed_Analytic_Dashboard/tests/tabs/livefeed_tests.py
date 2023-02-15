import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from pages.tabs.livefeed_page import LiveFeedTabPage
import unittest
from tests import conftest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LiveFeedTabTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.livefeedtabpage = LiveFeedTabPage(self.driver)

    @pytest.mark.run(1)
    def test_3_1_1_login_nominal(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

    # @pytest.mark.run(2)
    # def test_select_dropdown(self):
    #     self.livefeedtabpage.click_drop_down()
    #
    # @pytest.mark.run(3)
    # def test_x_select_venue(self):
    #     self.livefeedtabpage.select_venue()
    #
    # @pytest.mark.run(4)
    # def test_online_user(self):
    #     self.livefeedtabpage.select_venue()
    #     self.livefeedtabpage.toggle_online_user_btn()
    #
    # def test_show_one_active_user(self):
    #     print("test remained to automate")
    #     pass
    #
    # def test_two_user_same_trajcatory(self):
    #     print("test remained to automate")
    #     pass
    #
    # def test_two_user_different_trajcatory(self):
    #     print("test remained to automate")
    #     pass
    #
    # @pytest.mark.run(5)
    # def test_sort_group_order(self):
    #     self.livefeedtabpage.grp_srt()
    #
    # @pytest.mark.run(6)
    # def test_collapse_group_order(self):
    #     self.livefeedtabpage.collapse_grp()
    #
    # def test_3_2_8_select_a_group(self):
    #     print("test remained to automate")
    #     pass
    #
    # def test_3_2_9_select_a_user(self):
    #     print("test remained to automate")
    #     pass

    @pytest.mark.run(2)
    def test_3_2_10_change_floor(self):
        self.livefeedtabpage.select_venue()
        self.livefeedtabpage.change_venue_floor()


