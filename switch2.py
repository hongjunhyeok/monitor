#import RPi.GPIO as GPIO
import time


debounceDelay=0.050
def button(switch_pin,on_click):
    GPIO.setup(switch_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    
    buttonState = None
    lastButtonState = GPIO.LOW
    lastDebounceTime=0
    
    try:
        while True:
            reading = GPIO.input(switch_pin)
            
            
            if reading != lastButtonState:
                lastDebounceTime = time.time()
                
                #ignore if ~~
            if (time.time() - lastDebounceTime) > debounceDelay :
                    
                    if reading != buttonState:
                        buttonState = reading
                    
                        if buttonState==GPIO.LOW:
                            on_click()
                         
            lastButtonState = reading
                
    finally:
            GPIO.cleanup()

            
if __name__=='__main__':
    GPIO.setmode(GPIO.BCM)
    button(23,lambda : print('--click--'))


