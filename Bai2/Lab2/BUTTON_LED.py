import RPi._GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

led = 14
GPIO.setup(led, GPIO.OUT)

button = 15
#dien tro keo xuong,bam nut thi chan 15 len muc cao
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        state = GPIO.input(button)  #lay trang thai tu chan 15
        print(state)  # Xuat trang thai ra man hinh
        if state == True:  #nut duoc bam
            GPIO.output(led, True)  #bat led
            sleep(0.1)
        else:
            GPIO.output(led, False)
            sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()