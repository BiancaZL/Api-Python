import requests

def iniciar():
    requisicao = requests.get('http://192.168.15.20:5000/rankingDiario')

    ranking = requisicao.json()

    print("\n**** Ranking dos usuários que mais completaram tarefas hoje! ****\n")

    for linha in ranking:
        print(f"\n\t{linha['usuario']}\t{linha['tarefas_concluidas']}\n")

        
        