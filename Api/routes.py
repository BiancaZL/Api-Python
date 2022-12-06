from flask import Flask, jsonify
import pyodbc
import json
from datetime import date

  
data = date.today()
dataDeHoje = (f"{data:%d%m%y}")

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

@app.route('/homepage', methods=['GET'])
def homepage():
    texto = 'Página Inicial'
    dicionario = {'string': texto}
    return jsonify(dicionario)

#################

#Ranking dos usuários que mais completaram tarefas diárias
@app.route('/rankingDiario', methods=['GET'])
def rankingDiario():
    try:
        cursor = conexao.cursor()
        print('rankingDiario data:', dataDeHoje)
        
        comandoSQL = """
                        SELECT TOP 10 
                                    U.NOME_USUARIO,
                                    U.QTD_TAREFAS_CONCLUIDAS
                    
                        FROM 		TB_USUARIOS U 	         	           
                                    
                        INNER JOIN TB_TAREFAS T
                        ON U.NOME_USUARIO = T.NOME_USUARIO
            
                        WHERE
                                    TIPO_TAREFA = 'Diária'
                                    AND TAREFA_CONCLUIDA = 1
                                    AND DATA_CONCLUSAO = {}
                                    AND U.QTD_TAREFAS_CONCLUIDAS >= 5
                
                        ORDER BY QTD_TAREFAS_CONCLUIDAS DESC""".format(dataDeHoje)
        cursor.execute(comandoSQL)

        resultado = cursor.fetchall()
        print("\nresultado: ", resultado)
        '''for linha in resultado:
            i = 0
            res = {}
            res["usuario"] = 
            res["tarefas_concluidas"] = 
            i+=1

        #resultado_json = json.dumps(resultado)
        #print(resultado_json)

        return jsonify(res)
        '''

        res = []

        for linha in resultado:

            print("\nlinha no for: ",linha)

            res.append({"usuario": linha[0], "tarefas_concluidas": linha[1]})
            print("\n res no for: ",res)

        print("\nres dps do for: ",res)

        cursor.close()

    except Exception as erro:    
        print('Erro no método ranking diário: ' + erro)
        cursor.close()

    return jsonify(res)

#######################################################################################












app.run(host='0.0.0.0',debug=True)

