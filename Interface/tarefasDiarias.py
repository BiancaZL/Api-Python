import requests

usuario = 'BiancaZL'

def listarTarefas():
  requisicao = requests.get(f"http://192.168.15.20:5000/listarTarefasDiarias?usuario={usuario}")
  tarefas = requisicao.json()

  for tarefa in tarefas:
      print(f"\n\t{tarefa['id_tarefa']}\t{tarefa['nome_tarefa']}\n")



def inserirTarefa():
  id_tarefa = float(input('\nInsira o número de identificação da tarefa: '))
  nome_tarefa = str(input('\nInsira a sua tarefa: '))
  dicionario = {"usuario":usuario, "id_tarefa":id_tarefa, "tipo_tarefa":'Diária', "nome_tarefa":nome_tarefa}

  requisicao = requests.post(f"http://192.168.15.20:5000/inserirTarefa?usuario={dicionario['usuario']}&id_tarefa={dicionario['id_tarefa']}&tipo_tarefa={dicionario['tipo_tarefa']}&nome_tarefa={dicionario['nome_tarefa']}")
  mensagem = requisicao.json()
  print(mensagem['retorno']) 


def alterarTarefa():
  id_alteraTarefa = float(input('\nInsira o número de identificação da tarefa: '))
  nome_alteraTarefa = str(input('\nDigite o novo nome da tarefa: '))
  dicionario = {"usuario":usuario,"id_alteraTarefa":id_alteraTarefa, "nome_alteraTarefa":nome_alteraTarefa}
  
  requisicao = requests.patch(f"http://192.168.15.20:5000/alterarTarefa?usuario={dicionario['usuario']}&id_alteraTarefa={dicionario['id_alteraTarefa']}&nome_alteraTarefa={dicionario['nome_alteraTarefa']}")
  mensagem = requisicao.json()

  print(mensagem['retorno']) 


def concluirTarefa():
  id_concluiTarefa = float(input('\nInsira o número de identificação da tarefa para concluí-la: '))
  
  dicionario = {"usuario":usuario,"id_concluiTarefa":id_concluiTarefa}

  requisicao = requests.patch(f"http://192.168.15.20:5000/concluirTarefa?usuario={dicionario['usuario']}&id_concluiTarefa={dicionario['id_concluiTarefa']}") 
  mensagem = requisicao.json()

  print(mensagem['retorno'])     


def deletarTarefa():
  id_deletaTarefa = float(input('\nInsira o número de identificação da tarefa para deletá-la: '))
  
  dicionario = {"usuario":usuario,"id_deletaTarefa":id_deletaTarefa}
  
  requisicao = requests.delete(f"http://192.168.15.20:5000/deletarTarefa?usuario={dicionario['usuario']}&id_deletaTarefa={dicionario['id_deletaTarefa']}")
  
  mensagem = requisicao.json()
  print(mensagem['retorno'])   


def iniciar():
 
    print('\t\tLISTA DE TAREFAS DIÁRIAS\n')

    flag_tarefa = 1

    while flag_tarefa != 0:
      
        listarTarefas()

        flag_tarefa = float(input("""
        ******************

        [1] Inserir Tarefa \n  
        [2] Alterar Tarefa \n 
        [3] Marcar Tarefa como Concluída \n 
        [4] Deletar Tarefa \n  
        [0] Voltar ao Menu\n
        
        ******************
        """))
  
        match flag_tarefa:
          case 1:
            inserirTarefa()

          case 2:
            alterarTarefa()
            
          case 3:
            concluirTarefa()
          
          case 4:
            deletarTarefa()

          case 0:
            print('\nVoltando ao menu...')
                






