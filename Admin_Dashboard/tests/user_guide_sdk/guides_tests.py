import unittest

import pytest

from base.selenium_driver import SeleniumDriver
from pages.user_guide_sdk.guides_page import GuidesPage
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class GuideListTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.guidepage = GuidesPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)


    @pytest.mark.order(25)
    def test_3_4_3_download_user_guides(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.guidepage.open_guide()

    @pytest.mark.order(26)
    def test_3_4_3_1_open_guides_in_toggle_view_mode(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        print("open guides from toggle view mode - that is double clicks")
        self.guidepage.double_click_pdf_file_thubmnail()
        self.seleniumdriver.screen_shot(file="test_3_4_3_and_3_4_3_1_open_guides_all_together")


