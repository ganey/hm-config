import logging
import os

from minerconfig.minerconfig_app import ConfigApp

VARIANT = os.getenv('VARIANT')
SENTRY_DSN = os.getenv('SENTRY_DSN') # https://docs.sentry.io/product/sentry-basics/dsn-explainer/
BALENA_DEVICE_UUID = os.getenv('BALENA_DEVICE_UUID')
BALENA_APP_NAME = os.getenv('BALENA_APP_NAME')
FIRMWARE_VERSION = os.getenv('FIRMWARE_VERSION')
ETH0_MAC_ADDRESS_PATH = os.getenv('ETH0_MAC_ADDRESS_PATH', '/sys/class/net/eth0/address')
ONBOARDING_KEY_FILEPATH = os.getenv('ONBOARDING_KEY_FILEPATH', '/var/data/public_keys')
DIAGNOSTICS_JSON_FILEPATH = os.getenv('DIAGNOSTICS_JSON_FILEPATH', '/var/data/nebraDiagnostics.json')

def main():
    setup_logging()
    validate_env()
    start_config_app()

def setup_logging():
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

def validate_env():
    logging.debug("Starting with the following ENV:\n\
        SENTRY_DSN=%s\n\
        BALENA_APP_NAME=%s\n\
        BALENA_DEVICE_UUID=%s\n\
        VARIANT=%s\n\
        ETH0_MAC_ADDRESS_PATH=%s\n\
        ONBOARDING_KEY_FILEPATH=%s\n\
        DIAGNOSTICS_JSON_FILEPATH=%s\n\
        FIRMWARE_VERSION=%s\n" % 
        (SENTRY_DSN, BALENA_APP_NAME, BALENA_DEVICE_UUID, VARIANT, 
            ETH0_MAC_ADDRESS_PATH, ONBOARDING_KEY_FILEPATH, DIAGNOSTICS_JSON_FILEPATH, FIRMWARE_VERSION))

    # TODO check if any NONE

def start_config_app():
    config_app = ConfigApp(SENTRY_DSN, BALENA_APP_NAME, BALENA_DEVICE_UUID, VARIANT, 
        ETH0_MAC_ADDRESS_PATH, ONBOARDING_KEY_FILEPATH, DIAGNOSTICS_JSON_FILEPATH, FIRMWARE_VERSION)
    try:
        config_app.start()
    except Exception as e:
        logging.error(e)
        config_app.stop()

if __name__ == "__main__":
    main()