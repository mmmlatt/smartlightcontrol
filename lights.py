import tinytuya

#Lights with their IDs
lroom1_light = tinytuya.BulbDevice("Device ID", "Device IP", "Device Key")
lroom1_light.name = "Living Room Light 1"
lroom2_light = tinytuya.BulbDevice("Device ID", "Device IP", "Device Key")
lroom2_light.name = "Living Room Light 2"
lroom3_light = tinytuya.BulbDevice("Device ID", "Device IP", "Device Key")
lroom3_light.name = "Living Room Light 3"
lroom4_light = tinytuya.BulbDevice("Device ID", "Device IP", "Device Key")
lroom4_light.name = "Living Room Light 4"
office1_light = tinytuya.BulbDevice("Device ID", "Device IP", "Device Key")
office1_light.name = "Office Light 1"
office2_light = tinytuya.BulbDevice("Device ID", "Device IP", "Device Key")
office2_light.name = "Office Light 2"
office3_light = tinytuya.BulbDevice("Device ID", "Device IP", "Device Key")
office3_light.name = "Office Light 3"

light_list = [lroom1_light, lroom2_light, lroom3_light, lroom4_light, office1_light, office2_light, office3_light]

#Function to run set_version on all lights when app starts
def init_status(lights):
    for light in lights:
        light.set_version(3.4)
        light.set_socketPersistent(True)