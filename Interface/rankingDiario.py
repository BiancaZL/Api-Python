import requests

def iniciar():
    print('ranking diário')

    requisicao = requests.get('http://192.168.15.20:5000/rankingDiario')
    print('requisicao')
    print(requisicao)
    print(requisicao.json())

    teste = requisicao.json()

    for linha in teste:
        print(linha['usuario'])
        print ('/t')
        print(linha['tarefas_concluidas'])