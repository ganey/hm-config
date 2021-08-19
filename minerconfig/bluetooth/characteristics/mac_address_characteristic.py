from minerconfig.logger import logger

from lib.cputemp.service import Characteristic
import minerconfig.constants
from minerconfig.helpers import string_to_dbus_byte_array
from minerconfig.bluetooth.descriptors.mac_address_descriptor import MacAddressDescriptor
from minerconfig.bluetooth.descriptors.utf8_format_descriptor import UTF8FormatDescriptor

class MacAddressCharacteristic(Characteristic):

    def __init__(self, service, eth0_mac_address):
        Characteristic.__init__(
                self, minerconfig.constants.MAC_ADDRESS_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(MacAddressDescriptor(self))
        self.add_descriptor(UTF8FormatDescriptor(self))
        self.eth0_mac_address = eth0_mac_address.replace(':', '')

    def ReadValue(self, options):
        logger.debug('Read Mac Address')
        return string_to_dbus_byte_array(self.eth0_mac_address)

