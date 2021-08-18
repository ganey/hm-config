import sys
import logging
from time import sleep

from lib.cputemp.bletools import BleTools
import json

from minerconfig.bluetooth.advertisements.connection_advertisement import ConnectionAdvertisement

DIAGNOSTICS_REFRESH_SECONDS = 60

class DiagnosticsProcessor:
    def __init__(self, diagnostics_json_filepath, shared_state):
        self.shared_state = shared_state
        self.diagnostics_json_filepath = diagnostics_json_filepath

    def run(self):
        logging.debug("Diagnostics Thread Started")

        while True:
            self.read_diagnostics()
            sleep(DIAGNOSTICS_REFRESH_SECONDS)

    def read_diagnostics_and_get_ok(self):
        diagnostics_json_file = open(self.diagnostics_json_filepath)
        diagnostics_json = json.load(diagnostics_json_file)
        return diagnostics_json['PF'] is True
    
    def read_diagnostics(self):
        try:
            self.shared_state.are_diagnostics_ok = self.read_diagnostics_and_get_ok()

        except FileNotFoundError:
            self.shared_state.are_diagnostics_ok = False

        except json.JSONDecodeError:
            self.shared_state.are_diagnostics_ok = False

        except ValueError:
            self.shared_state.are_diagnostics_ok = False

        except:
            logging.warn("Unexpected error %s" % sys.exc_info()[0])