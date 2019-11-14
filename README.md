# Device Relay

## Technology
Software: [Micropython](https://micropython.org/),
[MQTT](https://www.eclipse.org/paho/),
[Kotlin](https://kotlinlang.org/),
[Firebase](https://firebase.google.com/?hl=pt-BR)

Hardware: [MCU esp8266](https://www.espressif.com/sites/default/files/documentation/ESP8266-DevKitC_getting_started_guide__EN.pdf), 
[Relay](https://www.fecegypt.com/uploads/dataSheet/1522335719_relay%20module.pdf)

## Ecosystem
![Ecosystem](https://user-images.githubusercontent.com/17392173/68856812-286de680-06c0-11ea-878d-91e09c082a28.jpg)

## Install Micropython

[esptool](https://github.com/espressif/esptool):
```
$ python3 -m pip install esptool
```
Download Micropython:
https://micropython.org/download
```
$ esptool.py --port /dev/ttyUSB0 erase_flash
$ esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin
```
Copy project archives for MCU esp8266:
```
$ ./put_all_files
```
To remove all the files:
```
$ ./rm_all_files
```
