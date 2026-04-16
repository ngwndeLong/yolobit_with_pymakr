from yolobit import *
from lib.aiot_lcd1602 import LCD1602
import task_readSensors

aiot_lcd1602 = None

def task_init():
    global aiot_lcd1602
    try:
        aiot_lcd1602 = LCD1602()
        print("[LCD] Init OK")
    except Exception as e:
        print("[LCD] Init fail: ", e)

def task_run():
    if aiot_lcd1602 is None:
        return
    
    temp = task_readSensors.current_temp
    light = task_readSensors.current_light

    try:
        aiot_lcd1602.move_to(0, 0)
        if light is not None:
            aiot_lcd1602.putstr(f"Light: {light}%   ") 
        else:
            aiot_lcd1602.putstr("Light: Error  ")

        aiot_lcd1602.move_to(0, 1)
        if temp is not None:
            aiot_lcd1602.putstr(f"Temp : {temp}*C   ")
        else:
            aiot_lcd1602.putstr("Temp : Error  ")
    except Exception as e:
        print("[openLCD]: ", e)