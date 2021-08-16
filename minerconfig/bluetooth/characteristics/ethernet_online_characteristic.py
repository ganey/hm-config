import logging
import dbus
from time import sleep
import h3
from minerconfig.helpers import string_to_dbus_byte_array

from lib.cputemp.service import Characteristic
import minerconfig.constants
from minerconfig.bluetooth.descriptors.ethernet_online_descriptor import EthernetOnlineDescriptor
from minerconfig.bluetooth.descriptors.utf8_format_descriptor import UTF8FormatDescriptor
import lib.protos.assert_location_pb2 as assert_location_pb2

ETHERNET_IS_ONLINE_CARRIER_VAL = "1"

class EthernetOnlineCharacteristic(Characteristic):

    def __init__(self, service):
        Characteristic.__init__(
                self, minerconfig.constants.ETHERNET_ONLINE_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(EthernetOnlineDescriptor(self))
        self.add_descriptor(UTF8FormatDescriptor(self))

    def ReadValue(self, options):
        logging.debug('Read Ethernet Online')

        is_ethernet_online = "false"

        ethernet_is_online_carrier_val = open("/sys/class/net/eth0/carrier").readline().strip()
        if(ethernet_is_online_carrier_val == ETHERNET_IS_ONLINE_CARRIER_VAL):
            is_ethernet_online = "true"

        return string_to_dbus_byte_array(is_ethernet_online)