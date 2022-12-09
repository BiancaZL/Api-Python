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



@app.route('/', methods=['GET']) #Rota padrão
def start():
    texto = 'A API está funcionando!'
    return texto



@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():

    cursor = conexao.cursor()
    try:
        parametros = request.args.to_dict()

        comandoSQL = f"""
                        INSERT INTO TB_USUARIOS(
                            NOME_USUARIO,
                            SENHA
                        )
                        VALUES(
                        {parametros.get("usuario")},		     
                        {parametros.get("senha")}			     				     
                        )
                    """
        cursor.execute(comandoSQL)

    except Exception as erro:    
        msg = {"mensagem":'Erro no cadastrarUsuario: {}'.format(erro)}
        cursor.rollback()
    else:
        msg = {"mensagem":'Usuário criado com sucesso!'}
        cursor.commit()

    cursor.close()
    return jsonify(msg)



# Procura o usuário no banco para fazer o login
@app.route('/buscarUsuario', methods=['GET'])
def buscarUsuario():
    cursor = conexao.cursor()
    try:
        parametros = request.args.to_dict()
        comandoSQL = f"""
                        SELECT
                                NOME_USUARIO,
                                SENHA
                        FROM TB_USUARIOS
                        WHERE	NOME_USUARIO = {parametros.get("usuario")}
                                AND SENHA = {parametros.get("senha")}
                        """
        cursor.execute(comandoSQL)
        resultado = cursor.fetchall()
        print(resultado) 
        res = {"usuario": resultado[0][0], "senha":resultado[0][1]}

    except Exception as erro:    
        print(f'Erro no método buscarUsuario: {erro}')
        res = {"usuario":'Não encontrado', "senha": 'Não encontrada'}
    cursor.close()
    return jsonify(res)



#Selecionar tarefas do inventário
@app.route('/listarInventarioTarefas', methods=['GET'])
def listarIventarioTarefas():
    cursor = conexao.cursor()
    try:
        parametros = request.args.to_dict()

        comandoSQL = f"""
                        SELECT 
                                ID_TAREFA, 
                                NOME_TAREFA 
                        FROM TB_TAREFAS 
                        WHERE 
                                TIPO_TAREFA = 'Inventário' 
                                AND NOME_USUARIO = {parametros.get("usuario")}
                                AND DATA_CRIACAO = {dataDeHoje}
                                AND TAREFA_CONCLUIDA = 0
                        """
        cursor.execute(comandoSQL)
        resultado = cursor.fetchall()

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
    cursor = conexao.cursor()
    try:
        
        parametros = request.args.to_dict()

        comandoSQL = f"""
                        SELECT 
                            ID_TAREFA, 
                            NOME_TAREFA 
                        FROM TB_TAREFAS 
                        WHERE 
                            TIPO_TAREFA = 'Diária' 
                            AND NOME_USUARIO = {parametros.get("usuario")}
                            AND DATA_CRIACAO = {dataDeHoje}
                            AND TAREFA_CONCLUIDA = 0"""
        cursor.execute(comandoSQL)
        resultado = cursor.fetchall()
  
        res = []

        for linha in resultado:
            res.append({"id_tarefa": linha[0], "nome_tarefa": linha[1]})
   
    except Exception as erro:    
        print(f'Erro no método listar tarefas: {erro}')

    cursor.close()

    return jsonify(res)


