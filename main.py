from event_manager import *
import time
import config

import task_readSensors
import task_openLCD
import task_controlFan
import task_controlLight
import task_motion
# import task_mqtt

event_manager.reset()

task_readSensors.task_init()
task_openLCD.task_init()
task_controlFan.task_init()
task_controlLight.task_init()
task_motion.task_init()

# task_mqtt.task_init()

# event_manager.add_timer_event(config.INTERVAL_TASK_MQTT, task_mqtt.task_run)
event_manager.add_timer_event(config.INTERVAL_UPDATE_SENSORS, task_readSensors.task_run)
event_manager.add_timer_event(config.INTERVAL_TASK_OPENLCD, task_openLCD.task_run)
event_manager.add_timer_event(config.INTERVAL_TASK_CONTROLFAN, task_controlFan.task_run)
event_manager.add_timer_event(config.INTERVAL_TASK_CONTROLLIGHT, task_controlLight.task_run)
event_manager.add_timer_event(config.INTERVAL_TASK_MOTION, task_motion.task_run)

print("Yolobit - demo")

while True:
    event_manager.run()
    time.sleep_ms(10)