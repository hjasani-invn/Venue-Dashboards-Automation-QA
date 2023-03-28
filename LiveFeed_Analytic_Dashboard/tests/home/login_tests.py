import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
from tests import conftest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.teststatus = TestStatus(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)


    @pytest.mark.run(1)
    def test_3_1_1_login_nominal(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        result_1 = self.loginpage.verify_signin()
        assert result_1 == True
        self.seleniumdriver.screen_shot(file="test_3_1_1_login_nominal")
        self.loginpage.click_sign_out()


    @pytest.mark.run(2)
    def test_3_1_2_login_bad_password(self):
        self.loginpage.login("AutomationTestUser001", "justWrongPassword")
        result_1 = self.loginpage.verify_login_failed()
        assert result_1 == "Wrong username or password. Please try again."
        self.seleniumdriver.screen_shot(file="test_3_1_2_login_bad_password")


    @pytest.mark.run(3)
    def test_3_1_3_login_bad_user(self):
        self.loginpage.login("BadUser@gmail.com", "BadPassword")
        result_1 = self.loginpage.verify_login_failed()
        assert result_1 == "Wrong username or password. Please try again."
        self.seleniumdriver.screen_shot(file="test_3_1_3_login_bad_user")


# ff = LoginTests()
# ff.test_valid_login()
