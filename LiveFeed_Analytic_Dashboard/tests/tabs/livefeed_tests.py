import pytest

from base.selenium_driver import SeleniumDriver
from pages.home.login_page import LoginPage
from pages.tabs.livefeed_page import LiveFeedTabPage
import unittest
from pytest_html_reporter import attach


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LiveFeedTabTests(unittest.TestCase):
    reason = "cannot automate"

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.livefeedtabpage = LiveFeedTabPage(self.driver)

        self.seleniumdriver = SeleniumDriver(self.driver)


        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

    @pytest.mark.run(1)
    def test_3_1_1_select_venues(self):
        self.livefeedtabpage.enter_venue_name(v_n="ICA_2021")
        self.seleniumdriver.screen_shot(file="test_3_1_1_select_venue_ICA_2021")


        self.livefeedtabpage.enter_venue_name(v_n="Cambrian_P2-1x1")
        self.seleniumdriver.screen_shot(file="test_3_1_1_select_venue_Cambrian_P2_1x1")


        self.livefeedtabpage.enter_venue_name(v_n="TDK_HQ_Nihonbashi")
        self.seleniumdriver.screen_shot(file="test_3_1_1_select_venue_TDK_HQ_Nihonbashi")

        # self.seleniumdriver.pytest_screenshot()

        self.loginpage.click_sign_out()

    @pytest.mark.skip(f"This test is skipped because {reason}")
    def test_3_1_2_online_all_users(self):
        # self.seleniumdriver.pytest_screenshot()
        self.seleniumdriver.screen_shot(file="test_3_1_2_online_all_users")


    @pytest.mark.skip(f"This test is skipped because {reason}")
    def test_3_1_3_show_one_active_user(self):
        # self.seleniumdriver.pytest_screenshot()
        self.seleniumdriver.screen_shot(file="test_3_1_3_show_one_active_user")


    @pytest.mark.skip(f"This test is skipped because {reason}")
    def test_3_1_4_online_multiple_active_users_same_trajectory(self):
        self.seleniumdriver.pytest_screenshot()

    @pytest.mark.skip(f"This test is skipped because {reason}")
    def test_3_1_5_online_multiple_active_users_different_trajectory(self):
        self.seleniumdriver.pytest_screenshot()

    @pytest.mark.skip(f"This test is skipped because {reason}")
    def test_3_1_6_floor_changes(self):
        self.seleniumdriver.pytest_screenshot()

    @pytest.mark.skip(f"This test is skipped because {reason}")
    def test_3_1_7_select_group(self):
        self.seleniumdriver.pytest_screenshot()

    @pytest.mark.skip(f"This test is skipped because {reason}")
    def test_3_1_8_sorting_group(self):
        self.seleniumdriver.pytest_screenshot()

    @pytest.mark.skip(f"This test is skipped because {reason}")
    def test_3_1_9_collapse_groups(self):
        self.seleniumdriver.pytest_screenshot()

