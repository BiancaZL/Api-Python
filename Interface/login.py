import menu

input_usuario = ''
input_senha = ''
banco_usuario = 'Bianca'
banco_senha = '123'

flag_login = 1


def logar():
    input_usuario = str(input("\nDigite seu nome de usuário: ")) 
     
    if(input_usuario == banco_usuario):   
        input_senha = str(input("\nDigite sua senha: "))   

        if(input_senha == banco_senha):
          print('\nUsuário autenticado. Bem vindo!')
          menu.iniciar()

        else:
          print('\nO login e a senha não coincidem. Tente novamente.')
    else:
      print('\nUsuário não cadastrado no sistema.')
                 
    #return usuario




while flag_login != 0:

  flag_login = float(input("""
  ******************
  \t\tLOGIN\n

  [1] Fazer Login \n  
  [2] Cadastro \n  
  [0] Sair do Sitema\n
  
  ******************
  """))
  

  match flag_login:
      case 1:
        logar()
        #flag_login = float(0)
      case 2:
        print('\nCadastro')
        flag_login = float(0)
      case 0:
        print('\nSaindo do sistema...')
        flag_login = float(0)




