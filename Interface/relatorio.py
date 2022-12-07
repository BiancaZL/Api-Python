import requests

def iniciar():

  requisicao = requests.get(f"http://192.168.15.20:5000/relatorio?usuario={usuario}")
  tarefas = requisicao.json()

  for tarefa in tarefas:
      print(f"\n\t{tarefa['id_tarefa']}\t{tarefa['nome_tarefa']}\n")