import pytest

from base.selenium_driver import SeleniumDriver
from pages.home.login_page import LoginPage
from pages.route_upload_download_modifications.route_upload_download_modifications_page import RouteUploadDownloadPage
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RouteUploadDownloadTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.route_upload_download = RouteUploadDownloadPage(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)

    @pytest.mark.skip("All Route upload, drawing, modification Tests needs to perform manually")
    def test_3_5_route_upload_download_modification(self):
        self.seleniumdriver.screen_shot(file="test_3_5_route_upload_download_modification")
        pass
