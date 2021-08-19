from minerconfig.logger import logger

from lib.cputemp.service import Characteristic
import minerconfig.constants

from minerconfig.bluetooth.descriptors.wifi_remove_descriptor import WifiRemoveDescriptor
from minerconfig.bluetooth.descriptors.opaque_structure_descriptor import OpaqueStructureDescriptor

import lib.protos.wifi_remove_pb2 as wifi_remove_pb2
import nmcli_custom
from minerconfig.helpers import string_to_dbus_byte_array

class WifiRemoveCharacteristic(Characteristic):

    def __init__(self, service):
        self.notifying = False
        Characteristic.__init__(
                self, minerconfig.constants.WIFI_REMOVE_CHARACTERISTIC_UUID,
                ["read", "write", "notify"], service)
        self.add_descriptor(WifiRemoveDescriptor(self))
        self.add_descriptor(OpaqueStructureDescriptor(self))
        self.wifi_status = "False"

    def wifi_remove_callback(self):
        if self.notifying:
            logger.debug('Callback WiFi Remove')
            value = string_to_dbus_byte_array(self.wifi_status)
            self.PropertiesChanged(minerconfig.constants.GATT_CHRC_IFACE, {"Value": value}, [])

        return self.notifying

    def StartNotify(self):

        logger.debug('Notify WiFi Remove')
        if self.notifying:
            return

        self.notifying = True

        value = string_to_dbus_byte_array(self.wifi_status)
        self.PropertiesChanged(minerconfig.constants.GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(30000, self.wifi_remove_callback)

    def StopNotify(self):
        self.notifying = False

    def WriteValue(self, value, options):
        logger.debug('Write WiFi Remove')
        wifi_remove_ssid = wifi_remove_pb2.wifi_remove_v1()
        wifi_remove_ssid.ParseFromString(bytes(value))
        nmcli_custom.connection.delete(wifi_remove_ssid.service)
        logger.debug('Connection %s should be deleted'
                      % wifi_remove_ssid.service)

    def ReadValue(self, options):
        logger.debug('Read WiFi Renove')
        return string_to_dbus_byte_array(self.wifistatus)