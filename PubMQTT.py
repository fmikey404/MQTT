from machine import Pin
from umqtt.simple import MQTTClient
import network, random
 
red = network.WLAN(network.STA_IF)
if not red.isconnected():
    red.active(True)
    red.connect('fuken404', '12345678')
    print("Contectado a la red")
else:
    print("Ya se encontraba conectado")
    
server = "broker.hivemq.com"
idClient = b'Snakeman'
topic = b'esp/numRandom'
cliente = MQTTClient(idClient, server)
cliente.connect()

while True:
    try:
        num = random.randint(0, 101)
        num = str(num)
        cliente.publish(topic, num)
    except:
        print("Algo falló")
