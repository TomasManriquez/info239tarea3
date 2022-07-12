from multiprocessing.connection import wait
import socket
import time
import random
localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
msgFromServer       = "Datagram Acepted"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("Link Available")

# Listen for incoming datagrams
while(True):
    #Falta añadir el tiempo para que demore y las condiciones, hasta ahora solo recibe datos y los reenvia
    #Hay que pasar el clientMsg o añadir algo para enviar que sea la confirmacion.
    
    ################

    ##################################
    if (random.randint(1,11)<4):
        tiempo = random.randint(500,3001)*0.001
        print(tiempo)
        time.sleep(tiempo)   
        clientMsg = str.encode("Lost package")
        print("Lost package")
        UDPServerSocket.sendto(clientMsg, address)
        
        
    else:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client:{}".format(message)
        print(clientMsg)
        #print("Link bussy")
        clientMsg = format(message) 
        #print(clientMsg)
        # Sending a reply to client
        #print(bytesToSend.decode())
        UDPServerSocket.sendto(bytesToSend, address)
        print("Link Available")
    