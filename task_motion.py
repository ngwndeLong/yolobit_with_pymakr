from yolobit import *
import task_readSensors

status = 0

def task_init():
    global status
    status = 0

def task_run():
    global status
    try:
        motion_detected = task_readSensors.current_motion
        if motion_detected is None:
            return

        if motion_detected == 1:
            if status == 0: 
                status = 1
                print("[Motion] Detected !")
        else:
            if status == 1: 
                status = 0

    except Exception as e:
        print("[Motion]: ", e)