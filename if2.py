nome = input(f"Digite seu nome: ")
print(f"Olá {nome}")
n1 = int(input("Digite sua nota: "))
n2 = int(input("Digite sua nota: "))
n3 = int(input("Digite sua nota: "))
n4 = int(input("Digite sua nota: "))
media = (n1+n2+n3+n4) / 4

if media >= 7:
    print('vc foi aprovado')
else: 
    print('reprovado')
