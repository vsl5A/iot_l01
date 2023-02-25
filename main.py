import random
import sys
import time

from Adafruit_IO import MQTTClient
from uart import  *
# from simple_ai import *
# làm ở video 4/11
AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "1235813"
AIO_KEY = "aio_VmdT844DlvEWC9M3Eh84I4jRRIz6"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " feed id:" + feed_id)
    if feed_id == "nutnhan1":
        if payload == "0":
            writeData("1")
        else:
            writeData("2")
    if feed_id == "nutnhan2":
        if payload == "0":
            writeData("3")
        else:
            writeData("4")
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
count = 10
typea = 0
coun_ai = 5
ai_result = ""
pre_ai = ""
while True:
    count = count - 1
    if count <= 0:
        count = 10
        if typea == 0:
            temp = random.randint(10, 20)
            client.publish("cambien1", temp)
            typea = 1
        elif typea == 1:
            humi = random.randint(50, 70)
            client.publish("cambien2", humi)
            typea = 2
        elif typea == 2:
            light = random.randint(100, 200)
            client.publish("cambien3", light)
            typea = 0
    coun_ai = coun_ai -1
    if coun_ai <=0:
        coun_ai =5
        ai_result = image_detector()
        print(" ai output:", ai_result)
        if pre_ai != ai_result:
            client.publish("ai ", ai_result)
    readSerial(client)
    time.sleep(1)
    pass
