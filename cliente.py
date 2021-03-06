from cmath import e
import socket
import random
import threading
import time

msgFromClient       ="Using Link Client 1"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

names = ["Matias","Juan","Jaime","Jose","Daniel","Sebastian","Luciana","Trinidad","Emilia","Ximena"]

def recvfrom(message,UDPClientSocket):
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    if ("Datagram Acepted"!=msgFromServer[0].decode()):
        print("El mensaje no llego")
        print("Enviando de nuevo: "+message.decode())
        send_to(message.decode(),UDPClientSocket)
    else:
        print("Mensaje aceptado: "+message.decode())
        
        
def send_to(message,UDPClientSocket):
    bytesToSend = str.encode(message)  #Lo transformamos a bytes para poder enviarlo 
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    verificator = threading.Thread(target=send_toThr, args=(2,bytesToSend,UDPClientSocket))
    verificator.start()
    recvfrom(bytesToSend,UDPClientSocket)
def send_toThr(seg,bytesToSend,UDPClientSocket):
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    time.sleep(seg)

# Se crea el socket UDP en el lado del cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
message = random.choice(names)
for i in message:
    
    print("Enviando: "+i)
    time.sleep(random.randint(500,3001)*0.001) 
    
    send_to(i,UDPClientSocket)
    

