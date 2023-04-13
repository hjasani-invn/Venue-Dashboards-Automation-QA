import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver
from pages.tabs.analytics.playback_page import PlaybackTabPage
from pages.home.login_page import LoginPage
import unittest
from tests import conftest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class PlaybackTabTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.playbacktabtabpage = PlaybackTabPage(self.driver)
        self.loginpage = LoginPage(self.driver)

        self.seleniumdriver = SeleniumDriver(self.driver)

        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.playbacktabtabpage.select_analytic_playback_tab()

    # @pytest.mark.run(1)
    # def test_3_3_1_login_nominal(self):
    #     self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

    # def test_3_3_2_select_analytics_playback_tab(self):
    #     # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
    #     # self.playbacktabtabpage.select_analytic_playback_tab()
    #     print("if playback tab is opened, then test is pass")

    def test_3_3_1_filter_sessions_by_time_playback_timezone_america(self):
        self.playbacktabtabpage.enter_venue_name(v_n="ICA_2021")
        self.playbacktabtabpage.select_floor()
        # self.playbacktabtabpage.set_duration()
        self.playbacktabtabpage.choose_date_and_time("12/10/2022", "0121", "03/01/2023",
                                                     "2330")  # MM/DD/YYYY, HHMM-':' not required in between HH:MM
        # assert result_1 == "Start date should be greater than "
        self.playbacktabtabpage.select_timezone("America/Denver")
        self.playbacktabtabpage.select_draw_style_dot()
        result_1 = self.playbacktabtabpage.click_search()
        # self.seleniumdriver.pytest_screenshot()
        assert result_1 is None
        # assert result_1 != "true"
        # self.playbacktabtabpage.select_all_users()
        self.playbacktabtabpage.select_specific_data()
        self.playbacktabtabpage.play_btn()
        self.seleniumdriver.screen_shot(file="test_3_3_1_filter_sessions_by_time_playback_timezone_america")



    def test_3_3_2_filter_sessions_by_time_playback_timezone_japan(self):
        self.playbacktabtabpage.enter_venue_name(v_n="ICA_2021")
        self.playbacktabtabpage.select_floor()
        # self.playbacktabtabpage.set_duration()
        self.playbacktabtabpage.choose_date_and_time("12/10/2022", "0121", "03/01/2023",
                                                     "2330")  # MM/DD/YYYY, HHMM-':' not required in between HH:MM
        # assert result_1 == "Start date should be greater than "
        self.playbacktabtabpage.select_timezone("Jap")
        self.playbacktabtabpage.select_draw_style_dot()
        result_1 = self.playbacktabtabpage.click_search()
        # self.seleniumdriver.pytest_screenshot()
        assert result_1 is None
        # assert result_1 != "true"
        # self.playbacktabtabpage.select_all_users()
        self.playbacktabtabpage.select_specific_data()
        self.playbacktabtabpage.play_btn()
        self.seleniumdriver.screen_shot(file="test_3_3_2_filter_sessions_by_time_playback_timezone_japan")


    def test_3_3_3_filter_sessions_by_time_playback_all_users(self):
        self.playbacktabtabpage.enter_venue_name(v_n="ICA_2021")
        self.playbacktabtabpage.select_floor()
        # self.playbacktabtabpage.set_duration()
        self.playbacktabtabpage.choose_date_and_time("12/10/2022", "0121", "03/01/2023",
                                                     "2330")  # MM/DD/YYYY, HHMM-':' not required in between HH:MM
        # assert result_1 == "Start date should be greater than "
        self.playbacktabtabpage.select_timezone("America/Denver")
        self.playbacktabtabpage.select_draw_style_dot()
        result_1 = self.playbacktabtabpage.click_search()
        # self.seleniumdriver.pytest_screenshot()
        assert result_1 is None
        # assert result_1 != "true"
        self.playbacktabtabpage.select_all_users()
        self.playbacktabtabpage.play_btn()
        self.seleniumdriver.screen_shot(file="test_3_3_3_filter_sessions_by_time_playback_all_users")




    def test_3_3_4_filter_sessions_with_draw_types(self):
        self.playbacktabtabpage.enter_venue_name(v_n="ICA_2021")
        self.playbacktabtabpage.select_floor()
        # self.playbacktabtabpage.set_duration()
        self.playbacktabtabpage.choose_date_and_time("12/10/2022", "0121", "03/01/2023",
                                                     "2330")  # MM/DD/YYYY, HHMM-':' not required in between HH:MM
        # assert result_1 == "Start date should be greater than "
        self.playbacktabtabpage.select_timezone("America/Denver")
        # DOT
        self.playbacktabtabpage.select_draw_style_dot()
        result_1 = self.playbacktabtabpage.click_search()
        # self.seleniumdriver.pytest_screenshot()
        assert result_1 is None
        # assert result_1 != "true"
        self.playbacktabtabpage.select_all_users()
        self.playbacktabtabpage.play_btn()
        self.seleniumdriver.screen_shot(file="test_3_3_4_filter_sessions_with_draw_type_dot")


        # LINE
        self.playbacktabtabpage.select_draw_style_line()
        result_1 = self.playbacktabtabpage.click_search()
        # self.seleniumdriver.pytest_screenshot()
        assert result_1 is None
        # assert result_1 != "true"
        self.playbacktabtabpage.select_all_users()
        self.playbacktabtabpage.play_btn()
        self.seleniumdriver.screen_shot(file="test_3_3_4_filter_sessions_with_draw_type_line")


        # TRAIL
        self.playbacktabtabpage.select_draw_style_trail()
        result_1 = self.playbacktabtabpage.click_search()
        # self.seleniumdriver.pytest_screenshot()
        assert result_1 is None
        # assert result_1 != "true"
        self.playbacktabtabpage.select_all_users()
        self.playbacktabtabpage.play_btn()
        self.seleniumdriver.screen_shot(file="test_3_3_4_filter_sessions_with_draw_type_trail")



    def test_3_3_5_show_zones(self):
        # self.seleniumdriver.pytest_screenshot()
        r_1 = self.playbacktabtabpage.show_zones()
        assert r_1 == "28F"
        self.seleniumdriver.screen_shot(file="test_3_3_5_show_zones")

