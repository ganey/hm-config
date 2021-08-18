from lib.cputemp.service import Service

import minerconfig.constants
from minerconfig.bluetooth.characteristics.onboarding_key_characteristic import OnboardingKeyCharacteristic
from minerconfig.bluetooth.characteristics.public_key_characteristic import PublicKeyCharacteristic
from minerconfig.bluetooth.characteristics.wifi_services_characteristic import WifiServicesCharacteristic
from minerconfig.bluetooth.characteristics.wifi_configured_services_characteristic import WifiConfiguredServicesCharacteristic
from minerconfig.bluetooth.characteristics.diagnostics_characteristic import DiagnosticsCharacteristic
from minerconfig.bluetooth.characteristics.mac_address_characteristic import MacAddressCharacteristic
from minerconfig.bluetooth.characteristics.lights_characteristic import LightsCharacteristic
from minerconfig.bluetooth.characteristics.wifi_ssid_characteristic import WifiSSIDCharacteristic
from minerconfig.bluetooth.characteristics.assert_location_characteristic import AssertLocationCharacteristic
from minerconfig.bluetooth.characteristics.add_gateway_characteristic import AddGatewayCharacteristic
from minerconfig.bluetooth.characteristics.wifi_connect_characteristic import WifiConnectCharacteristic
from minerconfig.bluetooth.characteristics.ethernet_online_characteristic import EthernetOnlineCharacteristic
from minerconfig.bluetooth.characteristics.software_version_characteristic import SoftwareVersionCharacteristic
from minerconfig.bluetooth.characteristics.wifi_remove_characteristic import WifiRemoveCharacteristic

class HeliumService(Service):

    def __init__(self, index, eth0_mac_address, onboarding_key, pub_key, firmware_version, shared_state):

        Service.__init__(self, index, minerconfig.constants.HELIUM_SERVICE_UUID, True)
        self.add_characteristic(OnboardingKeyCharacteristic(self, onboarding_key))
        self.add_characteristic(PublicKeyCharacteristic(self, pub_key))
        self.add_characteristic(WifiServicesCharacteristic(self, shared_state))
        self.add_characteristic(WifiConfiguredServicesCharacteristic(self, shared_state))
        self.add_characteristic(DiagnosticsCharacteristic(self))
        self.add_characteristic(MacAddressCharacteristic(self, eth0_mac_address))
        self.add_characteristic(LightsCharacteristic(self))
        self.add_characteristic(WifiSSIDCharacteristic(self, shared_state))
        self.add_characteristic(AssertLocationCharacteristic(self))
        self.add_characteristic(AddGatewayCharacteristic(self))
        self.add_characteristic(WifiConnectCharacteristic(self))
        self.add_characteristic(EthernetOnlineCharacteristic(self))
        self.add_characteristic(SoftwareVersionCharacteristic(self, firmware_version))
        self.add_characteristic(WifiRemoveCharacteristic(self))
