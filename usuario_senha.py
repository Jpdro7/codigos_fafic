print("Bem vindo!")
nome = input("Digite seu nome: ")
usuario = input("Cadastre seu usuario: ")
senha = input("Cadastre sua senha: ")
print("Senha e Usuario cadastrados com sucesso!")
print("Faça login para continuar")
login = input("Digite seu usuario: ")
senha_login = input("Digite sua senha: ")

if login == usuario and senha_login == senha:
    print(f"Bem vindo {nome}!")
else:
    print("Usuario ou senha incorretos, tente novamente!")
    login = input("Digite seu usuario: ")
    senha_login = input("Digite sua senha: ")
    if login == usuario and senha_login == senha:
     print("Login efetuado com sucesso!")
    else:
     print("Usuario ou senha incorretos, tente novamente!")
     login = input("Digite seu usuario: ")
     senha_login = input("Digite sua senha: ")
     if login == usuario and senha_login == senha:
      print("Login efetuado com sucesso!")
     else:
      print("Login falhou")

diaria = int("1")
semanal = int("7")
mensal = int("30") and int("31")
classe_executiva = str("executiva") and str("ex")
classe_economica = str("economica") and str("ec")
hospede = int(input("Quantos dias voce deseja ficar hospedado ? "))
hospede1 = str(input("Qual classe voce deseja se hospedar? "))

if hospede == diaria and classe_economica == hospede1:
    print("O valor da sua hospedagem sera 50 R$")
if hospede == semanal and classe_economica == hospede1:
    print("O valor da sua hospedagem sera 200 R$")
if hospede == mensal and classe_economica == hospede1:
    print("O valor da sua hospedagem sera 300 R$")
if hospede == diaria and classe_executiva == hospede1:
    print("O valor da sua hospedagem sera 400 R$")
if hospede == semanal and classe_executiva == hospede1:
    print("O valor da sua hospedagem sera 000 R$")
if hospede == mensal and classe_executiva == hospede1:
    print("O valor da sua hospedagem sera 100 R$")