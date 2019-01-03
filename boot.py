# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
import gc

import main
import mqtt_client
import wifi

connect = wifi.connect()
if not connect:
    print("not connected...")
    wifi.access_point()
    main.listen()
else:
    print("connected wifi")
    mqtt_client.init()
gc.collect()
