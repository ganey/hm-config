import logging
import dbus

from lib.cputemp.service import Application, Service, Characteristic, Descriptor
import minerconfig.constants

MANUFACTURER_NAME = "Nebra LTD."

class ManufactureNameCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
                self, minerconfig.constants.MANUFACTURE_NAME_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        logging.debug('Read Manufacturer')
        value = []
        val = MANUFACTURER_NAME
        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value