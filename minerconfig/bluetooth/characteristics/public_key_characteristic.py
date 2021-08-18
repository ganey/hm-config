from minerconfig.logger import logger 
import dbus

from lib.cputemp.service import Characteristic
import minerconfig.constants
from minerconfig.helpers import string_to_dbus_byte_array
from minerconfig.bluetooth.descriptors.public_key_descriptor import PublicKeyDescriptor
from minerconfig.bluetooth.descriptors.utf8_format_descriptor import UTF8FormatDescriptor

class PublicKeyCharacteristic(Characteristic):

    def __init__(self, service, pub_key):
        Characteristic.__init__(
                self, minerconfig.constants.PUBLIC_KEY_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(PublicKeyDescriptor(self))
        self.add_descriptor(UTF8FormatDescriptor(self))
        self.pub_key = pub_key

    def ReadValue(self, options):
        logger.debug("Read Public Key: %s", self.pub_key)
        return string_to_dbus_byte_array(self.pub_key)