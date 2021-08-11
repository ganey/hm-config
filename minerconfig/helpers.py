import dbus

# There is probably a less verbose way of doing this involving builtin functions
# and/or maps. But this is how the working code functions. Maintaining the logic
# for now.
def string_to_dbus_byte_array(str):
    byte_array = []

    for c in str:
            byte_array.append(dbus.Byte(c.encode()))

    return byte_array