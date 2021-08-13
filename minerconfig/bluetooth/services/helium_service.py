from lib.cputemp.service import Service

import minerconfig.constants
from minerconfig.bluetooth.characteristics.onboarding_key_characteristic import OnboardingKeyCharacteristic

class HeliumService(Service):

    def __init__(self, index, onboarding_key):

        Service.__init__(self, index, minerconfig.constants.HELIUM_SERVICE_UUID, True)
        self.add_characteristic(OnboardingKeyCharacteristic(self, onboarding_key))
#         self.add_characteristic(PublicKeyCharacteristic(self))
#         self.add_characteristic(WiFiServicesCharacteristic(self))
#         self.add_characteristic(WiFiConfiguredServicesCharacteristic(self))
#         self.add_characteristic(DiagnosticsCharacteristic(self))
#         self.add_characteristic(MacAddressCharacteristic(self))
#         self.add_characteristic(LightsCharacteristic(self))
#         self.add_characteristic(WiFiSSIDCharacteristic(self))
#         self.add_characteristic(AssertLocationCharacteristic(self))
#         self.add_characteristic(AddGatewayCharacteristic(self))
#         self.add_characteristic(WiFiConnectCharacteristic(self))
#         self.add_characteristic(EthernetOnlineCharacteristic(self))
#         self.add_characteristic(SoftwareVersionCharacteristic(self))
#         self.add_characteristic(WiFiRemoveCharacteristic(self))
