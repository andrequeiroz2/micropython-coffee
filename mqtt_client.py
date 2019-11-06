import machine
import ubinascii
from umqtt.robust import MQTTClient
import time

# Rele
pin = machine.Pin(14, machine.Pin.OUT)

MQTT_BROKER = "broker.hivemq.com"

CONFIG = {
    "MQTT_BROKER": MQTT_BROKER,
    "USER": "",
    "PASSWORD": "",
    "PORT": 1883,
    "KEEP_ALIVE": 30,
    # unique identifier of the chip
    "CLIENT_ID": b"esp8266_" + ubinascii.hexlify(machine.unique_id())
}
# Create an instance of MQTTClient
client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'],
                    user=CONFIG['USER'], password=CONFIG['PASSWORD'], port=CONFIG['PORT'],
                    keepalive=CONFIG['KEEP_ALIVE'])

# Method to act based on message received


def init(last_to_will):
    if last_to_will:
        client.set_last_will(
            topic_status, "Sensor Offline", qos=0, retain=True)
    client.connect()


def publish(topic, msg):
    print("publish to: ", topic, "data: ", msg)
    client.publish(topic, msg)
