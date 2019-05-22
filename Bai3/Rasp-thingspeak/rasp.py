import httplib
import json
import urllib
from time import sleep
#Chương trình con tạo dữ liệu để gửi lên server.
###Input - data - dữ liệu cần gửi lên server thingspeak
###Output - params - chuỗi được tạo để gửi lên server
def make_param_thingspeak(data):
    params = urllib.urlencode({'field1': data})
    return params
#Chương trình gửi dữ liệu lên server
###Input - params - dữ liệu cần gửi lên server dạng chuỗi
###Output - respone_data - tín hiệu nhận lại được từ server thingspeak
def thingspeak_post(params):
    headers = {"Content-type": "application/x-www-form-urlencoded",
    "X-THINGSPEAKAPIKEY": "abcdefgh"}
    conn = httplib.HTTPSConnection("api.thingspeak.com")
    conn.request("POST", "/update", params, headers)
    r1 = conn.getresponse()
    respone_data = r1.read()
    conn.close()
    return respone_data
while(1):
#ThingSpeak demo code
#Gui du lieu moi 300s 1 lan
    data_test = 25.5
    params_thingspeak = make_param_thingspeak(round(data_test,2))
    thingspeak_post(params_thingspeak)
    sleep(300)