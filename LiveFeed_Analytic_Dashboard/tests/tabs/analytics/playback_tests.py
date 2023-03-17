import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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

    @pytest.mark.run(1)
    def test_3_1_1_login_nominal(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

    def test_3_1_2_select_analytics_playback_tab(self):
        self.playbacktabtabpage.select_analytic_playback_tab()

    def test_3_3_1_filter_sessions_by_time_playback(self):
        self.playbacktabtabpage.enter_venue_name(v_n="ICA_2021")
        self.playbacktabtabpage.select_floor()
        # self.playbacktabtabpage.set_duration()
        self.playbacktabtabpage.choose_date_and_time("12/10/2022", "0121", "03/01/2023", "2330") #M/D/Y
        self.playbacktabtabpage.select_timezone("America/Denver")
        self.playbacktabtabpage.select_draw_style()
        self.playbacktabtabpage.click_search()
        self.playbacktabtabpage.select_all_users()
        self.playbacktabtabpage.play_btn()

    def test_3_3_2_show_zones(self):
        self.playbacktabtabpage.show_zones()