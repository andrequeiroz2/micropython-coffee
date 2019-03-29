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

def getTemperature():
    try:

        temp,hum=dht11.temperature()


        #Turns temp into a string
        temperature=str(temp)

        #Sleep the esp8266 otherwise we get errors as it is not able to process quickly the requests  
        time.sleep(5)
        print(temperature)

    #Finally clause at the end of the try to catch other incoming messages from topics
    finally:
        time.sleep(5)

#    try:  
#    #          c.check_msg()
#    except:
#
#        time.sleep(10*timeouts)
        #machine.reset()

if not connect:
    print("not connected...")
    wifi.access_point()
    main.listen()
else:
    print("connected wifi")
    TOPIC = b"gdgfoz/coffeeiot"
   # mqtt_client.init()
    #mqtt_client.subscribe(TOPIC)
    getTemperature()
gc.collect()
