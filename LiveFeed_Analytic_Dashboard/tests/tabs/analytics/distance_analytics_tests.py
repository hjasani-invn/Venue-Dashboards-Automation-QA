import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.tabs.analytics.distance_analytics_page import DistanceAnalyticsTabPage
from pages.home.login_page import LoginPage
import unittest
from tests import conftest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DistanceAnalyticsTabTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.distanceanalyticstabpage = DistanceAnalyticsTabPage(self.driver)
        self.loginpage = LoginPage(self.driver)

    # @pytest.mark.run(1)
    # def test_3_7_1_login_nominal(self):
    #     self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

    @pytest.mark.run(2)
    def test_3_7_1_populate_distance_analytics_map_diagram(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.distanceanalyticstabpage.select_analytics_distance_analytics_tab()
        time.sleep(1)
        self.distanceanalyticstabpage.enter_venue_name(v_n="ICA_2021")
        # self.distanceanalyticstabpage.select_floor(f_n="Fourth Floor")
        self.distanceanalyticstabpage.select_floor(f_n="F4")
        self.distanceanalyticstabpage.choose_date_and_time(s_date="11/24/2022", s_time="0000", e_date="01/27/2023",
                                                           e_time="2359")  # ':' not required in between HR:MM
        self.distanceanalyticstabpage.select_timezone("America/Denver")
        self.distanceanalyticstabpage.click_search()
        time.sleep(2)
        self.distanceanalyticstabpage.take_screenshot_for_all()
