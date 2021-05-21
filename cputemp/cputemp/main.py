"""
Test app to push the current CPU temperature to MQTT every 30 seconds.
"""
import os
import paho.mqtt.client as mqtt
from datetime import datetime
import time

def get_cpu_temp():
    """
    Obtains the current value of the CPU temperature.
    :returns: Current value of the CPU temperature if successful, zero value otherwise.
    :rtype: float
    """
    # Initialize the result.
    result = 0.0
    # The first line in this file holds the CPU temperature as an integer times 1000.
    # Read the first line and remove the newline character at the end of the string.
    if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            line = f.readline().strip()
        # Test if the string is an integer as expected.
        if line.isdigit():
            # Convert the string with the CPU temperature to a float in degrees Celsius.
            result = float(line) / 1000
    # Give the result back to the caller.
    return result


client = mqtt.Client()
while True:
    client.connect("localhost", 1883, 60)
    data = "{}, {}, {:.2f}".format(os.getenv('BALENA_DEVICE_UUID'),
                            datetime.now().strftime("%m/%d/%Y %H:%M:%S"),
                            get_cpu_temp())

    #print("Sending " + str(now))
    msgInfo = client.publish('cpu_temp', data, 0, False)
    if False == msgInfo.is_published():
        msgInfo.wait_for_publish()
    client.disconnect()

    time.sleep(30)
