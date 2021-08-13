import logging
import dbus

from lib.cputemp.service import Characteristic
import minerconfig.constants
from minerconfig.helpers import string_to_dbus_byte_array
from minerconfig.bluetooth.descriptors.diagnostics_descriptor import DiagnosticsDescriptor
from minerconfig.bluetooth.descriptors.opaque_structure_descriptor import OpaqueStructureDescriptor
import minerconfig.nmcli_custom as nmcli_custom
import lib.protos.diagnostics_pb2 as diagnostics_pb2

class DiagnosticsCharacteristic(Characteristic):
    # Returns proto of eth, wifi, fw, ip, p2pstatus

    def __init__(self, service):
        Characteristic.__init__(
                self, minerconfig.constants.DIAGNOSTICS_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(DiagnosticsDescriptor(self))
        self.add_descriptor(OpaqueStructureDescriptor(self))
        self.p2pstatus = ""

    def ReadValue(self, options): # noqa 901
        # TODO (Rob): come back and make this method less complex for
        # C901 complexity rules.
        logging.debug('Read diagnostics')
        logging.debug('Diagnostics miner_bus')
        miner_bus = dbus.SystemBus()
        logging.debug('Diagnostics miner_object')
        miner_object = miner_bus.get_object('com.helium.Miner', '/')
        logging.debug('Diagnostics miner_interface')
        miner_interface = dbus.Interface(miner_object, 'com.helium.Miner')
        logging.debug('Diagnostics p2pstatus')
        try:
            self.p2pstatus = miner_interface.P2PStatus()
            logging.debug('DBUS P2P SUCCEED')
            logging.debug(self.p2pstatus)
        except dbus.exceptions.DBusException:
            self.p2pstatus = ""
            logging.debug('DBUS P2P FAIL')

        try:
            eth_ip = nmcli_custom.device.show('eth0')['IP4.ADDRESS[1]'][:-3]
        except KeyError:
            pass
        try:
            wlanIP = nmcli_custom.device.show('wlan0')['IP4.ADDRESS[1]'][:-3]
        except KeyError:
            pass

        ip_address = "0.0.0.0"  # nosec
        if('eth_ip' in locals()):
            ip_address = str(eth_ip)
        elif('wlanIP' in locals()):
            ip_address = str(wlanIP)

        diagnostics_proto = diagnostics_pb2.diagnostics_v1()
        diagnostics_proto.diagnostics['connected'] = str(self.p2pstatus[0][1])
        diagnostics_proto.diagnostics['dialable'] = str(self.p2pstatus[1][1])
        diagnostics_proto.diagnostics['height'] = str(self.p2pstatus[3][1])
        diagnostics_proto.diagnostics['nat_type'] = str(self.p2pstatus[2][1])
        try:
            diagnostics_proto.diagnostics['eth'] = \
                open("/sys/class/net/eth0/address").readline(). \
                strip().replace(":", "")
        except FileNotFoundError:
            diagnostics_proto.diagnostics['eth'] = "FF:FF:FF:FF:FF:FF"
        diagnostics_proto.diagnostics['fw'] = os.getenv('FIRMWARE_VERSION')
        diagnostics_proto.diagnostics['ip'] = ip_address
        try:
            wifi_diag = open("/sys/class/net/wlan0/address").readline(). \
                strip().replace(":", "")
            diagnostics_proto.diagnostics['wifi'] = wifi_diag
        except FileNotFoundError:
            diagnostics_proto.diagnostics['wifi'] = "FF:FF:FF:FF:FF:FF"
        logging.debug('items added to proto')
        val = diagnostics_proto.SerializeToString()
        logging.debug(val)
        return string_to_dbus_byte_array(val)
