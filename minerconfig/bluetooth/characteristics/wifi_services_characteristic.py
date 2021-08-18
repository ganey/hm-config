import logging

from lib.cputemp.service import Characteristic
import minerconfig.constants

from minerconfig.bluetooth.descriptors.wifi_services_descriptor import WifiServicesDescriptor
from minerconfig.bluetooth.descriptors.opaque_structure_descriptor import OpaqueStructureDescriptor
import dbus

import lib.protos.wifi_services_pb2
from minerconfig.helpers import is_valid_ssid

class WifiServicesCharacteristic(Characteristic):

    def __init__(self, service, shared_state):
        Characteristic.__init__(
                self, minerconfig.constants.WIFI_SERVICES_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(WifiServicesDescriptor(self))
        self.add_descriptor(OpaqueStructureDescriptor(self))
        self.shared_state = shared_state

    def ReadValue(self, options):
        logging.debug('Read WiFi Services')
        known_wifi_services = lib.protos.wifi_services_pb2.wifi_services_v1()

        for network in self.shared_state.wifi_list_cache:
            ssid_str = str(network.ssid)

            if(is_valid_ssid(ssid_str)):
                ssid_unknown = ssid_str not in known_wifi_services.services
                
                if(ssid_unknown):
                    known_wifi_services.services.append(ssid_str)
                    logging.debug(ssid_str)

        value = []
        val = known_wifi_services.SerializeToString()

        for c in val:
            value.append(dbus.Byte(c))
        if("offset" in options):
            cutDownArray = value[int(options["offset"]):]
            return cutDownArray
        else:
            return value