#! /usr/bin/python3


#import RPi.GPIO as GPIO
import time
class Led():
    def __init__(self,led_pin):
        self.led_pin=led_pin
                
        self.status=False

         #what should we do??
        #set up , ininitalize the light 
    
        # GPIO.setup(self.led_pin,GPIO.OUT)
        # GPIO.output(self.led_pin,self.status)
       
    def turn_on(self):
        self.status=True
     #   GPIO.output(self.led_pin,self.status)
            
    def turn_off(self):
        self.status=False
      #  GPIO.output(self.led_pin,self.status)
        
    def get_status(self):
        return self.status




if __name__=='__main__ ':
  #  GPIO.setmode(GPIO.BCM)
    try:
        led=Led(18)
        while True:
            led.turn_on()
            time.sleep(0.5)
            led.turn_off()
            time.sleep(0.5)
    except Exception as err:
        print( '{0}'.format(err))


  #  finally:
         #   GPIO.cleanup()