import unittest

import pytest

from base.selenium_driver import SeleniumDriver
from pages.user_guide_sdk.venue_list_page import VenueListPage
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class VenueListTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.venuelistpage = VenueListPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)

    @pytest.mark.order(23)
    def test_3_4_1_open_venue_list(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.venuelistpage.open_venue_list()

        result_1 = self.venuelistpage.verify_list_opens()
        assert result_1 == "Venues"

        self.seleniumdriver.screen_shot(file="test_3_4_1_open_venue_list")
