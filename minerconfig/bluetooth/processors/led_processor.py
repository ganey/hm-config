import logging
from time import sleep

LED_REFRESH_SECONDS = 2

class LEDProcessor:
    def __init__(self, status_led, shared_state):
        self.status_led = status_led
        self.shared_state = shared_state

    def run(self):
        logging.debug("LED Thread Started")

        while True:
            if(self.shared_state.are_diagnostics_ok is False):
                self.status_led.blink(0.1, 0.1, 10, False)
            elif(self.shared_state.is_advertising_bluetooth is True):
                self.status_led.blink(1, 1, 1, False)
            else:
                self.status_led.on()
            sleep(LED_REFRESH_SECONDS)