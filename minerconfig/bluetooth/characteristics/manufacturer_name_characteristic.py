import logging

from lib.cputemp.service import Characteristic
import minerconfig.constants
from minerconfig.helpers import string_to_dbus_byte_array

MANUFACTURER_NAME = "Nebra LTD."

class ManufacturerNameCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
                self, minerconfig.constants.MANUFACTURER_NAME_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        logging.debug('Read Manufacturer')
        return string_to_dbus_byte_array(MANUFACTURER_NAME)