from yolobit import *
from lib.aiot_dht20 import DHT20

aiot_dht20 = None
current_temp = None
current_light = None
current_motion = 0

def task_init():
    global aiot_dht20
    try:
        aiot_dht20 = DHT20()
        print("[Sensors] Init DHT20 OK")
    except Exception as e:
        print("[Sensors] Init DHT20 fail: ", e)

def task_run():
    global current_temp, current_light, current_motion
    
    try:
        current_light = round(translate(pin0.read_analog(), 0, 4095, 0, 100))
        print(f"[LightSensor]: {current_light}%")
    except Exception as e:
        print("[Sensors] Light read error: ", e)

    if aiot_dht20 is not None:
        try:
            current_temp = aiot_dht20.dht20_temperature()
            print(f"[DHT20]: {current_temp}*C")
        except Exception as e:
            print("[Sensors] DHT20 read error: ", e)

    try:
        current_motion = pin1.read_digital()
        
    except Exception as e:
        print("[Sensors] Motion read error: ", e)