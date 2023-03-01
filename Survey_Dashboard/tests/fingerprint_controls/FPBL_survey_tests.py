import time

import pytest

from pages.fingerprint_controls.FPBL_survey_page import FPBLSurveyPage
from pages.login_page import LoginPage
import unittest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class FPBLSurveyTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.ffblsurveypage = FPBLSurveyPage(self.driver)

    @pytest.mark.run(1)
    def test_3_1_1_login_valid(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")

    @pytest.mark.run(2)
    def test_3_2_1_FPBL_survey(self):
        self.ffblsurveypage.click_admin()
        self.ffblsurveypage.click_survey_editor()
        self.ffblsurveypage.enter_venue()
        self.ffblsurveypage.select_floor()

        self.ffblsurveypage.click_fingerprint_btn()
        self.ffblsurveypage.select_fpbl_survey(processing_mode="Survey") # Survey, Beacon Recommendation
        self.ffblsurveypage.click_reprocess()

        self.ffblsurveypage.verify_fingerprint_timestamp()
        time.sleep(10)

    @pytest.mark.run(2)
    def test_3_2_2_FPBL_beacon(self):
        self.ffblsurveypage.click_admin()
        self.ffblsurveypage.click_survey_editor()
        self.ffblsurveypage.enter_venue()
        self.ffblsurveypage.select_floor()

        "select 'Default max beacons config' checkbox"
        self.ffblsurveypage.click_fingerprint_btn()
        self.ffblsurveypage.select_fpbl_survey(processing_mode="Beacon Recommendation") # Survey, Beacon Recommendation
        self.ffblsurveypage.click_reprocess()
        self.ffblsurveypage.verify_fingerprint_timestamp()
        time.sleep(10)

        "select specific number of beacons"
        self.ffblsurveypage.checkbox(number_of_beacons_on_4th_floor=5, number_of_beacons_on_1st_floor=2)
        time.sleep(10)
