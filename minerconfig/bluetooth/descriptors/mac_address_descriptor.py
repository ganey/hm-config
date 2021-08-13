
from lib.cputemp.service import Descriptor
import minerconfig.constants
from minerconfig.helpers import string_to_dbus_byte_array

class MacAddressDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, minerconfig.constants.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        return string_to_dbus_byte_array(minerconfig.constants.MAC_ADDRESS_LABEL)
