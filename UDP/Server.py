from socket import *

serverPort = 8080
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', serverPort))

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
