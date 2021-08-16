



# class WiFiRemoveCharacteristic(Characteristic):

#     def __init__(self, service):
#         self.notifying = False
#         Characteristic.__init__(
#                 self, minerconfig.constants.WIFI_REMOVE_CHARACTERISTIC_UUID,
#                 ["read", "write", "notify"], service)
#         self.add_descriptor(WiFiRemoveDescriptor(self))
#         self.add_descriptor(opaqueStructure(self))
#         self.wifistatus = "False"

#     def WiFiRemoveCallback(self):
#         if self.notifying:
#             logging.debug('Callback WiFi Remove')
#             value = []
#             val = self.wifistatus

#             for c in val:
#                 value.append(dbus.Byte(c.encode()))
#             self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])

#         return self.notifying

#     def StartNotify(self):

#         logging.debug('Notify WiFi Remove')
#         if self.notifying:
#             return

#         self.notifying = True

#         value = []

#         for c in self.WiFiStatus:
#             value.append(dbus.Byte(c.encode()))
#         self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
#         self.add_timeout(30000, self.WiFiRemoveCallback)

#     def StopNotify(self):
#         self.notifying = False

#     def WriteValue(self, value, options):
#         logging.debug('Write WiFi Remove')
#         wifiRemoveSSID = wifi_remove_pb2.wifi_remove_v1()
#         wifiRemoveSSID.ParseFromString(bytes(value))
#         nmcli.connection.delete(wifiRemoveSSID.service)
#         logging.debug('Connection %s should be deleted'
#                       % wifiRemoveSSID.service)

#     def ReadValue(self, options):
#         logging.debug('Read WiFi Renove')

#         value = []
#         val = self.wifistatus
#         for c in val:
#             value.append(dbus.Byte(c.encode()))
#         return value


# class WiFiRemoveDescriptor(Descriptor):

#     def __init__(self, characteristic):
#         Descriptor.__init__(
#                 self, minerconfig.constants.USER_DESC_DESCRIPTOR_UUID,
#                 ["read"],
#                 characteristic)

#     def ReadValue(self, options):
#         value = []
#         desc = minerconfig.constants.WIFI_REMOVE_VALUE

#         for c in desc:
#             value.append(dbus.Byte(c.encode()))
#         return value



# class SoftwareVersionCharacteristic(Characteristic):
#     def __init__(self, service):
#         Characteristic.__init__(
#                 self, minerconfig.constants.SOFTWARE_VERSION_CHARACTERISTIC_UUID,
#                 ["read"], service)

#     def ReadValue(self, options):
#         logging.debug('Read Firmware')

#         val = os.getenv('FIRMWARE_VERSION')

#         value = []

#         for c in val:
#             value.append(dbus.Byte(c.encode()))

#         return value


# class utf8Format(Descriptor):

#     def __init__(self, characteristic):
#         Descriptor.__init__(
#                 self, minerconfig.constants.PRESENTATION_FORMAT_DESCRIPTOR_UUID,
#                 ["read"],
#                 characteristic)

#     def ReadValue(self, options):
#         value = []
#         value.append(dbus.Byte(0x19))
#         value.append(dbus.Byte(0x00))
#         value.append(dbus.Byte(0x00))
#         value.append(dbus.Byte(0x00))
#         value.append(dbus.Byte(0x01))
#         value.append(dbus.Byte(0x00))
#         value.append(dbus.Byte(0x00))

#         return value

# def diagnosticsThreadCode():
#     logging.debug("Diagnostics Thread Started")
#     global diagnosticsStatus
#     while True:
#         try:
#             diagnosticsJsonFile = open("/var/data/nebraDiagnostics.json")
#             diagnosticsJsonFile = json.load(diagnosticsJsonFile)
#             if(diagnosticsJsonFile['PF'] is True):
#                 diagnosticsStatus = True
#             else:
#                 diagnosticsStatus = False

#         except FileNotFoundError:
#             diagnosticsStatus = False

#         except json.JSONDecodeError:
#             diagnosticsStatus = False

#         except ValueError:
#             diagnosticsStatus = False
#         sleep(60)


# def ledThreadCode():
#     logging.debug("LED Thread Started")
#     global diagnosticsStatus
#     global advertisementLED

#     while True:
#         if(diagnosticsStatus is False):
#             statusLed.blink(0.1, 0.1, 10, False)
#         elif(advertisementLED is True):
#             statusLed.blink(1, 1, 1, False)
#         else:
#             statusLed.on()
#             sleep(2)

# def startAdvert():
#     global advertise
#     advertise = True
#     logging.debug("Button press advertise queued")


# def advertisementThreadCode():
#     global advertise
#     global advertisementLED
#     global scanWifi
#     logging.debug("Advertising Thread Started")
#     while True:
#         if(advertise is True):
#             advertise = False
#             scanWifi = True
#             try:
#                 BleTools.disconnect_connections()
#             except TypeError:
#                 # Most Likely Already Disconnected
#                 pass
#             adv.register()
#             advertisementLED = True
#             sleep(300)
#             adv.unregister()
#             advertisementLED = False
#             scanWifi = False
#         else:
#             sleep(5)


# def wifiThreadCode():
#     global scanWifi
#     global wifiCache
#     logging.debug("WiFi Thread Started")
#     while True:
#         if(scanWifi is True):
#             logging.debug("Wi-Fi Scanning")
#             wifiCache = nmcli.device.wifi()
                # TODO -> call WifiServicesCharacteristic.update_wifi_list_cache, wificonfigureds12, wifissid4444444
#             logging.debug("Wi-Fi Complete")
#             sleep(15)
#         else:
#             sleep(5)