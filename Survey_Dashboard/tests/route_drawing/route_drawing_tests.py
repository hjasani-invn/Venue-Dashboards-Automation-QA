import pytest

from base.selenium_driver import SeleniumDriver
from pages.home.login_page import LoginPage
from pages.route_drawing.route_drawing_page import RouteDrawingPage
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RouteDrawingTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.route_drawing = RouteDrawingPage(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)

    @pytest.mark.skip("All Route Drawing Tests needs to perform manually")
    def test_3_4_route_drawing(self):
        self.seleniumdriver.screen_shot(file="test_3_4_route_drawing")
        pass
