import unittest

import pytest

from base.selenium_driver import SeleniumDriver
from pages.user_guide_sdk.key_list_page import KeyListPage
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class KeyListTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.keylistpage = KeyListPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)

    @pytest.mark.order(24)
    def test_3_4_2_open_key_list(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.keylistpage.open_key_list()

        result_1 = self.keylistpage.verify_keys_opens()
        assert result_1 == "Keys"

        self.seleniumdriver.screen_shot(file="test_3_4_2_open_key_list")
