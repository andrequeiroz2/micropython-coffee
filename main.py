import server
import mqtt_client
import wifi
from board import factory_topic_pub
from dht11 import get_data_dht11

is_connected = wifi.connect()

if not is_connected:
    print("not connected...")
    wifi.access_point()
    server.listen()
else:
    print("connected wifi")
    topics = factory_topic_sub()
    mqtt_client.init(True)

    while True:
        try:
            client.check_msg()
        except Exception as e:
            print("type error: " + str(e))

        sensor = get_data_dht11()
        temp = str(topics[0])
        humd = str(topics[1])

        client.publish(topic_temp, temp)
        client.publish(topic_humd, humd)

        time.sleep(20)

        try:
            client.check_msg()

        except Exception as e:
            print("type error: " + str(e))
