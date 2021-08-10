import logging
from time import sleep

from lib.cputemp.bletools import BleTools

from src.bluetooth.connection_advertisement import ConnectionAdvertisement

ADVERTISEMENT_SECONDS = 300

class AdvertisementProcessor:
    def __init__(self, variant):
        self.should_advertise = True
        self.connection_advertisement = ConnectionAdvertisement(0, variant)

    def run(self):
        logging.debug("Advertising Bluetooth")
        while True:
            if(self.should_advertise is True):
                self.should_advertise = False
                # scanWifi = True
                try:
                    BleTools.disconnect_connections()
                except TypeError:
                    # Most Likely Already Disconnected
                    pass
                self.connection_advertisement.register()
                # advertisementLED = True
                sleep(ADVERTISEMENT_SECONDS)
                logging.debug("Stopping Bluetooth advertisement")
                self.connection_advertisement.unregister()
                # advertisementLED = False
                # scanWifi = False
            else:
                sleep(5)