import RPi._GPIO as GPIO
import tkinter

pin_relay=14
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_relay, GPIO.OUT)

TK = tkinter.Tk()

def BAT():
        GPIO.output(pin_relay, False)

def TAT():
        GPIO.output(pin_relay, True)
_label = tkinter.Label(TK, text="BAT/TAT RELAY")
Nut_Bat = tkinter.Button(TK, height = 5, width = 30, text ="BAT", command = BAT)
Nut_Tat = tkinter.Button(TK, height = 5,width = 30, text ="TAT", command = TAT)

_label.pack()
Nut_Bat.pack()
Nut_Tat.pack()
TK.wm_title('IOT-VILLAMTECH')
TK.mainloop()