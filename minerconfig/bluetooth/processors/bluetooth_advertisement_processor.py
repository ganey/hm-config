import logging
from time import sleep

from lib.cputemp.bletools import BleTools

from minerconfig.bluetooth.advertisements.connection_advertisement import ConnectionAdvertisement

ADVERTISEMENT_TYPE = 'peripheral'
ADVERTISEMENT_INDEX = 0
ADVERTISEMENT_SECONDS = 300

class BluetoothAdvertisementProcessor:
    def __init__(self, eth0_mac_address, variant):
        self.should_advertise = True
        self.connection_advertisement = ConnectionAdvertisement(ADVERTISEMENT_INDEX, eth0_mac_address, ADVERTISEMENT_TYPE, variant)

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