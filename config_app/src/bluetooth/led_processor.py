import logging
from time import sleep

class LEDProcessor:
    def run(self):
        while True:
            logging.debug("Simulating LED")
            sleep(30)