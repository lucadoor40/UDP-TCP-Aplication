from socket import *

from UDP.Client import mensagem

severName= '127.0.0.1'
serverPort = 8080

clientSocket = socket(AF_INET,AF_STREAM)
clientSocket.settimeout(5)

class Frases:
    def __init__(self):
     self.frases = [
         'O UDP possui maior velocidade e menor confiabilidade em relação ao TCP',
         'O UDP não possui orientação a conexão (não requer autenticação ou three-way handshake)',
         'O UDP não possui controle de fluxo, retransmissão ou controle de congestionamento',
         'O DNS usa o UDP na porta 53',
         'O UDP tem um cabeçalho de tamanho fixo de apenas 8 bytes'
     ]

obj = Frases

for mensagem in obj.frases:

clientSocket.send(setence.encode)
