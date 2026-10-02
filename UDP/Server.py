from socket import *

serverPort = 1206
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('10.0.99.150', serverPort))

print("O servidor está escutando")
print("Que bom saber essas informações sobre o TCP")

try:
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
except KeyboardInterrupt:
    print("\nServidor UDP encerrado!")
    serverSocket.close()
