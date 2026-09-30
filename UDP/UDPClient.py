from socket import *
serverName='127.0.0.1'
serverPort=4033
clientSocket = socket(AF_INET,SOCK_DGRAM)
message= input('O udp possui maior velocidade e menor confiabilidade em relação ao tcp')
clientSocket . sendto (message . encode (), (serverName , serverPort) )
modifiedMessage , serverAddress = clientSocket . recvfrom(2048)
print (modifiedMessage .decode ())
clientSocket .close()
