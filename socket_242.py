import network 
import socket
import time

wf = network.WLAN(network.STA_IF)
wf.active(True)
wf.connect('Edwar_Wifi','Electro1')


while not wf.isconnected():
    print(".")
    time.sleep(1)

print("conectado:", wf.ifconfig())


sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.bind((wf.ifconfig()[0], 2024))
sc.listen(5)

print("Esperando conexiones")

(sc, addr) = sc.accept()
print('Cliente conectado de', addr)


while True:
    data = sc.recv(64).decode('utf-8')
    print(data.encode('utf-8'))
    
sc.close()   

