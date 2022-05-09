from machine import Pin, PWM
from umqtt.simple import MQTTClient
from time import sleep_ms as delay
import network

fHz = 10000
red = PWM(Pin(23), fHz)
green = PWM(Pin(22), fHz)
blue = PWM(Pin(21), fHz)

def map(valCon, valMax, valMin):
    valObt = (valCon * valMax)/valMin
    return round(valObt)

def subs(top, msg):
    if top == b'esp/RGB/R' and msg == b'1':
        red.duty(1023)
    elif top == b'esp/RGB/R' and msg == b'0':
        red.duty(0)
    if top == b'esp/RGB/G' and msg == b'1':
        green.duty(1023)
    elif top == b'esp/RGB/G' and msg == b'0':
        green.duty(0)
    if top == b'esp/RGB/B' and msg == b'1':
        blue.duty(1023)
    elif top == b'esp/RGB/B' and msg == b'0':
        blue.duty(0)
        
wifi = network.WLAN(network.STA_IF)
if not wifi.isconnected():
    wifi.active(True)
    wifi.connect('fuken404', '12345678')
    print("Contectado a la red")
else:
    print("Ya se encontraba conectado")
    
server = "broker.hivemq.com"
idClient = b'Snakeman'
topicSub = b'esp/RGB/#'
cliente = MQTTClient(idClient, server)
cliente.connect()

while True:
    cliente.set_callback(subs)
    cliente.subscribe(topicSub)
