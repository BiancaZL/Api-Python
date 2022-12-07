import requests

#Mesmas operações do TarefasDiarias

def iniciar():

    usuario = 'BiancaZL'

    requisicao = requests.get(f"http://192.168.15.20:5000/listarIventarioTarefas?usuario={usuario}")
    tarefas = requisicao.json()
    
    print('\t\tINVENTÁRIO DE TAREFAS\n')

    for tarefa in tarefas:
        print(f"\n\t{tarefa['id_tarefa']}\t{tarefa['nome_tarefa']}\n")
        