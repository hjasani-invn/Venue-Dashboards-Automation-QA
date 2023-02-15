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

    @pytest.mark.run(1)
    def test_3_7_1_login_nominal(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

    @pytest.mark.run(2)
    def test_3_7_x_populate_distance_analytics_map_diagram(self):
        self.distanceanalyticstabpage.select_analytic_distance_analytics_tab()
        self.distanceanalyticstabpage.enter_venue_name(v_n="ICA_2021")
        self.distanceanalyticstabpage.select_floor(f_n="Fourth Floor")
        self.distanceanalyticstabpage.choose_date_and_time(s_date="11/24/2022", s_time="0000", e_date="01/27/2023",
                                                           e_time="2359")  # ':' not required in between HR:MM
        self.distanceanalyticstabpage.select_timezone("America/Denver")
        self.distanceanalyticstabpage.click_search()
        self.distanceanalyticstabpage.take_screenshot_for_all()
