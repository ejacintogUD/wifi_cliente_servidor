import network
import time
import socket


wf = network.WLAN(network.STA_IF)
wf.active(True)

wf.connect('Edwar_Wifi', 'Electro1')

while not wf.isconnected():
    print(".")
    time.sleep(1)
    
    
print("Conectado a:", wf.ifconfig())

s = socket.socket()
s.bind(('192.168.26.180', 2024))
print("Crear el socket")

s.listen(10)

print("Escuchando hasta conexion")
(sc,addr) = s.accept()
print ("Se conecto:" , addr)

while True:
    dato = sc.recv(32)
    print(dato.decode())
    
 
s.close() 














