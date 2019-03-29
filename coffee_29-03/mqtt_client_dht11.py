from umqtt.simple import MQTTClient
from machine import Pin
import time
import machine
import dht11

server="broker.hivemq.com"

timeouts=2

#Define the topics
ttopic=b"gdgfoz/coffeeiot/temperature" #Temperature Topic
htopic=b"gdgfoz/coffeeiot/humidity" #Humidity Topic
stopic=b"gdgfoz/coffeeiot/status"  #Status Topic
ctopic=b"gdgfoz/coffeeiot/command" #Command Topic   
mtopic=b"gdgfoz/coffeeiot/monitor"#Monitor Topic

#Send status to status topic
def send_status(message):
  c.publish(stopic, message)  

#Sets the sleep mode
def esp_sleep(secondi):
  rtc=machine.RTC()
  rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
  send_status("Sensor going to sleep now")
  time.sleep(timeouts)
  send_mstatus("Sensor going to sleep now")
  rtc.alarm(rtc.ALARM0,secondi*1000)
  machine.deepsleep()
  
#Send status to status monitor topic
def send_mstatus(message):
  c.publish(mtopic, message)  
 
# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    if topic == b"gdgfoz/coffeeiot/command":
     
      if msg == b"Restart":
        send_status("Restarting")
        time.sleep(timeouts)
        machine.reset()
      elif msg == b"":
        send_status("Command not valid") 
        
      else:
        i=len(msg)
        dato=msg[:5]
        if dato== b"Sleep":

          tsleep=int(msg[6:i])

          
          if tsleep is not None:
            if tsleep >= 1:
              
              esp_sleep(tsleep)
              
            else:
              send_status("Sleep command error")  
            
          else:
            send_status("Command not valid")
                                 
        else: 
          send_status("Command not valid")
             
    else:
      print("Other command")

      
    
   
#Connects to the various topics 
def connetti():
  while True:
    try:
      c.connect()

      c.subscribe(ttopic)
      c.subscribe(htopic)
      c.subscribe(ctopic)
      c.subscribe(stopic)
      c.subscribe(mtopic)
      send_status("Sensor Ready Again")
      time.sleep(3*timeouts) 
      break
    except:
      #If it is not able to connect to mosquitto restart the device
     
      time.sleep(5*timeouts)
      machine.reset()  
    finally:
      time.sleep(5)
     
      
#Publish to different topics (temp and hum) 
def pubblica(topic,message): 
 c.publish(topic, message) 
  
#Define the mqtt client. callback method and connects to mqtt    
c = MQTTClient("coffeeiot", server)
c.set_callback(sub_cb)
connetti()


#Variables to manage the monitor and when send the temperature
monitor=False
inviatemp=True

#Main iteration 
while True:
  try:
    if monitor == True:          
      #Send status to monitor topic  
      send_mstatus("Sensor Ready")      
      #Sleep the esp8266 otherwise we get errors as it is not able to process quickly the requests
      time.sleep(5*timeouts)
      monitor=False
    elif monitor==False:
      monitor=True 
      
    #check the messages from topics    
    # Non-blocking wait for message
    try:  
      c.check_msg()
    except:
       time.sleep(5*timeouts)
       machine.reset()
    
    temp,hum=dht11.temperatura()
    
      
    #Turns temp into a string
    temperatura=str(temp)
    
    #Sleep the esp8266 otherwise we get errors as it is not able to process quickly the requests  
    time.sleep(5*timeouts)    

    #Turns hum into a string
    umidita=str(hum)
    
    #Check if to send temperature or humidity values to the topics
    if inviatemp == True:
      
      pubblica(ttopic,temperatura) 
      inviatemp=False
    else:  
      pubblica(htopic,umidita) 
      inviatemp=True
    
    time.sleep(10*timeouts)
    
    #Finally clause at the end of the try to catch other incoming messages from topics
  finally:
    time.sleep(5*timeouts)
    
    try:  
      c.check_msg()
    except:
      
      time.sleep(10*timeouts)
      machine.reset()
   
c.disconnect()