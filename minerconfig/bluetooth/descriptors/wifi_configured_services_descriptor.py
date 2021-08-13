from lib.cputemp.service import Descriptor
import minerconfig.constants
from minerconfig.helpers import string_to_dbus_byte_array

class WifiConfiguredServicesDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, minerconfig.constants.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        value = []
        return string_to_dbus_byte_array(minerconfig.constants.WIFI_CONFIGURED_SERVICES_LABEL)
