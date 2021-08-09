import os
import sentry_sdk
import dbus
import logging
import sys
import json
import src.nmcli_custom as nmcli
import src.uuids
import h3

import threading
# From imports
from time import sleep
# from RPi import GPIO
from lib.helium_hardware_definitions.variant_definitions import variant_definitions

# BLE Library
from lib.cputemp.advertisement import Advertisement
from lib.cputemp.service import Application, Service, Characteristic, Descriptor
from lib.cputemp.bletools import BleTools

# Protobuf Imports
import lib.protos.add_gateway_pb2
import lib.protos.assert_location_pb2
import lib.protos.diagnostics_pb2
import lib.protos.wifi_connect_pb2
import lib.protos.wifi_remove_pb2
import lib.protos.wifi_services_pb2

from gpiozero import Button, LED

class ConfigApp:
    def start(self):
        logging.debug("Starting ConfigApp")

    def stop(self):
        logging.debug("Stopping ConfigApp")

# # ET Phone Home
# variant = os.getenv('VARIANT')
# sentry_key = os.getenv('SENTRY_CONFIG')
# balena_id = os.getenv('BALENA_DEVICE_UUID')
# balena_app = os.getenv('BALENA_APP_NAME')
# uuids.FIRMWARE_VERSION = os.getenv('FIRMWARE_VERSION')
# sentry_sdk.init(sentry_key, environment=balena_app)
# sentry_sdk.set_user({"id": balena_id})
# sentry_sdk.set_context("variant", {variant})

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

# app = Application()
# app.add_service(DeviceInformationService(0))
# app.add_service(HeliumService(1))
# app.register()

# adv = ConfigAdvertisement(0)

# # Setup GPIO Devices
# variant = os.getenv('VARIANT')
# if (variant == "NEBHNT-IN1") or (variant == "Indoor"):
#     buttonGPIO = 26
#     statusGPIO = 25
# else:
#     buttonGPIO = 24
#     statusGPIO = 25
# userButton = Button(buttonGPIO, hold_time=2)
# statusLed = LED(statusGPIO)

# advertise = True

# count = 0

# appThread = threading.Thread(target=app.run)
# ledThread = threading.Thread(target=ledThreadCode)
# diagnosticsThread = threading.Thread(target=diagnosticsThreadCode)
# advertisementThread = threading.Thread(target=advertisementThreadCode)
# wifiThread = threading.Thread(target=wifiThreadCode)

# userButton.when_held = startAdvert


# # Main Loop Starts Here
# try:
#     print("Starting %s" % (count))
#     # app.run()
#     appThread.daemon = True
#     appThread.start()
#     ledThread.start()
#     diagnosticsThread.start()
#     wifiThread.start()
#     advertisementThread.start()

# except KeyboardInterrupt:
#     app.quit()
#     GPIO.cleanup()
# except Exception as e:
#     print(e)
#     GPIO.cleanup()