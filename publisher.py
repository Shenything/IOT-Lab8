import umqtt.robust as umqtt
from network import WLAN
import time
from machine import ADC


HOSTNAME = ''
PORT = 5050
TOPIC = 'temp/pico'

wifi = WLAN(WLAN.IF_STA)
wifi.active(True)

ssid =''
password = ''

mqtt = umqtt.MQTTClient(
    client_id = b'publish',
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
    
    

#Temperature code
temp_sensor = ADC(4)
timer = machine.Timer()

def read_temp():
    global temp_sensor
    value = temp_sensor.read_u16()
    voltage = value * (3.3 / 2 ** 16)
    temperature = 27 - (voltage - 0.706) / .001721
    
    return temperature


def function (t):
    temp = read_temp()
    
    
mqtt.connect()
while True:
    temp = read_temp()
    mqtt.publish(TOPIC, str(temp).encode())
    

timer.init(freq=1, mode = machine.Timer.PERIODIC, callback = function)
    

