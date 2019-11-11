import dht
import machine


def get_data_dht11(pin):

    d = dht.DHT11(machine.Pin(pin))
    d.measure()

    temperature = d.temperature()
    humidity = d.humidity()

    hdt11_info = [temperature, humidity]

    return hdt11_info
