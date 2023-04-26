import unittest

import pytest

from base.selenium_driver import SeleniumDriver
from pages.user_management.groups_page import GroupsPage
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class GroupsTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.grouppage = GroupsPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)

    @pytest.mark.order(18)
    def test_3_3_4_delete_group_if_available(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.grouppage.delete_group("abc")
        try:
            result_1 = self.grouppage.verify_grp_deleted()
            assert result_1 == "Group deleted"
        except:
            print("Group with name 'abc' is not available ")
        self.seleniumdriver.screen_shot(file="test_3_3_4_delete_group_if_available")

    @pytest.mark.order(19)
    def test_3_3_1_adding_groups(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.grouppage.all_grp("abc", "automation test group - this group will be deleted upon complete suite execution", "InvenSense-PowerUserGroup","Admin-InvenSense-PowerUserGroup")
        result_1 = self.grouppage.verify_grp_created()
        assert result_1 == "Group created"
        self.seleniumdriver.screen_shot(file="test_3_3_1_adding_groups")


    @pytest.mark.order(20)
    def test_3_3_3_edit_group(self):
        self.grouppage.edit_group("abc")
        # result_1 = self.grouppage.verify_grp_updated()
        # assert result_1 == "Group updated"
        self.seleniumdriver.screen_shot(file="test_3_3_3_edit_group")

    @pytest.mark.order(21)
    def test_3_3_4_delete_group(self):
        self.grouppage.delete_group("abc")
        result_1 = self.grouppage.verify_grp_deleted()
        assert result_1 == "Group deleted"
        self.seleniumdriver.screen_shot(file="test_3_3_4_delete_group")

    @pytest.mark.order(22)
    def test_3_3_5_download_all_groups_csv(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.grouppage.download_grp_csv()
        # result_1 = self.grouppage.verify_grp_csv_download()
        # r_1 = self.grouppage.file_data_empty()
        # assert r_1 == r_1
        self.grouppage.delete_file()
        self.seleniumdriver.screen_shot(file="test_3_3_5_download_all_groups_csv")
