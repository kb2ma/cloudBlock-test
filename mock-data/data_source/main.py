"""
Test app to push the current time to MQTT every 30 seconds.
"""
import paho.mqtt.client as mqtt
from datetime import datetime
import time

client = mqtt.Client()
while True:
    client.connect("localhost", 1883, 60)
    now_str = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    #print("Sending " + str(now))
    msgInfo = client.publish('cloud-input', now_str, 0, False)
    if False == msgInfo.is_published():
        msgInfo.wait_for_publish()
    client.disconnect()

    time.sleep(30)
