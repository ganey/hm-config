# This file contains all the UUIDs for each service to try and cut it down.
# Also contains all the descriptors

# Helium service
HELIUM_SERVICE_UUID = "0fda92b2-44a2-4af2-84f5-fa682baa2b8d"
ONBOARDING_KEY_FILEPATH = "/var/data/public_keys"

# Generic UUIDs
FIRMWARE_VERSION = "2021.01.01.1"
DEVINFO_SVC_UUID = "180A"
FIRMWARE_SVC_UUID = "0000180a-0000-1000-8000-00805f9b34fb"
MANUFACTURER_NAME_CHARACTERISTIC_UUID = "2A29"
FIRMWARE_REVISION_CHARACTERISTIC_UUID = "2A26"
SERIAL_NUMBER_CHARACTERISTIC_UUID = "2A25"
USER_DESC_DESCRIPTOR_UUID = "2901"
PRESENTATION_FORMAT_DESCRIPTOR_UUID = "2904"

# Firmware UUID
FIRMWARE_VERSION_CHARACTERISTIC_UUID = "00002a26-0000-1000-8000-00805f9b34fb"

# Software Version UUID
SOFTWARE_VERSION_CHARACTERISTIC_UUID = "c0b64050-697d-463a-a33f-70c4825731f8"
SOFTWARE_VERSION_VALUE = "Software Version"

# Onboarding Key
ONBOARDING_KEY_CHARACTERISTIC_UUID = "d083b2bd-be16-4600-b397-61512ca2f5ad"
ONBOARDING_KEY_LABEL = "Onboarding Key"

# Public Key
PUBLIC_KEY_CHARACTERISTIC_UUID = "0a852c59-50d3-4492-bfd3-22fe58a24f01"
PUBLIC_KEY_VALUE = "Public Key"

# WiFiServices
WIFI_SERVICES_CHARACTERISTIC_UUID = "d7515033-7e7b-45be-803f-c8737b171a29"
WIFI_SERVICES_VALUE = "WiFi Services"

# WiFiConfiguredServices
WIFI_CONFIGURED_SERVICES_CHARACTERISTIC_UUID = \
    "e125bda4-6fb8-11ea-bc55-0242ac130003"
WIFI_CONFIGURED_SERVICES_VALUE = "WiFi Configured Services"

# WiFiRemove
WIFI_REMOVE_CHARACTERISTIC_UUID = "8cc6e0b3-98c5-40cc-b1d8-692940e6994b"
WIFI_REMOVE_VALUE = "WiFi Remove"

# Diagnostics
DIAGNOSTICS_CHARACTERISTIC_UUID = "b833d34f-d871-422c-bf9e-8e6ec117d57e"
DIAGNOSTICS_VALUE = "Diagnostics"

# Mac address
MAC_ADDRESS_CHARACTERISTIC_UUID = "9c4314f2-8a0c-45fd-a58d-d4a7e64c3a57"
MAC_ADDRESS_VALUE = "Mac Address"

# Lights
LIGHTS_CHARACTERISTIC_UUID = "180efdef-7579-4b4a-b2df-72733b7fa2fe"
LIGHTS_VALUE = "Lights"


# WiFiSSID
WIFI_SSID_CHARACTERISTIC_UUID = "7731de63-bc6a-4100-8ab1-89b2356b038b"
WIFI_SSID_VALUE = "WiFi SSID"


# AssertLocation
ASSERT_LOCATION_CHARACTERISTIC_UUID = "d435f5de-01a4-4e7d-84ba-dfd347f60275"
ASSERT_LOCATION_VALUE = "Assert Location"

# Add Gateway
ADD_GATEWAY_CHARACTERISTIC_UUID = "df3b16ca-c985-4da2-a6d2-9b9b9abdb858"
ADD_GATEWAY_KEY_VALUE = "Add Gateway"

# WiFiConnect
WIFI_CONNECT_CHARACTERISTIC_UUID = "398168aa-0111-4ec0-b1fa-171671270608"
WIFI_CONNECT_KEY_VALUE = "WiFi Connect"


# Ethernet Online
ETHERNET_ONLINE_CHARACTERISTIC_UUID = "e5866bd6-0288-4476-98ca-ef7da6b4d289"
ETHERNET_ONLINE_VALUE = "Ethernet Online"

# WiFi Codes
wifiStatus = {
    "100": "connected",  # connected
    "50": "already",  # Already Connecting
    "60": "invalid",  # Invalid Key
    "30": "failed"   # Connection Failed
}