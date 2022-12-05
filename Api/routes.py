from flask import Flask, jsonify

#Inicializando o flask
app = Flask(__name__)

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

  

    return 














app.run(host='0.0.0.0',debug=True)

