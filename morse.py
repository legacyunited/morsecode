import RPi.GPIO as GPIO
import time
import json


def servo_begin():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setwarnings(False)
    
    global servo1
    servo1 = GPIO.PWM(11,50)
    servo1.start(0)
    
    servo1.ChangeDutyCycle(2)
    
    time.sleep(1)

def convert(message):
    
    with open("morse-code.json","r") as f:
        morse_code = json.load(f)
    f.close()
    
    servo_begin()
    
    print("Sending morse code to servo")
    
    for each in message:
        if each != " ":
            print(each, ':', morse_code[each])
            code = morse_code[each]
            for every in code:
                if every == '-':
                    servo1.ChangeDutyCycle(10)
                    time.sleep(0.2)
                    servo1.ChangeDutyCycle(2)
                else:
                    servo1.ChangeDutyCycle(4)
                    time.sleep(0.2)
                    servo1.ChangeDutyCycle(2)
                time.sleep(0.3)
            time.sleep(0.5)
                    
                    
        else:
            print("-------space-------")
            time.sleep(1.4)
            
        
    #print("Transmission Complete")
    servo_end()
            
def servo_end():
    servo1.ChangeDutyCycle(0)
    time.sleep(1)
    servo1.stop()
    GPIO.cleanup()
    #print("Goodbye")
    
'''
if __name__ == "__main__":
    pass
'''