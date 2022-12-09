import inventarioTarefas
import rankingDiario
import rankingPersistencia
import relatorio
import sobre
import tarefasDiarias
import exportar



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
      [7] Exportar\n 
      [0] Voltar\n       
      """))
      
      match menu:
         case 1:
            tarefasDiarias.iniciar()
         case 2:
            inventarioTarefas.iniciar()
         case 3:
            rankingDiario.iniciar()     
         case 4:
            rankingPersistencia.iniciar()
         case 5:
            relatorio.iniciar()               
         case 6:
            sobre.iniciar() 
         case 7:
            exportar.iniciar()            
         case 0:
            menu = 0.  

