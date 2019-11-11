import machine
import ubinascii
from umqtt.robust import MQTTClient
import time

MQTT_BROKER = "broker.hivemq.com"


CONFIG = {
    "MQTT_BROKER": MQTT_BROKER,
    "USER": "",
            "PASSWORD": "",
            "PORT": 1883,
            "KEEP_ALIVE": 30,
            # unique identifier of the chip
            "CLIENT_ID": b"esp8266_" + ubinascii.hexlify(machine.unique_id())}


# Create an instance of MQTTClient
client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'], user=CONFIG['USER'],
                    password=CONFIG['PASSWORD'], port=CONFIG['PORT'], keepalive=CONFIG['KEEP_ALIVE'])


def init():
    client.connect()


def check_msg():
    client.check_msg()


def disconnect():
    client.disconnect()


def publish(topic, msg, retain=True):
    print("topic:", topic, " / msg: ", msg)
    client.publish(topic, msg, qos=0, retain=retain)
