import zipfile as zp
import pyodbc
import json
import os

def iniciar():

    # Conectar com o servidor
    dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-2R15BM3\SQLEXPRESS;"
    "Database=ToDoList_DB;"
    )
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()

    cursor.execute("USE ToDoList_DB")

    # Dicionário tabela de tarefas
    cursor.execute("SELECT * FROM TB_TAREFAS")
    tb_tarefas = cursor.fetchall()
    colunas = [coluna[0] for coluna in cursor.description]
    resultado_tarefa = []
    for linha in tb_tarefas:
        resultado_tarefa.append(dict(zip(colunas, linha)))

    # Dicionário tabela de usuários
    cursor.execute("SELECT NOME_USUARIO, QTD_TAREFAS_CONCLUIDAS FROM TB_USUARIOS")
    tb_usuarios = cursor.fetchall()
    colunas = [coluna[0] for coluna in cursor.description]
    resultado_usuarios = []
    for linha in tb_usuarios:
        resultado_usuarios.append(dict(zip(colunas, linha)))

    nome_arquivo = 'DadosExportados'
        
    with open(f"{nome_arquivo}.json", "w") as outfile:  
        json.dump(resultado_tarefa, outfile) 
        json.dump(resultado_usuarios, outfile) 

    zip_file = zp.ZipFile(f'{nome_arquivo}.zip', "w")  
    zip_file.write(f'{nome_arquivo}.json', compress_type=zp.ZIP_DEFLATED)  
    zip_file.close()  
    os.remove(f"{nome_arquivo}.json") 

    zip_file.close()  

