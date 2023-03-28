import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.tabs.analytics.area_analytics_page import AreaAnalyticsTabPage
from pages.home.login_page import LoginPage
import unittest
from tests import conftest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AreaAnalyticsTabTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.areaanalyticstabpage = AreaAnalyticsTabPage(self.driver)
        self.loginpage = LoginPage(self.driver)

    # @pytest.mark.run(1)
    # def test_3_1_1_login_nominal(self):
    #     self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

    def test_3_5_1_populate_area_analytic(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.areaanalyticstabpage.select_analytic_area_analytic_tab()
        self.areaanalyticstabpage.enter_venue_name()
        self.areaanalyticstabpage.select_floor()
        self.areaanalyticstabpage.choose_date_and_time(s_date="11/16/2022", s_time="0001", e_date="01/21/2023", e_time="2321") # ':' not required in between HR:MM
        self.areaanalyticstabpage.select_timezone("America/Denver")
        self.areaanalyticstabpage.click_search()
        self.areaanalyticstabpage.select_all_users()
        r_1 = self.areaanalyticstabpage.verify_data_shown()
        assert r_1 == "Reset Zoom"

