from minerconfig.minerconfig_shared_state import MinerconfigSharedState
import sentry_sdk
from minerconfig.logger import logger 

import threading
# From imports
from time import sleep
from RPi import GPIO
from lib.hardware.variant_definitions import variant_definitions


from minerconfig.bluetooth.processors.bluetooh_services_processor import BluetoothServicesProcessor
from minerconfig.bluetooth.processors.led_processor import LEDProcessor
from minerconfig.bluetooth.processors.diagnostics_processor import DiagnosticsProcessor
from minerconfig.bluetooth.processors.wifi_processor import WifiProcessor
from minerconfig.bluetooth.processors.bluetooth_advertisement_processor import BluetoothAdvertisementProcessor

from minerconfig.file_loader import read_eth0_mac_address, read_onboarding_key
from minerconfig.helpers import is_indoor_variant
from gpiozero import Button, LED

import nmcli_custom

from gpiozero import Button, LED

USER_BUTTON_HOLD_SECONDS = 2
INDOOR_USER_BUTTON_GPIO = 26
INDOOR_STATUS_LED_GPIO = 25

OTHER_USER_BUTTON_GPIO = 24
OTHER_STATUS_LED_GPIO = 25

class ConfigApp:
    def __init__(self, sentry_dsn, balena_app_name, balena_device_uuid, variant, eth0_mac_address_filepath, onboarding_key_filepath, 
        diagnostics_json_filepath, ethernet_is_online_filepath, firmware_version):

        self.variant = variant
        self.init_sentry(sentry_dsn, balena_app_name, balena_device_uuid, variant)
        self.shared_state = MinerconfigSharedState()
        self.init_nmcli()
        self.init_gpio()

        eth0_mac_address = read_eth0_mac_address(eth0_mac_address_filepath)
        onboarding_key, pub_key, animal_name = read_onboarding_key(onboarding_key_filepath)
        # FIXME don't forget to redact onboarding key from logs
        logger.debug("Read onboarding key: %s, pub_key: %s, animal_name: %s" % (onboarding_key, pub_key, animal_name))

        self.bluetooth_services_processor = BluetoothServicesProcessor(eth0_mac_address, onboarding_key, pub_key, firmware_version, ethernet_is_online_filepath, self.shared_state)
        self.led_processor = LEDProcessor(self.status_led, self.shared_state)
        self.diagnostics_processor = DiagnosticsProcessor(diagnostics_json_filepath, self.shared_state)
        self.wifi_processor = WifiProcessor(self.shared_state)
        self.bluetooth_advertisement_processor = BluetoothAdvertisementProcessor(eth0_mac_address, variant, self.shared_state)
        
    def start(self):
        logger.debug("Starting ConfigApp")
        try:
            self.start_threads()

        except KeyboardInterrupt:
            logger.debug("KEYBOAD INTERRUPTION")
            self.stop()

        except Exception as e:
            logger.error(e)
            self.stop()

    def stop(self):
        logger.debug("Stopping ConfigApp")
        GPIO.cleanup()
        # Quits the cputemp application
        self.bluetooth_processor.quit()

    def init_sentry(self, sentry_dsn, balena_app_name, balena_device_uuid, variant):
        sentry_sdk.init(sentry_dsn, environment=balena_app_name)
        sentry_sdk.set_user({ "id": balena_device_uuid })
        sentry_sdk.set_context("variant", { variant })

    def init_nmcli(self):
        nmcli_custom.disable_use_sudo()

    def init_gpio(self):
        if is_indoor_variant(self.variant):
            user_button_gpio = INDOOR_USER_BUTTON_GPIO
            status_led_gpio = INDOOR_STATUS_LED_GPIO
        else:
            user_button_gpio = OTHER_USER_BUTTON_GPIO
            status_led_gpio = OTHER_STATUS_LED_GPIO
        
        self.user_button = Button(user_button_gpio, hold_time=USER_BUTTON_HOLD_SECONDS)
        self.user_button.when_held= self.start_bluetooth_advertisement
        self.status_led = LED(status_led_gpio)

    # Use daemon threads so that everything exists cleanly when the program stops
    def start_threads(self):
        self.bluetooth_services_thread = threading.Thread(target=self.bluetooth_services_processor.run)
        self.led_thread = threading.Thread(target=self.led_processor.run)
        self.diagnostics_thread = threading.Thread(target=self.diagnostics_processor.run)
        self.wifi_thread = threading.Thread(target=self.wifi_processor.run)
        self.bluetooth_advertisement_thread = threading.Thread(target=self.bluetooth_advertisement_processor.run)

        self.led_thread.daemon = True
        self.led_thread.start()

        # self.bluetooth_services_thread.daemon = True
        self.bluetooth_services_thread.start()

        # self.diagnostics_thread.daemon = True
        self.diagnostics_thread.start()

        # self.wifi_thread.daemon = True
        self.wifi_thread.start()

        # self.bluetooth_advertisement_thread.daemon = True
        self.bluetooth_advertisement_thread.start()

    def start_bluetooth_advertisement(self):
        logger.debug("Starting bluetooth advertisement")
        self.shared_state.should_advertise_bluetooth = True