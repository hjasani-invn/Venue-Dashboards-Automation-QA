import unittest

import pytest

from base.selenium_driver import SeleniumDriver
from pages.user_management.user_home_page import UserHomePage
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class UserHomeTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.userhomepage = UserHomePage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)

    @pytest.mark.order(13)
    def test_3_2_4_bulk_user_csv_download(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.userhomepage.download_bulk_csv_btn()
        # self.userhomepage.verify_download()

    @pytest.mark.order(14)
    def test_3_2_6_edit_user(self):
        self.userhomepage.filter_grp("Automation_Test_Group")
        self.userhomepage.edit_user(first_name_new="Demo_1")
        # result_1 = self.userhomepage.verify_rename()
        # assert result_1 == "Demo_1"

    @pytest.mark.order(15)
    def test_3_2_6_1_edit_user_unselect_grp(self):
        self.userhomepage.filter_grp("Automation_Test_Group")
        self.userhomepage.edit_user_remove_grp_name()

    @pytest.mark.order(16)
    def test_3_2_6_2_edit_user_select_multiple_grp(self):
        # self.userhomepage.filter_grp("Automation_Test_Group")
        self.userhomepage.select_multiple_grps()

    # this test case we are executing first of every iteration to make environment clean
    @pytest.mark.order(17)
    def test_3_2_7_delete_user(self):
        # self.userhomepage.delete_user()
        self.userhomepage.del_user_new()
        # result_1 = self.userhomepage.verify_deletes()
        # # result_1 = self.userhomepage.del_user_new()
        # assert result_1 == "deleted!"
        self.seleniumdriver.screen_shot(file="test_3_2_7_delete_user")