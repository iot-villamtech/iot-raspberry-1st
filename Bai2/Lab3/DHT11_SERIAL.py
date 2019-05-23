import Adafruit_DHT
import RPi._GPIO as GPIO
import time

# Adafruit_DHT ho tro nhieu loai cam bien DHT (DHT11, DHT22, DHT21)
# O day dung DHT11 nen chon cam bien  DHT11
chon_cam_bien = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BCM)

# chan DATA duoc noi vao chan GPIO18 cua PI
pin_sensor = 18

print("IOT-VILLAMTECH. Demo cam bien do am DHT 11")

while (True):
    # Doc Do am va Nhiet do tu cam bien thong qua thu vien Adafruit_DHT
    # Ham read_retry se doc gia tri Do am va Nhiet do cua cam bien
    # neu khong thanh cong se thu 15 lan, moi lan cach nhau 2 giay.
    do_am, nhiet_do = Adafruit_DHT.read_retry(chon_cam_bien, pin_sensor)

    # Kiem tra gia tri tra ve tu cam bien (do _am va nhiet_do) khac NULL
    if do_am is not None and nhiet_do is not None:
        print("Nhiet Do = {0:0.1f} C  Do Am = {1:0.1f} %\n".format(nhiet_do, do_am))
        print("IOT-VILLAMTECH. Cho 2 giay de tiep tuc do ...\n")
        time.sleep(2)
    else:
        # Loi :(
        print("Loi khong the doc tu cam bien DHT11 :(\n")
