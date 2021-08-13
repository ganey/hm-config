import logging

from lib.cputemp.service import Characteristic
import minerconfig.constants

from minerconfig.bluetooth.descriptors.wifi_ssid_descriptor import WifiSSIDDescriptor
from minerconfig.bluetooth.descriptors.utf8_format_descriptor import UTF8FormatDescriptor
from minerconfig.helpers import string_to_dbus_byte_array

from minerconfig.helpers import is_valid_ssid

class WifiSSIDCharacteristic(Characteristic):

    global wifiCache

    def __init__(self, service):
        Characteristic.__init__(
                self, minerconfig.constants.WIFI_SSID_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(WifiSSIDDescriptor(self))
        self.add_descriptor(UTF8FormatDescriptor(self))
        self.wifi_list_cache = []

    def update_wifi_list_cache(self, wifi_list_cache):
        self.wifi_list_cache = wifi_list_cache

    def ReadValue(self, options):

        logging.debug('Read WiFi SSID')
        active_connection = ""
        for network in self.wifi_list_cache:
            ssid_str = str(network.ssid)

            if(is_valid_ssid(ssid_str)):
                if(network.in_use):
                    active_connection = ssid_str

        return string_to_dbus_byte_array(active_connection)