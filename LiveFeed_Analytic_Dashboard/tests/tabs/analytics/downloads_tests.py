import os
import sys
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

        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.downloadstabpage.select_analytic_downloads_tab()

    @pytest.mark.run(1)
    def test_3_8_1_1_data_download_distances(self):
        self.downloadstabpage.select_distance()
        time.sleep(1)
        self.downloadstabpage.select_venue(venue_name="ICA_2021")
        self.downloadstabpage.click_dates()
        # self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="December",
        #                                                    desired_start_date='14')
        # self.downloadstabpage.select_end_year_month_date(desired_end_year=2023, desired_end_month="January",
        #                                                  desired_end_date='1')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="August",
                                                           desired_start_date='1')
        self.downloadstabpage.select_end_year_month_date(desired_end_year=2022, desired_end_month="December",
                                                         desired_end_date='31')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.click_out()
        # self.seleniumdriver.pytest_screenshot()
        r_1 = self.downloadstabpage.verify_data_shown()
        assert r_1 == True
        self.downloadstabpage.select_all_files()
        self.downloadstabpage.download_btn()
        # os.rename(from_file_name, to_file_name)
        os.rename("..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets.zip",
                  "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_distances_1.zip")

        # self.downloadstabpage.verify_file()
        # self.downloadstabpage.delete_downloaded_file()
        self.seleniumdriver.screen_shot(file="test_3_8_1_1_data_download_distances")

    @pytest.mark.run(2)
    def test_3_8_1_2_data_download_movement(self):
        self.downloadstabpage.select_movement()
        time.sleep(1)
        self.downloadstabpage.select_venue(venue_name="ICA_2021")
        self.downloadstabpage.click_dates()
        # self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="June",
        #                                                    desired_start_date='20')
        # self.downloadstabpage.select_end_year_month_date(desired_end_year=2022, desired_end_month="December",
        #                                                  desired_end_date='20')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="August",
                                                           desired_start_date='1')
        self.downloadstabpage.select_end_year_month_date(desired_end_year=2022, desired_end_month="December",
                                                         desired_end_date='31')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.click_out()
        # self.seleniumdriver.pytest_screenshot()
        r_1 = self.downloadstabpage.verify_data_shown()
        assert r_1 == True
        self.downloadstabpage.select_all_files()
        self.downloadstabpage.download_btn()
        # os.rename(from_file_name, to_file_name)
        os.rename(
            "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets.zip",
            "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_movements_1.zip")
        # self.downloadstabpage.verify_file()
        # self.downloadstabpage.delete_downloaded_file()
        self.seleniumdriver.screen_shot(file="test_3_8_1_2_data_download_movement")

    @pytest.mark.run(3)
    def test_3_8_1_3_data_download_playback(self):
        self.downloadstabpage.select_playback()
        time.sleep(1)
        self.downloadstabpage.select_venue(venue_name="ICA_2021")
        self.downloadstabpage.click_dates()
        # self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="June",
        #                                                    desired_start_date='20')
        # self.downloadstabpage.select_end_year_month_date(desired_end_year=2022, desired_end_month="December",
        #                                                  desired_end_date='20')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="August",
                                                           desired_start_date='1')
        self.downloadstabpage.select_end_year_month_date(desired_end_year=2022, desired_end_month="December",
                                                         desired_end_date='31')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.click_out()
        # self.seleniumdriver.pytest_screenshot()
        r_1 = self.downloadstabpage.verify_data_shown()
        assert r_1 == True
        self.downloadstabpage.select_all_files()
        self.downloadstabpage.download_btn()
        # os.rename(from_file_name, to_file_name)
        os.rename(
            "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets.zip",
            "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_playback_1.zip")
        # self.downloadstabpage.verify_file()
        # self.downloadstabpage.delete_downloaded_file()
        self.seleniumdriver.screen_shot(file="test_3_8_1_3_data_download_playback")

    @pytest.mark.run(4)
    def test_3_8_1_4_data_download_assets_playback(self):
        self.downloadstabpage.select_assets_playback()
        time.sleep(1)
        self.downloadstabpage.select_venue(venue_name="ICA_2021")
        self.downloadstabpage.click_dates()
        # self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="October",
        #                                                    desired_start_date='3')
        # self.downloadstabpage.select_end_year_month_date(desired_end_year=2023, desired_end_month="January",
        #                                                  desired_end_date='20')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="August",
                                                           desired_start_date='1')
        self.downloadstabpage.select_end_year_month_date(desired_end_year=2022, desired_end_month="December",
                                                         desired_end_date='31')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.click_out()
        # self.seleniumdriver.pytest_screenshot()
        r_1 = self.downloadstabpage.verify_data_shown()
        assert r_1 == True
        self.downloadstabpage.select_all_files()
        self.downloadstabpage.download_btn()
        # ROOT = sys.path[1]
        # print(ROOT)
        # downloaded_dir = os.path.join(ROOT, "Downloaded_Files")
        os.renames("..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets.zip",
                   "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_assets_playback_1.zip")

        # os.rename(from_file_name, to_file_name)
        # os.rename(
        #     "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets.zip",
        #     "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_assets_playback_1.zip")
        # self.downloadstabpage.verify_file()
        # self.downloadstabpage.delete_downloaded_file()
        self.seleniumdriver.screen_shot(file="test_3_8_1_4_data_download_assets_playback")

    def test_3_8_1_5_compare_files(self):
        # Distances
        print("----------Distances----------")
        self.downloadstabpage.select_distance()
        time.sleep(1)
        self.downloadstabpage.select_venue(venue_name="ICA_2021")
        self.downloadstabpage.click_dates()
        self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="August",
                                                           desired_start_date='1')
        self.downloadstabpage.select_end_year_month_date(desired_end_year=2022, desired_end_month="December",
                                                         desired_end_date='31')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.click_out()
        time.sleep(2)
        self.downloadstabpage.select_all_files()
        self.downloadstabpage.download_btn()
        os.rename("..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets.zip",
                  "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_distances_2.zip")
        # self.seleniumdriver.pytest_screenshot()
        compare_distance = self.downloadstabpage.compare_zips(
            zip1="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_distances_1.zip",
            zip2="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_distances_2.zip")
        assert compare_distance == True
        self.downloadstabpage.delete_downloaded_file_new(
            zip1="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_distances_1.zip",
            zip2="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_distances_2.zip")

        # Movements
        print("----------Movements----------")
        self.seleniumdriver.refresh_page()
        self.downloadstabpage.select_movement()
        time.sleep(1)
        self.downloadstabpage.select_venue(venue_name="ICA_2021")
        self.downloadstabpage.click_dates()
        self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="August",
                                                           desired_start_date='1')
        self.downloadstabpage.select_end_year_month_date(desired_end_year=2022, desired_end_month="December",
                                                         desired_end_date='31')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.click_out()
        time.sleep(2)
        self.downloadstabpage.select_all_files()
        self.downloadstabpage.download_btn()
        os.rename("..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets.zip",
                  "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_movements_2.zip")
        # self.seleniumdriver.pytest_screenshot()
        compare_movements = self.downloadstabpage.compare_zips(
            zip1="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_movements_1.zip",
            zip2="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_movements_2.zip")
        assert compare_movements == True
        self.downloadstabpage.delete_downloaded_file_new(
            zip1="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_movements_1.zip",
            zip2="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_movements_2.zip")

        # Playback
        print("----------Playback----------")
        self.seleniumdriver.refresh_page()
        self.downloadstabpage.select_playback()
        time.sleep(1)
        self.downloadstabpage.select_venue(venue_name="ICA_2021")
        self.downloadstabpage.click_dates()
        self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="August",
                                                           desired_start_date='1')
        self.downloadstabpage.select_end_year_month_date(desired_end_year=2022, desired_end_month="December",
                                                         desired_end_date='31')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.click_out()
        time.sleep(2)
        self.downloadstabpage.select_all_files()
        self.downloadstabpage.download_btn()
        os.rename("..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets.zip",
                  "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_playback_2.zip")
        # self.seleniumdriver.pytest_screenshot()
        compare_playback = self.downloadstabpage.compare_zips(
            zip1="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_playback_1.zip",
            zip2="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_playback_2.zip")
        assert compare_playback == True
        self.downloadstabpage.delete_downloaded_file_new(
            zip1="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_playback_1.zip",
            zip2="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_playback_2.zip")

        # Assets Playback
        print("----------Assets Playback----------")
        self.seleniumdriver.refresh_page()
        self.downloadstabpage.select_assets_playback()
        time.sleep(1)
        self.downloadstabpage.select_venue(venue_name="ICA_2021")
        self.downloadstabpage.click_dates()
        self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="August",
                                                           desired_start_date='1')
        self.downloadstabpage.select_end_year_month_date(desired_end_year=2022, desired_end_month="December",
                                                         desired_end_date='31')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.click_out()
        time.sleep(2)
        self.downloadstabpage.select_all_files()
        self.downloadstabpage.download_btn()
        os.rename("..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets.zip",
                  "..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_assets_playback_2.zip")
        # self.seleniumdriver.pytest_screenshot()
        compare_asset_playback = self.downloadstabpage.compare_zips(
            zip1="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_assets_playback_1.zip",
            zip2="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_assets_playback_2.zip")
        assert compare_asset_playback == True
        # ALl delete together
        self.downloadstabpage.delete_downloaded_file_new(
            zip1="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_assets_playback_1.zip",
            zip2="..\\LiveFeed_Analytic_Dashboard\\Downloaded_Files\\datasets_assets_playback_2.zip")

    def test_4_8_6_existing_data_download(self):
        self.downloadstabpage.select_distance()
        time.sleep(1)
        self.downloadstabpage.select_venue(venue_name="ICA_2021")
        self.downloadstabpage.click_dates()
        self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="June",
                                                           desired_start_date='20')
        self.downloadstabpage.select_end_year_month_date(desired_end_year=2022, desired_end_month="June",
                                                         desired_end_date='25')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.click_out()
        time.sleep(2)
        self.downloadstabpage.select_all_files()
        self.downloadstabpage.download_btn()

    def test_4_8_7_no_data_available(self):
        self.downloadstabpage.select_assets_playback()
        time.sleep(1)
        self.downloadstabpage.select_venue(venue_name="ICA_2021")
        self.downloadstabpage.click_dates()
        self.downloadstabpage.select_start_year_month_date(desired_start_year=2022, desired_start_month="November",
                                                           desired_start_date='1')
        self.downloadstabpage.select_end_year_month_date(desired_end_year=2022, desired_end_month="November",
                                                         desired_end_date='7')  # MM/DD/YYYY - MM/DD/YYYY, M/DD/YYYY
        self.downloadstabpage.click_out()
        time.sleep(2)
        self.downloadstabpage.select_all_files()
        self.downloadstabpage.download_btn()
        # self.seleniumdriver.pytest_screenshot()
        r_1 = self.downloadstabpage.verify_data_shown()
        assert r_1 == True
        self.downloadstabpage.delete_all_downloaded()
