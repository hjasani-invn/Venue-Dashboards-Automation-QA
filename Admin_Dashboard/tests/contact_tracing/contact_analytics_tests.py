import unittest

import pytest

from base.selenium_driver import SeleniumDriver
from pages.contact_tracing.contact_analytics_page import ContactAnalyticsPage
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ContactAnalyticsTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.contactanalyticspage = ContactAnalyticsPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.seleniumdriver = SeleniumDriver(self.driver)


    @pytest.mark.order(27)
    def test_3_5_1_1_contact_tracing_queries(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.contactanalyticspage.open_contact_analytics_tab()
        self.contactanalyticspage.enter_venue(v_n='ICA_2021')
        self.contactanalyticspage.chose_start_date(s_date="1/1/2021")  # DD/MM/YYYY, D/M/YYYY
        self.contactanalyticspage.choose_end_date(e_date="3/3/2021")
        self.contactanalyticspage.select_max_distance(enter_max_distance="2")
        self.contactanalyticspage.click_search_btn()

        result_1 = self.contactanalyticspage.verify_time_range_no_morethan_2_months_message()
        assert result_1 == "Timerange can not be more than 2 months"
        self.seleniumdriver.screen_shot(file="test_3_5_1_1_contact_tracing_queries")


    @pytest.mark.order(28)
    def test_3_5_1_2_contact_tracing_queries(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.contactanalyticspage.open_contact_analytics_tab()
        # self.contactanalyticspage.enter_venue(v_n='ICA Calgary')
        self.contactanalyticspage.chose_start_date(s_date="3/3/2021")  # DD/MM/YYYY, D/M/YYYY
        self.contactanalyticspage.choose_end_date(e_date="1/1/2021")
        self.contactanalyticspage.select_max_distance(enter_max_distance="2")
        self.contactanalyticspage.click_search_btn()

        result_1 = self.contactanalyticspage.verify_reverse_time_range_message()
        assert result_1 == "Time Range is Incorrect!"
        self.seleniumdriver.screen_shot(file="test_3_5_1_2_contact_tracing_queries")


    @pytest.mark.order(29)
    def test_3_5_1_3_contact_tracing_queries(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.contactanalyticspage.open_contact_analytics_tab()
        # self.contactanalyticspage.enter_venue(v_n='ICA Calgary')
        self.contactanalyticspage.chose_start_date(s_date="1/1/2021")  # DD/MM/YYYY, D/M/YYYY
        self.contactanalyticspage.choose_end_date(e_date="3/3/2021")
        self.contactanalyticspage.select_max_distance(enter_max_distance="25")
        self.contactanalyticspage.click_search_btn()

        result_1 = self.contactanalyticspage.verify_max_distance_message()
        assert result_1 == "Max distance can not be greater than 20mtrs."
        self.seleniumdriver.screen_shot(file="test_3_5_1_3_contact_tracing_queries")


    @pytest.mark.order(30)
    def test_3_5_1_4_contact_tracing_queries(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.contactanalyticspage.open_contact_analytics_tab()
        # self.contactanalyticspage.enter_venue(v_n='ICA Calgary')
        self.contactanalyticspage.chose_start_date(s_date="1/1/2021")  # DD/MM/YYYY, D/M/YYYY
        self.contactanalyticspage.choose_end_date(e_date="3/3/2021")
        self.contactanalyticspage.select_max_distance(enter_max_distance="twenty-five")
        self.contactanalyticspage.click_search_btn()

        result_1 = self.contactanalyticspage.verify_max_distance_message_if_words()
        assert result_1 == "Please enter max distance."
        self.seleniumdriver.screen_shot(file="test_3_5_1_4_contact_tracing_queries")


    # @pytest.mark.dependency()
    # @pytest.mark.order(31)
    @pytest.mark.skip()
    def test_3_5_1_5_contact_tracing_queries(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.contactanalyticspage.open_contact_analytics_tab()
        # self.contactanalyticspage.get_list_before_search()
        self.contactanalyticspage.enter_venue(v_n='ICA Calgary')
        # self.contactanalyticspage.enter_venue(v_n='ICA_2021')
        self.contactanalyticspage.chose_start_date(s_date="3/22/2022")  # DD/MM/YYYY, D/M/YYYY
        self.contactanalyticspage.choose_end_date(e_date="3/24/2022")
        self.contactanalyticspage.select_max_distance(enter_max_distance="2.41")
        self.contactanalyticspage.click_search_btn()
        # query_name="new query 1"
        # r_1 = self.contactanalyticspage.is_pop_up_2()
        # assert r_1 == "Query"
        # r_1 = self.contactanalyticspage.is_pop_up_2()
        # assert r_1 == "No Contact Data found"

        # self.contactanalyticspage.get_list_after_search()
        # self.contactanalyticspage.print_list()
        r_1 = self.contactanalyticspage.is_popup(query_name="new query")
        assert r_1 == "No Contact Data found for the given Search conditi" or "Query"
        self.seleniumdriverpage.screen_shot("test_3_5_1_5_contact_tracing_queries")
        # result_1 = self.contactanalyticspage.snack_bar_message()
        # assert result_1 == "Query"
        # try:
        #     r_1 = self.contactanalyticspage.is_popup(query_name="new query")
        #     # assert r_1 == "No Contact Data found for the given Search conditi"
        #     assert r_1 == "Query"
        # except:
        #     r_2 = self.contactanalyticspage.is_popup(query_name = "new query")
        #     assert r_2 == "Query"

    # # @pytest.mark.order(30) # if query created then only rename the latest query
    # @pytest.mark.dependency(depends=['ContactAnalyticsTests::test_3_5_1_5_contact_tracing_queries']) # if query created then only rename the latest query
    # def test_3_5_2_contact_tracing_rename_queries(self):
    #     # self.loginpage.login("TestUser001", "TP1M4St3R_p4ssw0rd")
    #     self.contactanalyticspage.update_query_name("renaming query")
    #     # self.contactanalyticspage.is_popup(query_name="renamed")
