from flask import Flask, jsonify, request
import pyodbc
from datetime import date

  
data = date.today()
dataDeHoje = (f"{data:%d%m%y}")
msg = ''

print('global data:', dataDeHoje)

#Inicializando o flask
app = Flask(__name__)

#Conexão ao banco SQL Server
dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-2R15BM3\SQLEXPRESS;"
    "Database=ToDoList_DB;"
)
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

#################

@app.route('/', methods=['GET']) #Rota padrão
def start():
    texto = 'A API está funcionando!'
    return texto






#######################################################################################

#Selecionar tarefas do inventário
@app.route('/listarIventarioTarefas', methods=['GET'])
def listarIventarioTarefas():
    try:
        usuario = request.args.get('usuario')

        comandoSQL = f"""
                        SELECT 
                                ID_TAREFA, 
                                NOME_TAREFA 
                        FROM TB_TAREFAS 
                        WHERE 
                                TIPO_TAREFA = 'Inventário' 
                                AND NOME_USUARIO = {usuario}
                                AND DATA_CRIACAO = '021222' --{dataDeHoje}
                                AND TAREFA_CONCLUIDA = 0
                        """
        cursor.execute(comandoSQL)

        resultado = cursor.fetchall()
        print("\nresultado: ", resultado)
  
        res = []

        for linha in resultado:
            res.append({"id_tarefa": linha[0], "nome_tarefa": linha[1]})
   
    except Exception as erro:    
        print(f'Erro no método listar tarefas: {erro}')

    cursor.close()

    return jsonify(res)



#Selecionar tarefas diárias
@app.route('/listarTarefasDiarias', methods=['GET'])
def listarTarefas():
    try:
        usuario = request.args.get('usuario')

        comandoSQL = f"""
                        SELECT 
                            ID_TAREFA, 
                            NOME_TAREFA 
                        FROM TB_TAREFAS 
                        WHERE 
                            TIPO_TAREFA = 'Diária' 
                            AND NOME_USUARIO = {usuario}
                            AND DATA_CRIACAO = '051222' --{dataDeHoje}
                            --AND TAREFA_CONCLUIDA = 0"""
        cursor.execute(comandoSQL)

        resultado = cursor.fetchall()
        print("\nresultado: ", resultado)
  
        res = []

        for linha in resultado:
            res.append({"id_tarefa": linha[0], "nome_tarefa": linha[1]})
   
    except Exception as erro:    
        print(f'Erro no método listar tarefas: {erro}')

    cursor.close()

    return jsonify(res)




#Inserir tarefa 
@app.route('/inserirTarefa', methods=['POST'])
def inserirTarefa():
    
    usuario = request.args.get('usuario')
    id_tarefa = request.args.get('id_tarefa')
    tipo_tarefa = request.args.get('tipo_tarefa')
    nome_tarefa = request.args.get('nomeTarefa')

    try:
        comandoSQL = f"""INSERT INTO TB_TAREFAS(
                            NOME_USUARIO,
                            ID_TAREFA, 
                            NOME_TAREFA, 
                            TIPO_TAREFA, 
                            DATA_CRIACAO, 
                            DATA_CONCLUSAO,
                            TAREFA_CONCLUIDA
                        )
                        VALUES(
                        {usuario},
                        {id_tarefa},
                        {nome_tarefa},
                        {tipo_tarefa},
                        {dataDeHoje}, 
                        '0',
                        0
                        )"""#.format(usuario, id_tarefa, nome_tarefa, tipo_tarefa, dataDeHoje)
        
        cursor.execute(comandoSQL)

    except Exception as erro:    
        msg = f"Erro no método inserirTarefa: {erro}"
        cursor.rollback()
        
    else:
        msg = "Tarefa inserida com sucesso!"
        cursor.commit()
    
    cursor.close()
        
    return jsonify(msg)



#alterar tarefa
@app.route('/alterarTarefa', methods=['PATCH'])
def alterarTarefa():

    usuario = request.args.get('usuario')
    id_alteraTarefa = request.args.get('id_alteraTarefa')
    nome_alteraTarefa = request.args.get('nome_alteraTarefa')

    try:   
        comandoSQL = f"""UPDATE TB_TAREFAS
                        SET NOME_TAREFA = {nome_alteraTarefa}
                        WHERE ID_TAREFA = {id_alteraTarefa} AND NOME_USUARIO = {usuario} 
                    """
        cursor.execute(comandoSQL)

    except Exception as erro:    
        msg = "Erro no método alterarTarefa: ", erro
        cursor.rollback()
        
    else:
        msg = "Tarefa alterada com sucesso!"
        cursor.commit()
    
    cursor.close()
    
    return jsonify(msg)   


