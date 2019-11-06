import server
import mqtt_client
import wifi
from board import factory_topic_sub

is_connected = wifi.connect()

if not is_connected:
    print("not connected...")
    wifi.access_point()
    server.listen()
else:
    print("connected wifi")
    topics = factory_topic_sub()
    mqtt_client.init()
    mqtt_client.subscribe(topics)
