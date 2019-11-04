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
    # mac = wifi.getMacAddress()
    # print(mac)
    # topic = b"" + (mac + "/coffeeiot").encode()
    # broker_topic = b"" + (mac + "/coffeeiot/broker").encode()
    # topics = [topic, broker_topic]
    #topic = b"" + (mac + "/coffeeiot").encode()

    topics = factory_topic_sub()

    # print(topics)
    # for topic in topics:
    #     print("ESP8266 is Connected to %s and subscribed to %s topic" %
    #       ("dasdas", topic))
    mqtt_client.init()
    mqtt_client.subscribe(topics)
