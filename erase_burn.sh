#!/bin/bash
if [ "$1" != "" ]; then
    type="$1"
else
    echo "Parameter type is empty"
fi

if [ "$2" != "" ]; then
    image="$2"
else
    echo "Parameter image is empty"
fi

if [ type=="esp32" ]; then
	echo "Device: esp32 and image: $image"
	esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
	esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 $image
else
	if [ type=="esp8266" ]; then
		echo "Device: esp8266 and image: $image"
		esptool.py --port /dev/ttyUSB0 erase_flash
		esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 $image
	fi	
fi