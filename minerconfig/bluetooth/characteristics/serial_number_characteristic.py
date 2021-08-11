import logging

from lib.cputemp.service import Characteristic
import minerconfig.constants
from minerconfig.helpers import string_to_dbus_byte_array

class SerialNumberCharacteristic(Characteristic):

    def __init__(self, service):
        Characteristic.__init__(
                self, minerconfig.constants.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

        self.eth_mac_address = open(minerconfig.constants.ETH0_MAC_ADDRESS_PATH) \
            .readline() \
            .strip() \
            .replace(":", "")

    def ReadValue(self, options):
        logging.debug('Read Serial Number')
        return string_to_dbus_byte_array(self.eth_mac_address)
