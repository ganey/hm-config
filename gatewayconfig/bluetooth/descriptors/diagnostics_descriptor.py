from lib.cputemp.service import Descriptor
from gatewayconfig.helpers import string_to_dbus_encoded_byte_array
import gatewayconfig.constants as constants


class DiagnosticsDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, constants.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        return string_to_dbus_encoded_byte_array(constants.DIAGNOSTICS_LABEL)
