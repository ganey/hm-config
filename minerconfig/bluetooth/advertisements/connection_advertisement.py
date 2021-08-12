from lib.cputemp.advertisement import Advertisement
import minerconfig.constants

ADVERTISEMENT_SERVICE_UUID = "0fda92b2-44a2-4af2-84f5-fa682baa2b8d"
UNKNOWN_MAC_ADDRESS_VAL = "XXXXXX"

class ConnectionAdvertisement(Advertisement):
    # BLE advertisement
    def __init__(self, index, advertisement_type, variant):
        Advertisement.__init__(self, index, advertisement_type)
        try:
            mac_address_last6 = open(minerconfig.constants.ETH0_MAC_ADDRESS_PATH) \
                .readline() \
                .strip() \
                .replace(":", "")[-6:] \
                .upper()

        except FileNotFoundError:
            mac_address_last6 = UNKNOWN_MAC_ADDRESS_VAL

        advertisement_name = "Nebra %s Hotspot (%s)" % (mac_address_last6, variant)
        self.add_local_name(advertisement_name)
        self.include_tx_power = True
        self.service_uuids = [ADVERTISEMENT_SERVICE_UUID]