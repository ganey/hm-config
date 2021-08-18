from unittest import TestCase

from minerconfig.minerconfig_shared_state import MinerconfigSharedState

class TestMinerconfigSha(TestCase):

    def test_init(self):
        shared_state = MinerconfigSharedState()

        self.assertEqual(shared_state.wifi_list_cache, [])
        self.assertEqual(shared_state.should_scan_wifi, False)
        self.assertEqual(shared_state.should_advertise_bluetooth, True)
        self.assertEqual(shared_state.is_advertising_bluetooth, False)
        self.assertEqual(shared_state.are_diagnostics_ok, False)