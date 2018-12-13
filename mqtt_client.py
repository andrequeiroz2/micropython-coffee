from umqtt.simple import MQTTClient
from machine import Pin
import machine
import ubinascii

# Setup a GPIO Pin for output
led = Pin(12, Pin.OUT)
pin = machine.Pin(2, machine.Pin.OUT)
pin2 = machine.Pin(4, machine.Pin.OUT)

# Modify below section as required
CONFIG = {
     # Configuration details of the MQTT broker
     "MQTT_BROKER": "iot.eclipse.org",
     "USER": "",
     "PASSWORD": "",
     "PORT": 1883,
     "TOPIC": b"andre/micro/python",
     # unique identifier of the chip
     "CLIENT_ID": b"esp8266_" + ubinascii.hexlify(machine.unique_id())
}


# Method to act based on message received
def onMessage(topic, msg):
    print("Topic: %s, Message: %s" % (topic, msg))

    if msg == b"on":
        pin.off()
        led.on()
        pin2.on()
    elif msg == b"off":
        pin.on()
        led.off()
        pin2.off()

def init():
    #Create an instance of MQTTClient
    client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'], user=CONFIG['USER'], password=CONFIG['PASSWORD'], port=CONFIG['PORT'])
    # Attach call back handler to be called on receiving messages
    client.set_callback(onMessage)
    client.connect()
    #client.publish("test", "ESP8266 is Connected")
    client.subscribe(CONFIG['TOPIC'])
    print("ESP8266 is Connected to %s and subscribed to %s topic" % (CONFIG['MQTT_BROKER'], CONFIG['TOPIC']))

    try:
        while True:
            client.wait_msg()
            #msg = (client.check_msg())
    finally:
        client.disconnect()
	# client.publish("test", "ESP8266 is Connected")

# init()