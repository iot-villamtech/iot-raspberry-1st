import RPi._GPIO as GPIO
import time
#KHai bao I/O
GPIO.setmode(GPIO.BCM)
button = 15
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        GPIO.wait_for_edge(button, GPIO.RISING) #phat hien thanh doi khi 1 canh cua xung thay doi(Nhan nut)
        print ("IOT-VILLAMTECH --->Pressed<---")
        start = time.time() #Bat dau tinh thoi gian nhan nut
        time.sleep(0.2)

        while GPIO.input(button) == GPIO.HIGH:
            time.sleep(0.02)

        length = time.time() - start #Thoi gian hien tai tru di thoi gian start
        print (length)
        #Xuat thoi gian an nut ra man hinh
        if length > 5:
            print ("Long Press")
        elif length > 1:
            print ("Medium Press")
        else:
            print ("Short Press")

except KeyboardInterrupt:
    GPIO.cleanup()