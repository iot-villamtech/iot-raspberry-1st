import RPi._GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

led = 14
GPIO.setup(led, GPIO.OUT)

button = 15
#dien tro keo xuong,bam nut thi chan 15 len muc cao
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

state_led = 0
old_state = 0
lastChangedTime = 0
waitTime = 300


def millis():
    return time.time() * 1000


try:
    while True:
        state = GPIO.input(button)  #lay trang thai tu chan 15       
        if state != old_state:
            old_state = state
            lastChangedTime = millis()

        if (millis() - lastChangedTime) > waitTime:
            old_state = state
            lastChangedTime = millis()

        if old_state == True:  #nut duoc bam
            state_led = ~state_led
            
        print(state_led)  # Xuat trang thai ra man hinh
        GPIO.output(led, state_led) #bat/tat led

except KeyboardInterrupt:
    GPIO.cleanup()