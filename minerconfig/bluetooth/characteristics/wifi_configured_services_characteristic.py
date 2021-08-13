import logging

from lib.cputemp.service import Characteristic
import minerconfig.constants

from minerconfig.bluetooth.descriptors.wifi_configured_services_descriptor import WifiConfiguredServicesDescriptor
from minerconfig.bluetooth.descriptors.opaque_structure_descriptor import OpaqueStructureDescriptor
from minerconfig.helpers import string_to_dbus_byte_array
from minerconfig.helpers import is_valid_ssid

import lib.protos.wifi_services_pb2

class WifiConfiguredServicesCharacteristic(Characteristic):

    global wifiCache

    def __init__(self, service):
        Characteristic.__init__(
                self, minerconfig.constants.WIFI_CONFIGURED_SERVICES_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(WifiConfiguredServicesDescriptor(self))
        self.add_descriptor(OpaqueStructureDescriptor(self))
        self.wifi_list_cache = []

    def update_wifi_list_cache(self, wifi_list_cache):
        self.wifi_list_cache = wifi_list_cache

    def ReadValue(self, options):
        logging.debug('Read WiFi CONFIGURED Services')
        configured_wifi_services = lib.protos.wifi_services_pb2.wifi_services_v1()

        for network in self.wifi_list_cache:
            ssid_str = str(network.ssid)

            if(is_valid_ssid(ssid_str)):
                if(network.in_use):
                    configured_wifi_services.services.append(ssid_str)

        return string_to_dbus_byte_array(configured_wifi_services.SerializeToString())
