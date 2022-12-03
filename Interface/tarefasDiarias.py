

def inserir_alterarTarefa():

    while flag_insere_altera != 0:



        flag_insere_altera = float(input(
            '''
            O que você deseja fazer?

            [1] Inserir Tarefa \n  
            [2] Alterar Tarefa\n  
            [Qualquer tecla] Voltar\n
            '''
        ))

        if (flag_insere_altera == 1):
            nomeTarefa = float(input('\nInsira a sua tarefa: '))

            #Insert no banco (criar id pra tarefa)
            #print('\nTarefa criada com sucesso!')


        elif (flag_insere_altera == 2):
            alteraTarefa = float(input('\nInsira o número de identificação da tarefa: '))
            #if(alteraTarefa not found):
                #print('\nEssa tarefa não existe.')
                #retorna para o while insere_altera
        else:
            print('\nVoltando para o menu principal...')
            


def iniciar():
 
    print('\t\tLISTA DE TAREFAS DIÁRIAS\n')

    '''
    for tarefa in banco --
        print(tarefa)
         if(tarefa.notfound):
            print('\nNão há tarefas!')
    '''    

    flag_tarefa = 1

    while flag_tarefa != 0:

        flag_tarefa = float(input("""
        ******************

        [1] Inserir ou Alterar Tarefa \n  
        [2] Marcar Tarefa como Concluída \n  
        [0] Voltar ao Menu\n
        
        ******************
        """))
  
        match flag_tarefa:
          case 1:
            inserir_alterarTarefa()
            
          case 2:
            print('\nCadastro')
              

          case 0:
            print('\nVoltando ao menu...')
                




#inserir tarefa

#deletar tarefa

#alterar informações da tarefa

#marcar tarefa como concluída


