import logging
import dbus

from lib.cputemp.service import Characteristic
import minerconfig.constants
from minerconfig.helpers import string_to_dbus_byte_array
from minerconfig.bluetooth.descriptors.onboarding_key_descriptor import OnboardingKeyDescriptor


class OnboardingKeyCharacteristic(Characteristic):
    def __init__(self, service, onboarding_key):
        Characteristic.__init__(
                self, minerconfig.constants.ONBOARDING_KEY_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(OnboardingKeyDescriptor(self))
        # self.add_descriptor(utf8Format(self))
        self.onboarding_key = onboarding_key

    def ReadValue(self, options):
        logging.debug('Read Onboarding Key')
        return string_to_dbus_byte_array(self.onboarding_key)
