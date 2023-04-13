import unittest
unittest.TestLoader.sortTestMethodsUsing = None

from tests.home.login_tests import LoginTests
from tests.tabs.livefeed_tests import LiveFeedTabTests

from tests.tabs.analytics.playback_tests import PlaybackTabTests
from tests.tabs.analytics.heatmap_tests import HeatmapTabTests
from tests.tabs.analytics.area_analytics_tests import AreaAnalyticsTabTests
from tests.tabs.analytics.movement_analytics_tests import MovementAnalyticsTabTests
from tests.tabs.analytics.distance_analytics_tests import DistanceAnalyticsTabTests
from tests.tabs.analytics.downloads_tests import DownloadsTabTests


tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LiveFeedTabTests)

tc3 = unittest.TestLoader().loadTestsFromTestCase(PlaybackTabTests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(HeatmapTabTests)
tc5 = unittest.TestLoader().loadTestsFromTestCase(AreaAnalyticsTabTests)
tc6 = unittest.TestLoader().loadTestsFromTestCase(MovementAnalyticsTabTests)
tc7 = unittest.TestLoader().loadTestsFromTestCase(DistanceAnalyticsTabTests)
tc8 = unittest.TestLoader().loadTestsFromTestCase(DownloadsTabTests)
