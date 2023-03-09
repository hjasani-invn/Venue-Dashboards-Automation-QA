import time

import pytest
from pages.home.login_page import LoginPage
from pages.survey_viewer.venue_display_page import DisplayVenuePage
import unittest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class VenueDisplayTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.login_page = LoginPage(self.driver)
        self.display_page = DisplayVenuePage(self.driver)
        self.login_page.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        
    @pytest.mark.run(5)
    def test_3_2_1_venue_display(self):
        self.display_page.click_dashboard()
        self.display_page.click_survey_viewer()
        self.display_page.click_select_venue()

        # Test CES
        self.display_page.enter_venue_search("CES")
        self.display_page.click_search_result("CES")
        self.display_page.zoom_in_3x()
        self.display_page.zoom_out_3x()

        self.display_page.click_select_venue()
        self.display_page.clear_search_box()

        # Test ICA Calgary
        self.display_page.enter_venue_search("ICA_2021")
        self.display_page.click_search_result("ICA_2021")
        self.display_page.zoom_in_3x()
        self.display_page.zoom_out_3x()

        self.display_page.click_select_venue()
        self.display_page.clear_search_box()

        # Test TDK_HQ_Nihonbashi
        self.display_page.enter_venue_search("TDK_HQ_Nihonbashi")
        self.display_page.click_search_result("TDK_HQ_Nihonbashi")
        self.display_page.zoom_in_3x()
        self.display_page.zoom_out_3x()
        
        self.login_page.sign_out()
    
    # @pytest.mark.run(6)
    @pytest.mark.skip
    def test_3_2_2_map_scrolling_venue_refresh(self):
        self.display_page.click_dashboard()
        self.display_page.click_survey_viewer()
        self.display_page.click_select_venue()
        self.display_page.enter_venue_search("ICA_2021")
        self.display_page.click_search_result("ICA_2021")
        self.display_page.pan_up()
        self.display_page.pan_down()
        self.display_page.pan_left()
        self.display_page.pan_right()
        self.login_page.sign_out()
        time.sleep(5)

    # @pytest.mark.skip
    @pytest.mark.run(7)
    def test_3_2_3_map_views(self):
        self.display_page.click_dashboard()
        self.display_page.click_survey_viewer()
        self.display_page.click_select_venue()
        self.display_page.enter_venue_search("ICA_2021")
        self.display_page.click_search_result("ICA_2021")
        self.display_page.select_satellite_maps()
        self.display_page.select_satellite_maps()
        self.display_page.select_street_maps()
        self.display_page.select_none()
        self.login_page.sign_out()

    # @pytest.mark.skip
    @pytest.mark.run(8)
    def test_3_2_4_map_overlays(self):
        self.display_page.click_dashboard()
        self.display_page.click_survey_viewer()
        self.display_page.click_select_venue()
        self.display_page.enter_venue_search("ICA")
        self.display_page.click_search_result("ICA")
        self.display_page.select_none()
        self.display_page.select_none()
        self.display_page.zoom_in_3x()
        self.display_page.select_mag_wifi()
        self.display_page.select_mag_pos()
        self.display_page.select_coverage()
        self.login_page.sign_out()

    # @pytest.mark.skip
    @pytest.mark.run(9)
    def test_3_3_1_zoom_levels(self):
        self.display_page.click_admin()
        self.display_page.click_survey_editor()
        self.display_page.click_select_venue()

        self.display_page.enter_venue_search("CES")
        self.display_page.click_search_result("CES")
        self.display_page.zoom_in_3x()
        self.display_page.zoom_out_3x()

        self.display_page.click_select_venue()
        self.display_page.clear_search_box()

        # Test ICA Calgary
        self.display_page.enter_venue_search("ICA_2021")
        self.display_page.click_search_result("ICA_2021")
        self.display_page.zoom_in_3x()
        self.display_page.zoom_out_3x()

        self.display_page.click_select_venue()
        self.display_page.clear_search_box()

        # Test TDK_HQ_Nihonbashi
        self.display_page.enter_venue_search("TDK_HQ_Nihonbashi")
        self.display_page.click_search_result("TDK_HQ_Nihonbashi")
        self.display_page.zoom_in_3x()
        self.display_page.zoom_out_3x()
        self.login_page.sign_out()

    @pytest.mark.skip
    # @pytest.mark.run(6)
    def test_3_3_2_map_scrolling(self):
        pass

    
    # @pytest.mark.skip
    @pytest.mark.run(10)
    def test_3_3_3_map_views(self):
        self.display_page.click_admin()
        self.display_page.click_survey_editor()
        self.display_page.click_select_venue()
        self.display_page.enter_venue_search("ICA_2021")
        self.display_page.click_search_result("ICA_2021")
        self.display_page.select_satellite_maps()
        self.display_page.select_satellite_maps()
        self.display_page.select_street_maps()
        self.display_page.select_none()
        self.login_page.sign_out()

    
    @pytest.mark.run(11)
    def test_3_3_4_map_overlays(self):
        self.display_page.click_admin()
        self.display_page.click_survey_editor()
        self.display_page.click_select_venue()
        self.display_page.enter_venue_search("ICA")
        self.display_page.click_search_result("ICA")
        self.display_page.select_none()
        self.display_page.select_none()
        self.display_page.zoom_in_3x()
        self.display_page.select_mag_wifi()
        self.display_page.select_mag_pos()
        self.display_page.select_coverage()
        self.login_page.sign_out()
    
    # NOTE: tests 3.5 and 3.6 are route drawing and require manual intervention

    # @pytest.mark.skip
    @pytest.mark.run(12)
    def test_3_6_1_normal_route_length(self):
        self.display_page.click_admin()
        self.display_page.click_survey_editor()
        self.display_page.click_select_venue()
        self.display_page.enter_venue_search("ICA")
        self.display_page.click_search_result("ICA")
        self.display_page.select_access_point_list()
        self.display_page.delete_all_sources()
        self.display_page.cancel_btn()
        self.login_page.sign_out()

    
