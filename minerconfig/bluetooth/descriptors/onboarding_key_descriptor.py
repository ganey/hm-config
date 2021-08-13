from lib.cputemp.service import Descriptor
import minerconfig.constants
from minerconfig.helpers import string_to_dbus_byte_array

class OnboardingKeyDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, minerconfig.constants.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)
        self.onboarding_key_label = minerconfig.constants.ONBOARDING_KEY_LABEL

    def ReadValue(self, options):
        return string_to_dbus_byte_array(self.onboarding_key_label)
