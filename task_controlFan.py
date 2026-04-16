from yolobit import *
import task_readSensors

status = 0

def task_init():
    global status
    status = 0
    pin10.write_analog(0)

def task_run():
    global status
    temp = task_readSensors.current_temp

    if temp is None:
        return

    try:
        if temp > 28:
            if status == 0:
                pin10.write_analog(round(translate(70, 0, 100, 0, 1023)))
                status = 1
                print(f"[Fan] ON ({temp:.1f}C)")
        else:
            if status == 1:
                pin10.write_analog(0)
                status = 0
                print(f"[Fan] OFF ({temp:.1f}C)")
    except Exception as e:
        print("[controlFan]: ", e)