from socket import *

serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)

print("O servidor está escutando")
print("Que bom saber essas informações sobre o UDP")

try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        print(f"Conectado por {addr}")

        sentence = connectionSocket.recv(1024).decode()
        print(f"Recebido: {sentence}")

        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())

        connectionSocket.close()
        print("Cliente desconectado\n")

except KeyboardInterrupt:
    print("\nServidor TCP encerrado!")
    serverSocket.close()