import logging
import dbus
from time import sleep
import h3

from lib.cputemp.service import Characteristic
import minerconfig.constants
from minerconfig.bluetooth.descriptors.assert_location_descriptor import AssertLocationDescriptor
from minerconfig.bluetooth.descriptors.utf8_format_descriptor import UTF8FormatDescriptor
import lib.protos.assert_location_pb2 as assert_location_pb2

class EthernetOnlineCharacteristic(Characteristic):

    def __init__(self, service):
        Characteristic.__init__(
                self, minerconfig.constants.ETHERNET_ONLINE_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(EthernetOnlineDescriptor(self))
        self.add_descriptor(UTF8FormatDescriptor(self))

    def ReadValue(self, options):

        logging.debug('Read Ethernet Online')

        value = []

        val = "false"

        if(open("/sys/class/net/eth0/carrier").readline().strip() == "1"):
            val = "true"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value