import logging
import os

from minerconfig.minerconfig import ConfigApp

logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
VARIANT = os.getenv('VARIANT')
SENTRY_DSN = os.getenv('SENTRY_DSN') # https://docs.sentry.io/product/sentry-basics/dsn-explainer/
BALENA_DEVICE_UUID = os.getenv('BALENA_DEVICE_UUID')
BALENA_APP_NAME = os.getenv('BALENA_APP_NAME')
FIRMWARE_VERSION = os.getenv('FIRMWARE_VERSION')

def main():
    config_app = ConfigApp(SENTRY_DSN, BALENA_APP_NAME, BALENA_DEVICE_UUID, VARIANT)
    try:
        config_app.start()
    except Exception as e:
        logging.error(e)
        config_app.stop()

if __name__ == "__main__":
    main()