import dht
import machine
TPin = 2


def get_data_dht11():

    d = dht.DHT11(machine.Pin(TPin))

    d.measure()

    temperature = d.temperature()
    humidity = d.humidity()
    print("temperature:", temperature)
    hdt11_info = [temperature, humidity]

    return hdt11_info
