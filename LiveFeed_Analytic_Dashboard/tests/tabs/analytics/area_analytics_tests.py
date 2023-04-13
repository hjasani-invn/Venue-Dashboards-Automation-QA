import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver
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
        self.seleniumdriver = SeleniumDriver(self.driver)

        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.areaanalyticstabpage.select_analytic_area_analytic_tab()




    def test_3_5_1_populate_area_analytic(self):
        self.areaanalyticstabpage.enter_venue_name(v_n='ICA_2021')
        self.areaanalyticstabpage.select_floor()
        self.areaanalyticstabpage.choose_date_and_time(s_date="11/16/2022", s_time="0001", e_date="01/21/2023", e_time="2321") # ':' not required in between HR:MM
        # self.areaanalyticstabpage.choose_date_and_time(s_date="01/21/2023", s_time="0001", e_date="01/21/2023", e_time="2321") # ':' not required in between HR:MM
        self.areaanalyticstabpage.select_timezone("America/Denver")
        # self.seleniumdriver.pytest_screenshot()
        events = self.areaanalyticstabpage.verify_events_available()
        assert (events > 0)

        self.areaanalyticstabpage.click_search()
        # self.areaanalyticstabpage.select_all_users()
        self.areaanalyticstabpage.select_specific_data()
        # self.seleniumdriver.pytest_screenshot()
        frame = self.areaanalyticstabpage.is_frame_appear()
        assert frame == True
        self.seleniumdriver.screen_shot(file="test_3_5_1_populate_area_analytic")


        # self.seleniumdriver.pytest_screenshot()
        # r_1 = self.areaanalyticstabpage.verify_data_shown()
        # assert r_1 == "Reset Zoom"


