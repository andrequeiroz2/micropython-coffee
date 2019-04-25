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
    # unique identifier of the chip
    "CLIENT_ID": b"esp8266_" + ubinascii.hexlify(machine.unique_id())
}
# Create an instance of MQTTClient
client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'],
                user=CONFIG['USER'], password=CONFIG['PASSWORD'], port=CONFIG['PORT'])

# Method to act based on message received
def onMessage(topic, msg):
    print("Topic: %s, Message: %s" % (topic, msg))

    if msg == b"on":
        pin.on()
        # led.on()
    elif msg == b"off":
        pin.off()
        # led.off()
    
def init():
    client.set_callback(onMessage)
    client.connect()
    
def publish(topic, msg):
    client.publish(topic, msg)
    
def subscribe(topics):
    print(topics)
    for topic in topics:
        client.subscribe(topic)
        print("ESP8266 is Connected to %s and subscribed to %s topic" %
          (CONFIG['MQTT_BROKER'], topic))
    
    try:
        while True:
            print("wait_msg")
            client.wait_msg()
            # msg = (client.check_msg())
    except Exception as e:
        print("type error: " + str(e))   