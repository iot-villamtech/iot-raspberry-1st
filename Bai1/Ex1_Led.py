import RPi._GPIO as GPIO
from time import sleep
pins = [14, 15, 18, 23, 24]
blink_delay = 0.5

GPIO.setmode(GPIO.BCM)
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)


def tatAll():
    for pin in pins:
        GPIO.output(pin, False)
    sleep(blink_delay)


def sangGiuaRa():
    for pin in range(0, 5):
        GPIO.output(pins, True)
        sleep(blink_delay)
        GPIO.output(pins, False)
        sleep(blink_delay)
    tatAll()


def chopTat():
    for pin in pins:
        GPIO.output(pin, True)
    sleep(blink_delay)
    tatAll()


def sangDanTraiPhai():
    for pin in pins:
        GPIO.output(pin, True)
        sleep(blink_delay)
    tatAll()


def sangDanPhaiTrai():
    for pin in reversed(pins):
        GPIO.output(pin, True)
        sleep(blink_delay)
    tatAll()


def sangDuoiPhaiTrai():
    for pin in pins:
        GPIO.output(pin, True)
        sleep(blink_delay)
        GPIO.output(pin, False)
        sleep(blink_delay)
    tatAll()


def sangDuoiTraiPhai():
    for pin in reversed(pins):
        GPIO.output(pin, True)
        sleep(blink_delay)
        GPIO.output(pin, False)
        sleep(blink_delay)
    tatAll()


try:
    while True:
        sangDuoiPhaiTrai()

except KeyboardInterrupt:
    pass
GPIO.cleanup()