from lib.cputemp.service import Application, Service, Characteristic, Descriptor
from src.bluetooth.manufacture_name_characteristic import ManufactureNameCharacteristic
import src.constants

class DeviceInformationService(Service):
    # Service that provides basic information
    def __init__(self, index):
        Service.__init__(self, index, src.constants.DEVINFO_SVC_UUID, True)
        self.add_characteristic(ManufactureNameCharacteristic(self))
        # self.add_characteristic(FirmwareRevisionCharacteristic(self))
        # self.add_characteristic(SerialNumberCharacteristic(self))