import logging

from lib.cputemp.service import Characteristic
import minerconfig.constants
import dbus

from minerconfig.bluetooth.descriptors.wifi_connect_descriptor import WiFiConnectDescriptor
from minerconfig.bluetooth.descriptors.opaque_structure_descriptor import OpaqueStructureDescriptor
from minerconfig.helpers import string_to_dbus_byte_array
from minerconfig.helpers import is_valid_ssid

import lib.protos.wifi_connect_pb2 as wifi_connect_pb2
import minerconfig.nmcli_custom as nmcli_custom


class WifiConnectCharacteristic(Characteristic):

    def __init__(self, service):
        self.notifying = False
        Characteristic.__init__(
                self, minerconfig.constants.WIFI_CONNECT_CHARACTERISTIC_UUID,
                ["read", "write", "notify"], service)
        self.add_descriptor(WiFiConnectDescriptor(self))
        self.add_descriptor(OpaqueStructureDescriptor(self))
        self.wifi_status = ""

    def WiFiConnectCallback(self):
        if self.notifying:
            logging.debug('Callback WiFi Connect')
            value = []
            self.wifi_status = "timeout"

            for c in self.wifi_status:
                value.append(dbus.Byte(c.encode()))
            self.PropertiesChanged(minerconfig.constants.GATT_CHRC_IFACE, {"Value": value}, [])

        return self.notifying

    def StartNotify(self):

        logging.debug('Notify WiFi Connect')
        if self.notifying:
            return

        self.notifying = True

        value = []
        self.wifi_status = self.check_wifi_status()
        for c in self.wifi_status:
            value.append(dbus.Byte(c.encode()))
        self.PropertiesChanged(minerconfig.constants.GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(30000, self.WiFiConnectCallback)

    def StopNotify(self):
        self.notifying = False

    def WriteValue(self, value, options):
        logging.debug('Write WiFi Connect')
        if(self.check_wifi_status() == "connected"):
            nmcli_custom.device.disconnect('wlan0')
            logging.debug('Disconnected From Wifi')
        # logging.debug(value)
        wiFiDetails = wifi_connect_pb2.wifi_connect_v1()
        # logging.debug('PB2C')
        wiFiDetails.ParseFromString(bytes(value))
        # logging.debug('PB2P')
        self.wifi_status = "already"
        logging.debug(str(wiFiDetails.service))

        nmcli_custom.device.wifi_connect(str(wiFiDetails.service),
                                  str(wiFiDetails.password))
        self.wifi_status = self.check_wifi_status()

    def check_wifi_status(self):
        # Check the current wi-fi connection status
        logging.debug('Check WiFi Connect')
        state = str(nmcli_custom.device.show('wlan0')['GENERAL.STATE'].split(" ")[0])
        logging.debug(str(minerconfig.constants.wifiStatus[state]))
        return minerconfig.constants.wifiStatus[state]

    def ReadValue(self, options):

        logging.debug('Read WiFi Connect')
        self.wifi_status = self.check_wifi_status()
        value = []

        for c in self.wifi_status:
            value.append(dbus.Byte(c.encode()))
        return value
