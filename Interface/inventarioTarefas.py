import requests

#Mesmas operações do TarefasDiarias

def iniciar():

    dicionario = {"usuario":'LunaMS'}

    requisicao = requests.get(f"http://192.168.15.20:5000/listarInventarioTarefas?usuario='{dicionario['usuario']}'")
    tarefas = requisicao.json()
    
    print('\n\t* * * * INVENTÁRIO DE TAREFAS * * * *\n')

    for tarefa in tarefas:
        print(f"\n\t{tarefa['id_tarefa']}\t{tarefa['nome_tarefa']}\n")
        