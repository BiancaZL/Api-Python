import inventarioTarefas
import rankingDiario
import rankingPersistencia
import relatorio
import sobre
import tarefasDiarias

def iniciar():
   menu = 1


   while menu != 0:
      menu = float(input("""
      \nMENU!\n

      [1] Tarefas Diárias \n  
      [2] Inventário de Tarefas \n  
      [3] Ranking Diário \n   
      [4] Ranking de Persistência \n
      [5] Relatório\n
      [6] Sobre\n 
      [0] Voltar\n       
      """))
      
      match menu:
         case 1:
            tarefasDiarias.iniciar()
            menu = float(0)
         case 2:
            inventarioTarefas.iniciar()
            menu = float(0)
         case 3:
            rankingDiario.iniciar()
            menu = float(0)
         case 4:
            rankingPersistencia.iniciar()
            menu = float(0)           
         case 5:
            relatorio.iniciar()
            menu = float(0)    
         case 6:
            sobre.iniciar()
            menu = float(0)    
         case 7:
            #tarefasDiarias.iniciar()
            menu = float(0)    
         case 8:
            #tarefasDiarias.iniciar()
            menu = float(0)  
