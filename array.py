mac = "asd:asda:da"
topic = b"" + (mac + "/coffeeiot").encode()
broker_topic = b"" + (mac + "/coffeeiot/broker").encode()
topics = [topic, broker_topic]
print(topics)
for topic in topics:
    print("ESP8266 is Connected to %s and subscribed to %s topic" %
          ("dasdas", topic))
