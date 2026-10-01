from socket import *

serverName = '127.0.0.1'
serverPort = 8080

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(5)
clientSocket.connect((serverName, serverPort))

class Frases:
    def __init__(self):
        self.frases = [
            'O UDP possui maior velocidade e menor confiabilidade em relação ao TCP',
            'O UDP não possui orientação a conexão (não requer autenticação ou three-way handshake)',
            'O UDP não possui controle de fluxo, retransmissão ou controle de congestionamento',
            'O DNS usa o UDP na porta 53',
            'O UDP tem um cabeçalho de tamanho fixo de apenas 8 bytes'
        ]

obj = Frases()

for mensagem in obj.frases:
    try:
        print(f"Enviando: {mensagem}")
        clientSocket.send(mensagem.encode())

        modifiedMessage = clientSocket.recv(1024)
        print(f"Resposta do servidor: {modifiedMessage.decode()}\n")

    except timeout:
        print(f"Erro: Servidor não respondeu para a frase: {mensagem}\n")
    except Exception as e:
        print(f"Erro: {e}\n")

clientSocket.close()
