from lib.cputemp.service import Application, Service, Characteristic, Descriptor
from minerconfig.bluetooth.manufacture_name_characteristic import ManufactureNameCharacteristic
import minerconfig.constants

class DeviceInformationService(Service):
    # Service that provides basic information
    def __init__(self, index):
        Service.__init__(self, index, minerconfig.constants.DEVINFO_SVC_UUID, True)
        self.add_characteristic(ManufactureNameCharacteristic(self))
        # self.add_characteristic(FirmwareRevisionCharacteristic(self))
        # self.add_characteristic(SerialNumberCharacteristic(self))