import RPi._GPIO as GPIO
import time

#Khai bao I/O
GPIO.setmode(GPIO.BCM)
led = 14
button = 15

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Trang thai Led off
state_led = False 
GPIO.output(led, state_led)

try:
    while True:
        GPIO.wait_for_edge(button, GPIO.RISING) #phat hien thanh doi khi 1 canh cua xung thay doi(Nhan nut)
        print("OT-VILLAMTECH --->Pressed<---")
        start = time.time() #Bat dau tinh thoi gian nhan nut
        time.sleep(0.2)

        while GPIO.input(button) == GPIO.HIGH: #Kiem tra nut da nhan
            time.sleep(0.02)

        length = time.time() - start #Thoi gian hien tai tru di thoi gian start
        print(length) #In thoi gian ra man hinh

        if length > 0.2: #Neu thoi gian lon hown 200ms thi doi trang thai led
            state_led = ~state_led
        GPIO.output(led, state_led)  #bat/tat led

except KeyboardInterrupt:
    GPIO.cleanup()
