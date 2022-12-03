import pyodbc

print('a')

try:
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=DESKTOP-2R15BM3\SQLEXPRESS;"
        "Database=ToDoList_DB;"
    )

    conexao = pyodbc.connect(dados_conexao) # Garantindo que está rodando

    print(conexao)
    print('\nConexão ao Banco realizada com sucesso.')

except Exception as erro:
    print('\nErro ao conectar no Banco de Dados: ' + erro)





