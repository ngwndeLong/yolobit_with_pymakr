from yolobit import *
import task_readSensors

status = 0

def task_init():
    global status
    status = 0
    pin14.write_digital(0)

def task_run():
    global status
    light = task_readSensors.current_light

    if light is None:
        return

    try:
        if light < 20:
            if status == 0:
                pin14.write_digital(1)
                status = 1
                print(f"[Light] ON ({light}%)")
        else:
            if status == 1:
                pin14.write_digital(0)
                status = 0
                print(f"[Light] OFF ({light}%)")
    except Exception as e:
        print("[controlLight]: ", e)