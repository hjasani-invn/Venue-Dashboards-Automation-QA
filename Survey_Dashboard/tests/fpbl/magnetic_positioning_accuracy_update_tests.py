import time

import pytest

from pages.fpbl.magnetic_positioning_accuracy_update_page import MagneticPositioningAccuracyUpdatePage
from pages.home.login_page import LoginPage
import unittest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class MagneticPositioningAccuracyUpdateTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.magnetic_positioning_accuracy_update_page = MagneticPositioningAccuracyUpdatePage(self.driver)

    # @pytest.mark.run(1)
    # def test_3_8_login_valid(self):
    #     self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

    # @pytest.mark.run(2)
    def test_3_8_1_FPBL_magnetic_positioning_accuracy_update(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.magnetic_positioning_accuracy_update_page.click_admin()
        self.magnetic_positioning_accuracy_update_page.click_survey_editor()
        self.magnetic_positioning_accuracy_update_page.enter_venue()
        self.magnetic_positioning_accuracy_update_page.select_floor()

        time.sleep(10)