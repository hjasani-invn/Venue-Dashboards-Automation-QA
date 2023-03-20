import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.tabs.analytics.heatmap_page import HeatmapTabPage
from pages.home.login_page import LoginPage
import unittest
from tests import conftest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class HeatmapTabTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.heatmaptabpage = HeatmapTabPage(self.driver)
        self.loginpage = LoginPage(self.driver)

    # @pytest.mark.run(1)
    # def test_3_1_1_login_nominal(self):
    #     self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

    def test_3_4_1_populate_heatmap(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.heatmaptabpage.select_analytic_heatmap_tab()
        self.heatmaptabpage.enter_venue_name(v_n='ICA_2021')
        self.heatmaptabpage.select_floor()
        self.heatmaptabpage.choose_date_and_time(s_date="11/03/2022", s_time="0000", e_date="11/06/2022", e_time="2359") # MM/DD/YYY, HHMM-':' not required in between HR:MM
        self.heatmaptabpage.select_timezone("America/Denver")
        self.heatmaptabpage.click_search()
        self.heatmaptabpage.select_all_users()

