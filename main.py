import server
import mqtt_client
import wifi
import time
from board import factory_topic_pub
from dht11 import get_data_dht11
Tpin = 4

is_connected = wifi.connect()

if not is_connected:
    print("not connected...")
    wifi.access_point()
    server.listen()
else:
    print("connected wifi")
    topics = factory_topic_pub()
    mqtt_client.init()

    topic_temp = str(topics[0])
    topic_humd = str(topics[1])

    while True:

        sensor = get_data_dht11(Tpin)
        temp = str(sensor[0])
        humd = str(sensor[1])

        mqtt_client.publish(topic_temp, temp)
        mqtt_client.publish(topic_humd, humd)

        time.sleep(20)

    mqtt_client.disconnect()
