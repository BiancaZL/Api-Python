import requests

def iniciar():

  dicionario = {"usuario":'BiancaZL'}
  requisicao = requests.get(f"http://192.168.15.20:5000/relatorio?usuario='{dicionario['usuario']}'")
 
  tarefas = requisicao.json()

  for tarefa in tarefas:
      print(f"\n\tVocê completou{tarefa['id_tarefa']}\t{tarefa['nome_tarefa']}\n")