#Inserir tarefa diária
@app.route('/inserirTarefa', methods=['POST'])
def inserirTarefa():
    cursor = conexao.cursor()

    try:
        
        parametros = request.args.to_dict()

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
                        {parametros.get("usuario")},
                        {parametros.get("id_tarefa")},
                        {parametros.get("nome_tarefa")},                        
                        {parametros.get("tipo_tarefa")},
                        {dataDeHoje}, 
                        '0',
                        0
                        )"""
        
        cursor.execute(comandoSQL)

    except Exception as erro:    
        msg = f"Erro no método inserirTarefa: {erro}"
        cursor.rollback()
        
    else:
        msg = "Tarefa inserida com sucesso!"
        cursor.commit()
    
    cursor.close()
    return jsonify(msg)

#alterar tarefa diária
@app.route('/alterarTarefa', methods=['PATCH'])
def alterarTarefa():

    msg = {}
    cursor = conexao.cursor()

    try:   
        parametros = request.args.to_dict()

        comandoSQL = f"""UPDATE TB_TAREFAS
                        SET NOME_TAREFA = {parametros.get("nome_alteraTarefa")}
                        WHERE ID_TAREFA = {parametros.get("id_alteraTarefa")} AND NOME_USUARIO = {parametros.get("usuario")} 
                    """
        cursor.execute(comandoSQL)

    except Exception as erro:    
        msg = {"mensagem":'Erro no método alterarTarefa: {}'.format(erro)}
        cursor.rollback()
        
    else:
        msg = {"mensagem": 'Tarefa alterada com sucesso!'}
        cursor.commit()
    
    cursor.close()
    return jsonify(msg)   


#concluir tarefa diária
@app.route('/concluirTarefa', methods=['PATCH'])
def concluirTarefa():
    cursor = conexao.cursor()
    try:        
        parametros = request.args.to_dict()

        comandoSQL = f"""UPDATE TB_TAREFAS
                         SET TAREFA_CONCLUIDA = 1, DATA_CONCLUSAO = {dataDeHoje}
                         WHERE ID_TAREFA = {parametros.get("id_concluiTarefa")} AND NOME_USUARIO = {parametros.get("usuario")}  
                    """
        cursor.execute(comandoSQL)

    except Exception as erro:    
        msg = {"mensagem":'Erro no métodoConcluir tarefa: {}'.format(erro)}
        cursor.rollback()
    else:
        msg = {"mensagem":'Tarefa concluída com sucesso!'}
        cursor.commit()

    cursor.close()
    return jsonify(msg)   



#deletar tarefa diária
@app.route('/deletarTarefa', methods=['DELETE'])
def deletarTarefa():
    cursor = conexao.cursor()
    try:   
        parametros = request.args.to_dict()

        comandoSQL = f"""DELETE FROM TB_TAREFAS
                         WHERE ID_TAREFA = {parametros.get("id_deletaTarefa")} AND NOME_USUARIO = {parametros.get("usuario")} 
                    """
        cursor.execute(comandoSQL)

    except Exception as erro:    
        msg = {"mensagem":'Erro no método deletar tarefa:: {}'.format(erro)}
        cursor.rollback()
    
    else:
        msg = {"mensagem":'Tarefa deletada com sucesso!'}
        cursor.commit()
    
    cursor.close()
    return jsonify(msg) 


#Ranking dos usuários que mais completaram tarefas diárias
@app.route('/rankingDiario', methods=['GET'])
def rankingDiario():
    cursor = conexao.cursor()
    try:
        comandoSQL = f"""
                        SELECT TOP 10 
                                    U.NOME_USUARIO,
                                    U.QTD_TAREFAS_CONCLUIDAS
                    
                        FROM 		TB_USUARIOS U 	         	           
                                    
                        INNER JOIN TB_TAREFAS T
                        ON U.NOME_USUARIO = T.NOME_USUARIO
            
                        WHERE
                                    T.TIPO_TAREFA = 'Diária'
                                    AND T.TAREFA_CONCLUIDA = 1
                                    AND T.DATA_CONCLUSAO = {dataDeHoje}
                                    AND U.QTD_TAREFAS_CONCLUIDAS >= 5
                
                        ORDER BY QTD_TAREFAS_CONCLUIDAS DESC"""
        cursor.execute(comandoSQL)
        resultado = cursor.fetchall()
  
        res = []

        for linha in resultado:
            res.append({"usuario": linha[0], "tarefas_concluidas": linha[1]})
   
    except Exception as erro:    
        print(f'Erro no método ranking diário: {erro}')

    cursor.close()
    return jsonify(res)


#Relatório do usuário
@app.route('/relatorioTarefasConcluidas', methods=['GET'])
def relatorioTarefasConcluidas():
    cursor = conexao.cursor()
    try:

        parametros = request.args.to_dict()

        comandoSQL = f"""
                        SELECT 
                                COUNT (*)
                        FROM TB_TAREFAS 
                        WHERE                              
                                NOME_USUARIO = {parametros.get("usuario")}
                                AND DATA_CONCLUSAO = {dataDeHoje}
                                AND TAREFA_CONCLUIDA = 1
                        """
        cursor.execute(comandoSQL)

        resultado = cursor.fetchall()
        res = {"qtd_tarefaC": resultado[0][0]}
   
    except Exception as erro:    
        res = {"qtd_tarefaC":'Não encontrado'}

    cursor.close()
    return jsonify(res)


@app.route('/relatorioTarefasNaoConcluidas', methods=['GET'])
def relatorioTarefasNaoConcluidas():
    cursor = conexao.cursor()
    try:

        parametros = request.args.to_dict()

        comandoSQL = f"""
                        SELECT 
                                COUNT (*)
                        FROM TB_TAREFAS 
                        WHERE                              
                                NOME_USUARIO = {parametros.get("usuario")}
                                AND DATA_CONCLUSAO = {dataDeHoje}
                                AND TAREFA_CONCLUIDA = 0
                        """
        cursor.execute(comandoSQL)

        resultado = cursor.fetchall()
        res = {"qtd_tarefaN": resultado[0][0]}
   
    except Exception as erro:    
        res = {"qtd_tarefaN":'Não encontrado'}

    cursor.close()
    return jsonify(res)







############
app.run(host='0.0.0.0',debug=True)
