import unittest

unittest.TestLoader.sortTestMethodsUsing = None

from tests.home.login_tests import LoginTests
from tests.survey_viewer_editor.survey_viewer_editor_test import VenueDisplayTest

from tests.access_points.source_white_ignore_list_tests import SourceWhiteIgnoreListTests
from tests.access_points.move_entries_tests import MoveEntriesTests
from tests.fingerprint_controls.FPBL_survey_tests import FPBLSurveyTests
from tests.route_drawing.route_drawing_tests import RouteDrawingTests
from tests.route_upload_download_modifications.route_upload_download_modifications_tests import RouteUploadDownloadTest
from tests.beacon_entry.adding_beacons_tests import AddBeaconTests
from tests.beacon_entry.editing_beacons_tests import EditBeaconTests
from tests.beacon_entry.deleting_beacons_tests import DeleteBeaconTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(VenueDisplayTest)

tc3 = unittest.TestLoader().loadTestsFromTestCase(SourceWhiteIgnoreListTests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(MoveEntriesTests)
tc5 = unittest.TestLoader().loadTestsFromTestCase(FPBLSurveyTests)
tc6 = unittest.TestLoader().loadTestsFromTestCase(RouteDrawingTests)
tc7 = unittest.TestLoader().loadTestsFromTestCase(RouteUploadDownloadTest)
tc8 = unittest.TestLoader().loadTestsFromTestCase(AddBeaconTests)
tc9 = unittest.TestLoader().loadTestsFromTestCase(EditBeaconTests)
tc10 = unittest.TestLoader().loadTestsFromTestCase(DeleteBeaconTests)