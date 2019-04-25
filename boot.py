# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
import gc

import main
import mqtt_client
import wifi
import dht11
import time

connect = wifi.connect()

if not connect:
    print("not connected...")
    wifi.access_point()
    main.listen()
else:
    print("connected wifi")
    mac = wifi.getMacAddress()
    print(mac)
    topic = b"" + (mac + "/coffeeiot").encode()
    broker_topic = b"" + (mac + "/coffeeiot/broker").encode()
    topics = [topic, broker_topic]
    #topic = b"" + (mac + "/coffeeiot").encode()

    # print(topics)
    # for topic in topics:
    #     print("ESP8266 is Connected to %s and subscribed to %s topic" %
    #       ("dasdas", topic))
    mqtt_client.init()
    mqtt_client.subscribe(topics)
gc.collect()
