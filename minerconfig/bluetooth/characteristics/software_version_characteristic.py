import logging

from lib.cputemp.service import Characteristic
import minerconfig.constants

from minerconfig.bluetooth.descriptors.wifi_configured_services_descriptor import WifiConfiguredServicesDescriptor
from minerconfig.bluetooth.descriptors.opaque_structure_descriptor import OpaqueStructureDescriptor
from minerconfig.helpers import string_to_dbus_byte_array
from minerconfig.helpers import is_valid_ssid


class SoftwareVersionCharacteristic(Characteristic):
    def __init__(self, service, firmware_version):
        Characteristic.__init__(
                self, minerconfig.constants.SOFTWARE_VERSION_CHARACTERISTIC_UUID,
                ["read"], service)
        self.firmware_version = firmware_version

    def ReadValue(self, options):
        logging.debug('Read Firmware')
        return string_to_dbus_byte_array(self.firmware_version)
