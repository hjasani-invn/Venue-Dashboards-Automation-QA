import unittest
unittest.TestLoader.sortTestMethodsUsing = None

from tests.home.login_tests import LoginTests
from tests.survey_viewer.venue_display_test import VenueDisplayTest

from tests.access_points.source_white_ignore_list_tests import SourceWhiteIgnoreListTests
from tests.access_points.move_entries_tests import MoveEntriesTests


tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(VenueDisplayTest)

tc3 = unittest.TestLoader().loadTestsFromTestCase(SourceWhiteIgnoreListTests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(MoveEntriesTests)