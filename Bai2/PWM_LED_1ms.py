# Chuong trinh chop tat led i thoi gian ngan, mo ta pwm

import RPi._GPIO as GPIO
from time import sleep

pin = 14  #khai bao pin out
GPIO.setmode(GPIO.BCM)  #khai bao kieu pin
GPIO.setup(pin, GPIO.OUT)  #setup pin output

try:
    while True:
        GPIO.output(pin, True)  #bat led
        sleep(0.001)  #delay 1ms
        GPIO.output(pin, False)  #tat led
        sleep(0.009)  #delay 1ms

except KeyboardInterrupt:  #thoat chuong trinh khi an Ctrl + C
    print(" Thoat chuong trinh")
    GPIO.cleanup()
