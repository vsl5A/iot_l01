import random
import sys
import time

from Adafruit_IO import MQTTClient

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

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
count = 10
while True:
    count = count - 1
    if count <= 0:
        count = 10
        temp = random.randint(10, 20)
        client.publish("cambien1", temp)
    time.sleep(1)
    pass
