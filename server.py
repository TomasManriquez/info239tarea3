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
    if(random.randint(1,11)>=4):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client:{}".format(message)
        print(clientMsg)
        clientMsg = format(message) 
        UDPServerSocket.sendto(bytesToSend, address)
        print("Link Available")
    else:  
        clientMsg = str.encode("Lost package")
        print("Lost package")
        time.sleep(random.randint(500,3001)*0.001)
        UDPServerSocket.sendto(clientMsg, address)
    