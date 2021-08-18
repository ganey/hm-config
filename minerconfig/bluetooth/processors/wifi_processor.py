import logging
from time import sleep

import minerconfig.nmcli_custom

BROADCAST_ON_REFRESH_SECONDS = 15
BROADCAST_OFF_REFRESH_SECONDS = 5

class WifiProcessor:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def run(self):
        logging.debug("Wifi Thread Started")

        while True:
            if(self.shared_state.should_scan_wifi is True):
                self.shared_state.wifi_list_cache = minerconfig.nmcli_custom.device.wifi()
                sleep(BROADCAST_ON_REFRESH_SECONDS)
            else:
                sleep(BROADCAST_OFF_REFRESH_SECONDS)
