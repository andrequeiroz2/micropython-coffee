import machine
import network
import ubinascii
import file


def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        data = file.get_wifi_password()
        if data != "":
            print('connecting to network: ', data[0])
            wlan.connect(data[0], data[1])
            retry = 0
            while not wlan.isconnected():
                retry = retry + 1
                if retry < 2000:
                    machine.idle()
                else:
                    break
    print('network config:', wlan.ifconfig())
    if wlan.ifconfig()[0] == "0.0.0.0":
        return False
    return True

def getMacAddress():
    mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    return mac

def access_point():
    ap = network.WLAN(network.AP_IF)
    ap.active()
    WIFI_NAME = 'espcoffee'
    WIFI_PASSWORD = 'esp1234567890'
    ap.config(essid=WIFI_NAME,
              authmode=network.AUTH_WPA_WPA2_PSK, password=WIFI_PASSWORD)
    print('Connect to ', WIFI_NAME, ' network with password', WIFI_PASSWORD,' and access: http://' +
          ap.ifconfig()[0], " in you browser")


def get_networks():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    return wlan.scan()

#     for i in wifi_networks:
#         print(i[0])
