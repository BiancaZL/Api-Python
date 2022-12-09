import requests

def iniciar():

  dicionario = {"usuario":'BiancaZL'}
  requisicao = requests.get(f"http://192.168.15.20:5000/relatorioTarefasConcluidas?usuario='{dicionario['usuario']}'")
  
  qtd_tarefasConcluidas = requisicao.json()

  requisicao2 = requests.get(f"http://192.168.15.20:5000/relatorioTarefasNaoConcluidas?usuario='{dicionario['usuario']}'")
  
  qtd_tarefasNaoConcluidas = requisicao2.json()

  print(f"\n\tVocê completou {qtd_tarefasConcluidas['qtd_tarefaC']} tarefas hoje, parabéns!")
  print(f"\n\tAinda faltam {qtd_tarefasNaoConcluidas['qtd_tarefaN']} tarefas para serem feitas!")