#concluir tarefa
@app.route('/concluirTarefa', methods=['PATCH'])
def concluirTarefa():
    try:   
        
        usuario = request.args.get('usuario')
        id_concluiTarefa = request.args.get('id_tarefa')

        comandoSQL = f"""UPDATE TB_TAREFAS
                         SET TAREFA_CONCLUIDA = 1, DATA_CONCLUSAO = {dataDeHoje}
                         WHERE ID_TAREFA = {id_concluiTarefa} AND NOME_USUARIO = {usuario}  
                    """
    
        cursor.execute(comandoSQL)

    except Exception as erro:    
        msg = f"Erro no métodoConcluir tarefa {erro}"
        cursor.rollback()
    else:
        msg = "Tarefa concluída com sucesso!"
        cursor.commit()
    cursor.close()
    return jsonify(msg)   



#deletar tarefa
@app.route('/concluirTarefa', methods=['DELETE'])
def deletarTarefa():
    try:   
        usuario = request.args.get('usuario')   
        id_deletaTarefa = request.args.get('id_deletaTarefa')

        comandoSQL = f"""DELETE FROM TB_TAREFAS
                         WHERE ID_TAREFA = {id_deletaTarefa} AND NOME_USUARIO = {usuario} 
                    """
        cursor.execute(comandoSQL)

    except Exception as erro:    
        msg = f"Erro no método deletar tarefa: {erro}"
        cursor.rollback()
    
    else:
        msg = "Tarefa deletada com sucesso!"
        cursor.commit()
    
    cursor.close()

    return jsonify(msg) 







#######################################################################################

#Ranking dos usuários que mais completaram tarefas diárias
@app.route('/rankingDiario', methods=['GET'])
def rankingDiario():
    try:
          
        comandoSQL = f"""
                        SELECT TOP 10 
                                    U.NOME_USUARIO,
                                    U.QTD_TAREFAS_CONCLUIDAS
                    
                        FROM 		TB_USUARIOS U 	         	           
                                    
                        INNER JOIN TB_TAREFAS T
                        ON U.NOME_USUARIO = T.NOME_USUARIO
            
                        WHERE
                                    TIPO_TAREFA = 'Diária'
                                    AND TAREFA_CONCLUIDA = 1
                                    AND DATA_CONCLUSAO = {'051222'}
                                    AND U.QTD_TAREFAS_CONCLUIDAS >= 5
                
                        ORDER BY QTD_TAREFAS_CONCLUIDAS DESC"""#.format('051222')
        cursor.execute(comandoSQL)

        resultado = cursor.fetchall()
        print("\nresultado: ", resultado)
  
        res = []

        for linha in resultado:
            res.append({"usuario": linha[0], "tarefas_concluidas": linha[1]})
   
    except Exception as erro:    
        print(f'Erro no método ranking diário: {erro}')

    cursor.close()

    return jsonify(res)

#######################################################################################
#Relatório do usuário
#Selecionar tarefas do inventário
@app.route('/relatorio', methods=['GET'])
def relatorio():
    try:
        usuario = request.args.get('usuario')

        comandoSQL = f"""
                        SELECT 
                                ID_TAREFA, 
                                NOME_TAREFA 
                        FROM TB_TAREFAS 
                        WHERE 
                                TIPO_TAREFA = 'Inventário' 
                                AND NOME_USUARIO = {usuario}
                                AND DATA_CRIACAO = '021222' --{dataDeHoje}
                                AND TAREFA_CONCLUIDA = 0
                        """
        cursor.execute(comandoSQL)

        resultado = cursor.fetchall()
        print("\nresultado: ", resultado)
  
        res = []

        for linha in resultado:
            res.append({"id_tarefa": linha[0], "nome_tarefa": linha[1]})
   
    except Exception as erro:    
        print(f'Erro no método listar tarefas: {erro}')

    cursor.close()

    return jsonify(res)









############

app.run(host='0.0.0.0',debug=True)

