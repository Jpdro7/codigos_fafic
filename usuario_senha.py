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

diaria_ec = ("diaria, classe economica") and ("DCE")
semanal_ec = ("semanal, classe economica") and ("SCE")
mensal_ec = ("mensal, classe economica") and ("MCE")
diaria_ex = ("mensal, classe executiva") and ("DCEX")
semanal_ex = ("semanal, classe executiva") and ("SCEX")
mensal_ex = ("mensal, classe executiva") and ("MCEX")
print("Aqui estão todos os nossos planos: ")
print("Diaria, Classe Economica (DCE)")
print("Semanal, Classe Economica (SCE)")
print("Mensal, Classe Economica (MCE)")
print("Diaria, Classe Executiva (DCEX)")
print("Semanal, Classe Executiva (SCEX)")
print("Mensal, Classe Executiva (MCEX)")
hospede = input("Qual plano voce deseja escolher ? ")
if hospede == diaria_ec:
    print("O valor da sua hospedagem sera 49.99 R$")
if hospede == semanal_ec:
    print("O valor da sua hospedagem sera 249.99.00 R$")
if hospede == mensal_ec:
    print("O valor da sua hospedagem sera 499.99 R$")
if hospede == diaria_ex:
    print("O valor da sua hospedagem sera 99.99 R$")
if hospede == semanal_ex:
    print("O valor da sua hospedagem sera 299.99 R$")
if hospede == mensal_ex:
    print("O valor da sua hospedagem sera 649.00 R$")