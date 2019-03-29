#Module to read temperature and humidity with dht11 sensor
import dht
import machine
TPin=5 #GPIO Pin
def temperature():
  
  d=dht.DHT11(machine.Pin(TPin))
  d.measure()
 
  temperature=d.temperature()
  humidity=d.humidity()
 
  print(d.temperature())
  print(d.humidity())
  return temperature,humidity
  