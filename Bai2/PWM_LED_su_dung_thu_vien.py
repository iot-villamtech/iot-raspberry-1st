# PWM LED su dung thu vien
import RPi._GPIO as GPIO
from time import sleep

pin = 14  #khai bao pin out
GPIO.setmode(GPIO.BCM)  #khai bao kieu pin
GPIO.setup(pin, GPIO.OUT)  #setup pin output

pwm = GPIO.PWM(pin, 500)  #khai bao pwm, pin = 14, tan so 500Hz
pwm.start(0)  #bat dau voi duty cycle = 0

# PWM led sang dan
def pwm_led_sang_dan():
     for duty_cycle in range(100):
        pwm.ChangeDutyCycle(duty_cycle)  #thay doi duty cycle tu 0 den 100
        sleep(0.1)

# PWM led tat dan
def pwm_led_tat_dan():
     for duty_cycle in reversed(range(100)):
        pwm.ChangeDutyCycle(duty_cycle)  #thay doi duty cycle tu 0 den 100
        sleep(0.1)

try:
    pwm_led_sang_dan()
    pwm_led_tat_dan()

finally:
    GPIO.cleanup()
