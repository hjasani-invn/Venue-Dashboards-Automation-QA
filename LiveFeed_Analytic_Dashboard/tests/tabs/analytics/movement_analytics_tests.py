import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.tabs.analytics.movement_analytics_page import MovementAnalyticsTabPage
from pages.home.login_page import LoginPage
import unittest
from tests import conftest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class MovementAnalyticsTabTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.movementanalyticstabpage = MovementAnalyticsTabPage(self.driver)
        self.loginpage = LoginPage(self.driver)

    # @pytest.mark.run(1)
    # def test_3_1_1_login_nominal(self):
    #     self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

    @pytest.mark.run(2)
    def test_3_6_1_populate_movement_analytic_time_filter(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.movementanalyticstabpage.select_analytic_movement_analytic_tab()
        time.sleep(2)
        self.movementanalyticstabpage.enter_venue_name(v_n="ICA_2021")
        self.movementanalyticstabpage.select_floor(f_n='F4')
        self.movementanalyticstabpage.add_time_range()
        self.movementanalyticstabpage.select_year_month(desired_start_year=2022, desired_start_month="December",
                                                        desired_start_date='14',
                                                        desired_end_year=2023, desired_end_month="February",
                                                        desired_end_date='1',
                                                        # desired_end_year=2023, desired_end_month="December", desired_end_date='1',
                                                        start_time="1212", end_time="2129")
        # self.movementanalyticstabpage.select_year_month(desired_start_year=2022, desired_start_month="November",
        #                                                 desired_start_date='10',
        #                                                 desired_end_year=2022, desired_end_month="December",
        #                                                 desired_end_date='4',
        #                                                 # desired_end_year=2023, desired_end_month="December", desired_end_date='1',
        #                                                 start_time="1212", end_time="2129")
        time.sleep(5)
        self.movementanalyticstabpage.screen_shot_for_test_3_6_1_populate_movement_analytic_time_filter()

    @pytest.mark.run(3)
    def test_3_6_2_movement_analytics_by_date(self):
        self.movementanalyticstabpage.select_analytic_movement_analytic_tab()
        time.sleep(2)
        self.movementanalyticstabpage.enter_venue_name(v_n="ICA_2021")
        self.movementanalyticstabpage.select_floor(f_n='F4')
        self.movementanalyticstabpage.select_user_drop_down_for_users()
        self.movementanalyticstabpage.add_time_range()
        self.movementanalyticstabpage.select_year_month(desired_start_year=2022, desired_start_month="December",
                                                        desired_start_date='14',
                                                        desired_end_year=2023, desired_end_month="February",
                                                        desired_end_date='1',
                                                        start_time="1212", end_time="2129")
        time.sleep(5)
        self.movementanalyticstabpage.screen_shot_for_test_3_6_2_movement_analytics_by_date()