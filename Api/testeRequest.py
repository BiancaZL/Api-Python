import requests

requisicao = requests.get('http://192.168.15.20:5000/homepage')
print('requisicao')
print(requisicao)
print(requisicao.json())

teste = requisicao.json()

aaa = teste['string']
print(aaa)

