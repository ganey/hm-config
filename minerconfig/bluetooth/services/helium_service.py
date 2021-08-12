# class HeliumService(Service):
#     DEVINFO_SVC_UUID = "0fda92b2-44a2-4af2-84f5-fa682baa2b8d"

#     def __init__(self, index):

#         Service.__init__(self, index, self.DEVINFO_SVC_UUID, True)
#         self.add_characteristic(OnboardingKeyCharacteristic(self))
#         self.add_characteristic(PublicKeyCharacteristic(self))
#         self.add_characteristic(WiFiServicesCharacteristic(self))
#         self.add_characteristic(WiFiConfiguredServicesCharacteristic(self))
#         self.add_characteristic(DiagnosticsCharacteristic(self))
#         self.add_characteristic(MacAddressCharacteristic(self))
#         self.add_characteristic(LightsCharacteristic(self))
#         self.add_characteristic(WiFiSSIDCharacteristic(self))
#         self.add_characteristic(AssertLocationCharacteristic(self))
#         self.add_characteristic(AddGatewayCharacteristic(self))
#         self.add_characteristic(WiFiConnectCharacteristic(self))
#         self.add_characteristic(EthernetOnlineCharacteristic(self))
#         self.add_characteristic(SoftwareVersionCharacteristic(self))
#         self.add_characteristic(WiFiRemoveCharacteristic(self))
