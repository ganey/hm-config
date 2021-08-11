from lib.cputemp.service import Application, Service, Characteristic, Descriptor
from minerconfig.bluetooth.characteristics.manufacture_name_characteristic import ManufacturerNameCharacteristic
from minerconfig.bluetooth.characteristics.firmware_revision_characteristic import FirmwareRevisionCharacteristic
from minerconfig.bluetooth.characteristics.serial_number_characteristic import SerialNumberCharacteristic
import minerconfig.constants

class DeviceInformationService(Service):
    # Service that provides basic information
    def __init__(self, index):
        Service.__init__(self, index, minerconfig.constants.DEVINFO_SVC_UUID, True)
        self.add_characteristic(ManufacturerNameCharacteristic(self))
        self.add_characteristic(FirmwareRevisionCharacteristic(self))
        self.add_characteristic(SerialNumberCharacteristic(self))