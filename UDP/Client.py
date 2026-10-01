from socket import *

serverName = '127.0.0.1'
serverPort = 8080

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(5)

class Frases:
    def __init__(self):
        self.frases = [
            'O TCP possui menor velocidade e maior confiabilidade em relação ao UDP',
            'O TCP possui uma orientação a conexão (ao qual requer uma autenticação chamada de three-way handshake)',  # ✅ Corrigido
            'O TCP possui controle de fluxo, retransmissão e controle de congestionamento',
            'O HTTP usa o TCP na porta 80',
            'O TCP tem um cabeçalho cujo o tamanho varia entre 20 a 60 bytes'
        ]

obj = Frases()

for mensagem in obj.frases:
    try:
        print(f"Enviando: {mensagem}")
        clientSocket.sendto(mensagem.encode(), (serverName, serverPort))

        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(f"Resposta do servidor: {modifiedMessage.decode()}\n")

    except timeout:
        print(f"Erro: Servidor não respondeu para a frase: {mensagem}\n")
    except Exception as e:
        print(f"Erro: {e}\n")

clientSocket.close()
