from socket import *
serverName='127.0.0.1'
serverPort=4033
clientSocket = socket(AF_INET,SOCK_DGRAM)
frases=['O TCP possui menor velocidade e maior confiabilidade em relação ao TCP',
         'O TCP possui uma orientação a conexão(ao qual requer uma auntenticação chamada de three-way handshake',
        'O TCP possui controle de fluxo, retransmissão e controle de congestionamento'
        'O HTTP usa o TCP na porta 80'
        ]

for mensagem in frases:
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

