import factory
import dbus.mainloop.glib
from unittest.mock import patch, mock_open

from minerconfig.bluetooth.advertisements.connection_advertisement import ConnectionAdvertisement

class ConnectionAdvertisementFactory(factory.Factory):
    class Meta:
        model = ConnectionAdvertisement

    eth0_mac_address = 'A1:B2:C3:DD:E5:F6'
    advertisement_type = 'peripheral'
    variant = 'NEBHNT-IN1"'