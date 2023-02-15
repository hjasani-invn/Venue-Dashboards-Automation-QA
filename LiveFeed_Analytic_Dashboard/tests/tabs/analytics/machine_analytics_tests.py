import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from pages.tabs.analytics.machine_analytics_page import MachineAnalyticsTabPage

import unittest

from tests import conftest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class MachineAnalyticsTabTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.machineanalyticstabpage = MachineAnalyticsTabPage(self.driver)
        self.loginpage = LoginPage(self.driver)

    # @pytest.mark.run(1)
    # def test_login_nominal(self):
    #     self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

    @pytest.mark.run(1)
    def test_3_9_1_machine_analytics_query(self):
        "this test is not loading any data, skeleton is ready for future expansion"
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.machineanalyticstabpage.select_machine_analytic_downloads_tab()
        self.machineanalyticstabpage.enter_venue_name(v_n="ICA_2021")
        self.machineanalyticstabpage.select_all_machines()
        self.machineanalyticstabpage.choose_date_and_time(s_date="02/01/2023", s_time="0000", e_date="02/08/2023", e_time="1159")
        self.machineanalyticstabpage.click_search()
        self.machineanalyticstabpage.remove_search_panel_to_left()
        pass


