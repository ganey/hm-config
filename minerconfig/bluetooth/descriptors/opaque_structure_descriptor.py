from lib.cputemp.service import Descriptor
import minerconfig.constants
from minerconfig.helpers import string_to_dbus_byte_array
import dbus

class OpaqueStructureDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, minerconfig.constants.PRESENTATION_FORMAT_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        value = []
        value.append(dbus.Byte(0x1B))
        value.append(dbus.Byte(0x00))
        value.append(dbus.Byte(0x00))
        value.append(dbus.Byte(0x00))
        value.append(dbus.Byte(0x01))
        value.append(dbus.Byte(0x00))
        value.append(dbus.Byte(0x00))

        return value