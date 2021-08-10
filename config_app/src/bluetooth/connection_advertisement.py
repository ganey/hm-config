from lib.cputemp.advertisement import Advertisement
from lib.helium_hardware_definitions.variant_definitions import variant_definitions

MAC_ADDRESS_PATH = "/sys/class/net/eth0/address"
ADVERTISEMENT_SERVICE_UUID = "0fda92b2-44a2-4af2-84f5-fa682baa2b8d"
UNKNOWN_MAC_ADDRESS_NAME = "UNKNOWN_MAC"

class ConnectionAdvertisement(Advertisement):
    # BLE advertisement
    def __init__(self, index, variant):
        Advertisement.__init__(self, index, "peripheral")
        try:
            mac_address = open(MAC_ADDRESS_PATH) \
                .readline() \
                .strip() \
                .replace(":", "")[-6:] \
                .upper()

        except FileNotFoundError:
            mac_address = UNKNOWN_MAC_ADDRESS_NAME

        advertisement_name = "Nebra %s Hotspot (%s)" % (mac_address, variant)
        self.add_local_name(advertisement_name)
        self.include_tx_power = True
        self.service_uuids = [ADVERTISEMENT_SERVICE_UUID]