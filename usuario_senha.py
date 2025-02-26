print("Bem Vindo Vagabundo!")
usuario = input("Cadastre seu nome de usuario: ")
senha = input("Cadastre sua senha: ")
print("Senha e Usuario cadastrados com sucesso!")
print("Faça login para continuar")
login = input("Digite seu nome de usuario: ")
senha_login = input("Digite sua senha: ")

if login == usuario and senha_login == senha:
    print("Login efetuado com sucesso!")
else:
    print("Usuario ou senha incorretos!")