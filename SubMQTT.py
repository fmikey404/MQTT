from machine import Pin
from umqtt.simple import MQTTClient
import network

led = Pin(2, Pin.OUT)
def subs(top, msg):
    if top == b'esp/ledInterno' and msg == b'1':
        led.on()
    else:
        led.off()
        
red = network.WLAN(network.STA_IF)
if not red.isconnected():
    red.active(True)
    red.connect('fuken404', '12345678')
    print("Contectado a la red")
else:
    print("Ya se encontraba conectado")
    
server = "broker.hivemq.com"
idClient = b'Snakeman'
topicSub = b'esp/ledInterno'
cliente = MQTTClient(idClient, server)
cliente.connect()

while True:
    try:
        cliente.set_callback(subs)
        cliente.subscribe(topicSub)
    except:
        print("Algo falló")
