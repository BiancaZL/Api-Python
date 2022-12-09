import requests
import menu

def login():
    print('\t\tLOGIN\n')

    input_usuario = str(input("\nDigite seu nome de usuário: "))
    input_senha = str(input('\nDigite sua senha: ')) 
    dicionario = {"usuario":input_usuario,"senha":input_senha}
    
    requisicao = requests.get(f"http://192.168.15.20:5000/buscarUsuario?usuario='{dicionario['usuario']}'&senha='{dicionario['senha']}'")
    credenciais = requisicao.json()

    if(input_usuario == credenciais['usuario']):   
          
        if(input_senha == credenciais['senha']):
          print("\nBem vindo ao ToDoList!")
          menu.iniciar()
          
        else:
          print('\nO login e a senha não coincidem. Tente novamente.')
    else:
      print('\nUsuário não cadastrado no sistema.')


def cadastro():
    print('\t\tCADASTRO NO SISTEMA\n')

    usuario = str(input('\nInsira um nome de usuário: '))
    senha = str(input('\nDigite uma senha: '))
    dicionario = {"usuario":usuario,"senha":senha}

    requisicao = requests.post(f"http://192.168.15.20:5000/cadastrarUsuario?usuario='{dicionario['usuario']}'&senha='{dicionario['senha']}'")
    mensagem = requisicao.json()
    
    print(f"\n{mensagem['mensagem']}")
              
  
def iniciar():
  flag_login = 1

  while flag_login != 0:

    flag_login = float(input("""
    ******************
    \tLOGIN\n

    [1] Fazer Login \n  
    [2] Cadastro \n  
    [0] Sair do Sitema\n
    
    ******************
    """))
    

    match flag_login:
        case 1:
          login()     
        case 2:
          cadastro()
        case 0:
          print('\nSaindo do sistema...')
          flag_login = float(0)

iniciar()
