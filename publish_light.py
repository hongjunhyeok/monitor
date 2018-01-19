#! /usr/bin/python3
from Led import Led
#from switch2 import button
#import RPi.GPIO as GPIO
from threading import Thread
import time
from datetime import datetime
import paho.mqtt.client as mqtt
import SensorFrame
t1=datetime.now()
def led_control(client,led,topic):
    topic='home/#' + topic
    if led.get_status():
        led.turn_off()
        client.publish(topic,'OFF'+'/'+str(datetime.now())[0:19])
        
    else:
        led.turn_on()
        client.publish(topic,'ON'+'/'+str(datetime.now())[0:19])

    client.loop(1)
    

def main():
    #GPIO.setmode(GPIO.BCM)
    client=mqtt.Client()
    client.connect('localhost',1883)
    client.loop(1)

    try:
        led1=Led(18)
        led2=Led(17)
        #Thread
        
       # Thread(target=button,args=(23,lambda: led_control(client,led1,'light1'))).start()
      #  Thread(target=button,args=(27,lambda:led_control(client,led2,'light2'))).start()
        while True:
            pass
        #time.sleep(1000)
    finally:
        b_run = False
        time.sleep(1)
      #  GPIO.cleanup()

if __name__ == '__main__':
    main()
