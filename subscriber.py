import umqtt.robust as umqtt
from network import WLAN
import time

from machine import Pin, Timer


HOSTNAME = ''
PORT = 5050
TOPIC = 'temp/pico'

wifi = WLAN(WLAN.IF_STA)
wifi.active(True)

ssid = ''
password = ''

mqtt = umqtt.MQTTClient(
    client_id = b'subscriber',
    server = HOSTNAME.encode(),
    port = PORT,
    keepalive = 7000
)


def connect(
    wifi_obj,
    ssid,
    password,
    timeout =10
):
    wifi_obj.connect(ssid,password)
    
    while timeout > 0:
        if wifi_obj.status() !=3:
            time.sleep(1)
            timeout -= 1
        else:
            return True
        
    return False

wifi.connect(ssid,password)
time.sleep(2)

if wifi.status() != 3:
    print("Could not connect")
else:
    print("Sucessfully connected")
    
    
def callback(topic,message):
    print(f'Temperature is : {message}')
    
    temp = float(message)
    
    led = Pin("LED", Pin.OUT)
    
    if temp > 30 :
        led.on()
        
    else :
        led.off()

mqtt.connect()

mqtt.set_callback(callback)
mqtt.subscribe(TOPIC)

while True:
    mqtt.wait_msg()



