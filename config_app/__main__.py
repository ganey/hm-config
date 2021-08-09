import logging
import os

from src.config_app import ConfigApp

logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

def main():
    config_app = ConfigApp()
    try:
        config_app.start()
    except Exception as e:
        logging.error(e)
        config_app.stop()

if __name__ == "__main__":
    main()