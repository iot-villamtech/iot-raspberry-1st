from tkinter import *
import RPi._GPIO as GPIO
import time

pin = 14  #khai bao pin out
GPIO.setmode(GPIO.BCM)  #khai bao kieu pin
GPIO.setup(pin, GPIO.OUT)  #setup pin output

pwm = GPIO.PWM(pin, 500)  #khai bao pwm, pin = 14, tan so 500Hz
pwm.start(0)  #bat dau voi duty cycle = 0

class App:
    def __init__(self, master): #su dung con tro
        #tao giao dien
        frame = Frame(master)
        frame.pack()

        Label(frame, text='Do Sang').grid(row=0, column=0)

        scaleRed = Scale(frame,
                         length=500,
                         from_=0,
                         to=100,
                         orient=HORIZONTAL,
                         command=self.dieuchinhpwm) #bat su kien keo thanh slide sau do goi to dieuchinhpwm
        scaleRed.grid(row=0, column=1)
    #Dieu chinh pwm
    def dieuchinhpwm(self, duty):
        pwm.ChangeDutyCycle(float(duty))


root = Tk()
root.wm_title('RasPi.vn-Dieu Khien Do Sang LED')
app = App(root)
root.geometry("600x100+0+0")
try:
    root.mainloop()
finally:
    GPIO.cleanup()