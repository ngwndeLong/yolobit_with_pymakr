from yolobit import *
from lib.mqtt import MQTTClient
import config
import task_readSensors
import time

client = None
wifi_connected = False

def task_init():
    global client, wifi_connected
    
    # Connect Wifi 
    print(f"[WiFi] Đang kết nối tới {config.WIFI_SSID}...")
    import wifi
    wifi.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
    
    # Wait for Wifi (10s timeout)
    for _ in range(10):
        if wifi.is_connected():
            wifi_connected = True
            print("[WiFi] Kết nối thành công!")
            break
        time.sleep(1)
        
    if not wifi_connected:
        print("[WiFi] Lỗi: Không thể kết nối WiFi. MQTT sẽ bị vô hiệu hóa.")
        return

    # Init MQTT
    try:
        print("[MQTT] Đang kết nối tới Broker...")
        client = MQTTClient(config.MQTT_SERVER, config.MQTT_PORT, 
                            config.MQTT_USER, config.MQTT_PASSWORD)
        client.connect()
        print("[MQTT] Kết nối thành công!")
    except Exception as e:
        print("[MQTT] Lỗi khởi tạo: ", e)
        client = None

def task_run():
    global client
    if client is None: 
        return

    try:
        temp = task_readSensors.current_temp
        light = task_readSensors.current_light
        motion = task_readSensors.current_motion

        if temp is not None:
            client.publish(config.MQTT_TOPIC_V2, str(temp))
            print(f"[MQTT] Đã gửi Nhiệt độ: {temp} -> {config.MQTT_TOPIC_V2}")
            
        if light is not None:
            client.publish(config.MQTT_TOPIC_V1, str(light))
            print(f"[MQTT] Đã gửi Ánh sáng: {light} -> {config.MQTT_TOPIC_V1}")

        if motion is not None:
            client.publish(config.MQTT_TOPIC_V3, str(motion))
            print(f"[MQTT] Đã gửi Chuyển động: {motion} -> {config.MQTT_TOPIC_V1}")
            
    except Exception as e:
        print("[MQTT] Lỗi quá trình gửi tin: ", e)