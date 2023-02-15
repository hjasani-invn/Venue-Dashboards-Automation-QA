import unittest
unittest.TestLoader.sortTestMethodsUsing = None

from tests.home.login_tests import LoginTests

from tests.tabs.analytics.playback_tests import PlaybackTabTests
from tests.tabs.analytics.heatmap_tests import HeatmapTabTests
from tests.tabs.analytics.area_analytics_tests import AreaAnalyticsTabTests
from tests.tabs.analytics.movement_analytics_tests import MovementAnalyticsTabTests
from tests.tabs.analytics.distance_analytics_tests import DistanceAnalyticsTabTests
from tests.tabs.analytics.downloads_tests import DownloadsTabTests


tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)

tc2 = unittest.TestLoader().loadTestsFromTestCase(PlaybackTabTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(HeatmapTabTests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(AreaAnalyticsTabTests)
tc5 = unittest.TestLoader().loadTestsFromTestCase(MovementAnalyticsTabTests)
tc6 = unittest.TestLoader().loadTestsFromTestCase(DistanceAnalyticsTabTests)
tc7 = unittest.TestLoader().loadTestsFromTestCase(DownloadsTabTests)
