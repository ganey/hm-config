import logging
import os

from lib.cputemp.service import Characteristic
import minerconfig.constants
from minerconfig.helpers import string_to_dbus_byte_array

from minerconfig.bluetooth.descriptors.lights_descriptor import LightsDescriptor
from minerconfig.bluetooth.descriptors.utf8_format_descriptor import UTF8FormatDescriptor

DEFAULT_LIGHTS_VALUE = 'false'

class LightsCharacteristic(Characteristic):

    def __init__(self, service):
        Characteristic.__init__(
                self, minerconfig.constants.LIGHTS_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(LightsDescriptor(self))
        self.add_descriptor(UTF8FormatDescriptor(self))

    def ReadValue(self, options):
        logging.debug('Read Lights')
        return string_to_dbus_byte_array(DEFAULT_LIGHTS_VALUE)