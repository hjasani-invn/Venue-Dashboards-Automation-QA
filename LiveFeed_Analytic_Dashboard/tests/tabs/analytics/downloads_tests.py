import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.tabs.analytics.downloads_page import DownloadsTabPage
from pages.tabs.analytics.movement_analytics_page import MovementAnalyticsTabPage

from pages.home.login_page import LoginPage
from base.selenium_driver import SeleniumDriver
import unittest

from tests import conftest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DownloadsTabTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.downloadstabpage = DownloadsTabPage(self.driver)
        self.movementanalyticstabpage = MovementAnalyticsTabPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)

    # @pytest.mark.run(1)
    # def test_3_8_1_login_nominal(self):
    #     self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

    @pytest.mark.run(1)
    def test_3_8_1_1_data_download_distances(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.downloadstabpage.select_analytic_downloads_tab()
        self.downloadstabpage.select_distance()
        # self.downloadstabpage.select_venue(venue_name="6 floors venue")
        self.downloadstabpage.select_venue(venue_name="ICA_2021")
        # self.downloadstabpage.add_dates(dates="12/05/2022 - 01/26/2023") #MM/DD/YYYY - MM/DD/YYYY
        self.downloadstabpage.click_dates()
        self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="November",
                                                           desired_start_date='10')
        self.downloadstabpage.select_end_year_month_date(desired_end_year=2023, desired_end_month="January",
                                                         desired_end_date='4')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.click_out()
        self.downloadstabpage.select_all_files()
        self.downloadstabpage.download_btn()
        self.downloadstabpage.verify_file()
        self.downloadstabpage.delete_downloaded_file()
        self.seleniumdriver.screen_shot(file="test_3_8_1_1_data_download_distances")

    @pytest.mark.run(2)
    def test_3_8_1_2_data_download_movement(self):
        self.downloadstabpage.select_analytic_downloads_tab()
        self.downloadstabpage.select_movement()
        self.downloadstabpage.select_venue(venue_name="ICA_2021")
        # self.downloadstabpage.add_dates(dates="01/09/2022 - 01/01/2023")  # MM/DD/YYYY - MM/DD/YYYY
        self.downloadstabpage.click_dates()
        self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="June",
                                                           desired_start_date='20')
        self.downloadstabpage.select_end_year_month_date(desired_end_year=2022, desired_end_month="December",
                                                         desired_end_date='20')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.click_out()
        self.downloadstabpage.select_all_files()
        self.downloadstabpage.download_btn()
        self.downloadstabpage.verify_file()
        self.downloadstabpage.delete_downloaded_file()
        self.seleniumdriver.screen_shot(file="test_3_8_1_2_data_download_movement")


    @pytest.mark.run(3)
    def test_3_8_1_3_data_download_playback(self):
        self.downloadstabpage.select_analytic_downloads_tab()
        self.downloadstabpage.select_playback()
        self.downloadstabpage.select_venue(venue_name="ICA_2021")
        # self.downloadstabpage.add_dates(dates="12/09/2022 - 01/14/2023")  # MM/DD/YYYY - MM/DD/YYYY
        self.downloadstabpage.click_dates()
        self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="June",
                                                           desired_start_date='20')
        self.downloadstabpage.select_end_year_month_date(desired_end_year=2022, desired_end_month="December",
                                                         desired_end_date='20')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.click_out()
        self.downloadstabpage.select_all_files()
        self.downloadstabpage.download_btn()
        self.downloadstabpage.verify_file()
        self.downloadstabpage.delete_downloaded_file()
        self.seleniumdriver.screen_shot(file="test_3_8_1_3_data_download_playback")


    @pytest.mark.run(4)
    def test_3_8_1_4_data_download_assets_playback(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.downloadstabpage.select_analytic_downloads_tab()
        self.downloadstabpage.select_assets_playback()
        self.downloadstabpage.select_venue(venue_name="ICA_2021")
        # self.downloadstabpage.add_dates(dates="01/09/2023 - 01/13/2023")  # MM/DD/YYYY - MM/DD/YYYY
        self.downloadstabpage.click_dates()
        self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="October",
                                                           desired_start_date='3')
        self.downloadstabpage.select_end_year_month_date(desired_end_year=2023, desired_end_month="January",
                                                         desired_end_date='20')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.click_out()
        self.downloadstabpage.select_all_files()
        self.downloadstabpage.download_btn()
        self.downloadstabpage.verify_file()
        self.downloadstabpage.delete_downloaded_file()
        self.seleniumdriver.screen_shot(file="test_3_8_1_4_data_download_assets_playback")

