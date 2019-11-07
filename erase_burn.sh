#!/bin/bash
if [ "$1" != "" ]; then
    type="$1"
else
    echo "Positional parameter 1 is empty"
fi

if [ "$2" != "" ]; then
    image="$2"
else
    echo "Positional parameter 1 is empty"
fi

if [ type=="esp32" ]; then
	echo "esp32"
	esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
	esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 $image
else
	if [type=="esp8266"]; then
		echo "esp8266"
	fi	
fi

exit
#esptool.py --port /dev/ttyUSB0 erase_flash &&
#esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp32-idf3-20190529-v1.11.bin
