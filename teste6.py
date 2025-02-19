nome = input("Digite seu nome")
sobrenome = input("Digite seu sobrenome")

nascimento = int(input('Digite o ano do seu nascimento'))
anoAtual = int(input('Digite o ano atual'))

idade = nascimento - anoAtual

print(f"Bem Vindo! {nome} {sobrenome} Você Tem {idade} Anos")