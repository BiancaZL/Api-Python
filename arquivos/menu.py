import tarefasDiarias 

menu = 1

while menu != 0:
    menu = float(input("""
    \nMENU!\n

    "[1] Cadastrar de produto \n  
    "[2] Relatório de produtos \n  
    "[3] Relatório de Estoque Baixo \n   
    "[4] Exportar dados \n
    "[0] Sair\n
    """
        )
    )
    
    match menu:
        case 1:
           tarefasDiarias.iniciar()
           menu = float(0)
           
        case 2:
            print('a')
            #rankingDiario()
        case 3:
            print('a')
            #relatorioEstoqueBaixo()
        case 4:
            print('a')
            #exportarDados()