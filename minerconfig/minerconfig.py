# import os
import sentry_sdk
# import dbus
import logging
# import sys
# import json
# import src.nmcli_custom as nmcli
# import h3

import threading
# From imports
from time import sleep
# from RPi import GPIO
from lib.hardware.variant_definitions import variant_definitions

# # BLE Library
# from lib.cputemp.advertisement import Advertisement
# from lib.cputemp.service import Application, Service, Characteristic, Descriptor
# from lib.cputemp.bletools import BleTools

from minerconfig.bluetooth.processors.bluetooh_services_processor import BluetoothServicesProcessor
from minerconfig.bluetooth.processors.led_processor import LEDProcessor
from minerconfig.bluetooth.processors.bluetooth_advertisement_processor import BluetoothAdvertisementProcessor


# Protobuf Imports
import lib.protos.add_gateway_pb2
import lib.protos.assert_location_pb2
import lib.protos.diagnostics_pb2
import lib.protos.wifi_connect_pb2
import lib.protos.wifi_remove_pb2
import lib.protos.wifi_services_pb2

from gpiozero import Button, LED
MANUFACTURER_NAME = "Nebra LTD."

class ConfigApp:
    def __init__(self, sentry_dsn, balena_app_name, balena_device_uuid, variant):
        self.init_sentry(sentry_dsn, balena_app_name, balena_device_uuid, variant)
        self.variant = variant
        self.restart_counter = 0
        self.bluetooth_services_processor = BluetoothServicesProcessor()
        # self.led_processor = LEDProcessor()
        self.bluetooth_advertisement_processor = BluetoothAdvertisementProcessor(variant)
        
    def start(self):
        logging.debug("Starting ConfigApp")
        try:
            print("Starting %s" % (self.restart_counter))
            bluetooth_services_thread = threading.Thread(target=self.bluetooth_services_processor.run)
            # led_thread = threading.Thread(target=self.led_processor.run)
            bluetooth_advertisement_thread = threading.Thread(target=self.bluetooth_advertisement_processor.run)
            bluetooth_services_thread.daemon = True
            bluetooth_services_thread.start()
            # led_thread.start()
            bluetooth_advertisement_thread.start()
            # ledThread.start()
            # diagnosticsThread.start()
            # wifiThread.start()
            # advertisementThread.start()

        except KeyboardInterrupt:
            logging.debug("KEYBOAD INTERRUPTION")
            self.bluetooth_processor.quit()
            # GPIO.cleanup()
        except Exception as e:
            logging.error(e)
            # GPIO.cleanup()

    def stop(self):
        logging.debug("Stopping ConfigApp")

    def init_sentry(self, sentry_dsn, balena_app_name, balena_device_uuid, variant):
        sentry_sdk.init(sentry_dsn, environment=balena_app_name)
        sentry_sdk.set_user({ "id": balena_device_uuid })
        sentry_sdk.set_context("variant", { variant })

# variantDetails = variant_definitions[variant]

# # Disable sudo for nmcli
# nmcli.disable_use_sudo()

# GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"
# NOTIFY_TIMEOUT = 5000

# # Public Onboarding Keys
# while True:
#     try:
#         public_keys_file = open("/var/data/public_keys").readline().split('"')
#         break
#     except FileNotFoundError:
#         logging.debug('Waiting for keyfile')
#     sleep(60)

# # Keyfile exists, now running.
# pubKey = str(public_keys_file[1])
# onboardingKey = str(public_keys_file[3])
# animalName = str( [5])

# # Setup Thread Variables
# advertisementLED = False
# diagnosticsStatus = False
# scanWifi = False
# wifiCache = []

# logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)



# adv = ConfigAdvertisement(0)

# # Setup GPIO Devices
# if (variant == "NEBHNT-IN1") or (variant == "Indoor"):
#     buttonGPIO = 26
#     statusGPIO = 25
# else:
#     buttonGPIO = 24
#     statusGPIO = 25
# userButton = Button(buttonGPIO, hold_time=2)
# statusLed = LED(statusGPIO)

# advertise = True


# ledThread = threading.Thread(target=ledThreadCode)
# diagnosticsThread = threading.Thread(target=diagnosticsThreadCode)
# advertisementThread = threading.Thread(target=advertisementThreadCode)
# wifiThread = threading.Thread(target=wifiThreadCode)

# userButton.when_held = startAdvert


