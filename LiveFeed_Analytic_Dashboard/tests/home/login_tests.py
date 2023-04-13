import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver
from pages.home.login_page import LoginPage
import unittest
from tests import conftest
from pytest_html_reporter import attach



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)


    @pytest.mark.run(1)
    def test_3_1_1_login_nominal(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        # self.seleniumdriver.pytest_screenshot()

        result_1 = self.loginpage.verify_signin()
        assert result_1 == True
        self.seleniumdriver.screen_shot(file="test_3_1_1_login_nominal")
        self.loginpage.click_sign_out()


    @pytest.mark.run(2)
    def test_3_1_2_login_bad_password(self):
        self.loginpage.login("AutomationTestUser001", "justWrongPassword")
        # self.seleniumdriver.pytest_screenshot()
        result_1 = self.loginpage.verify_login_failed()
        assert result_1 == "Wrong username or password. Please try again."
        self.seleniumdriver.screen_shot(file="test_3_1_2_login_bad_password")

    @pytest.mark.run(3)
    def test_3_1_3_login_bad_user(self):
        self.loginpage.login("BadUser@gmail.com", "BadPassword")
        # data = self.driver.get_screenshot_as_png()
        # # print(f"this is ss: \n {data}")
        # shot = self.seleniumdriver.screen_shot(file="test_3_1_3_login_bad_user_1.png")
        # attach(data=data)
        # # attach(data=self.seleniumdriver.screen_shot(file="test_3_1_3_login_bad_user_1.png"))
        # self.seleniumdriver.pytest_screenshot()
        result_1 = self.loginpage.verify_login_failed()
        assert result_1 == "Wrong username or password. Please try again."  # True Message
        self.seleniumdriver.screen_shot(file="test_3_1_3_login_bad_user_1.png")



# ff = LoginTests()
# ff.test_valid_login()
