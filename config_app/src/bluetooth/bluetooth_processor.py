from lib.cputemp.service import Application
from src.bluetooth.device_information_service import DeviceInformationService

class BluetoothProcessor(Application):
    def __init__(self):
        super().__init__()
        self.add_service(DeviceInformationService(0))
        # self.add_service(HeliumService(1))
        self.register()
    