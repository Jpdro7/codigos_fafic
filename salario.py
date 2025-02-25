salario = float(input("Digite seu salario: "))
porcentagem = float(input("Digite a porcentagem do seu imposto de renda: "))
print(f"O seu salario {salario} e a porcentagem do IR é {porcentagem}")
ir = salario * porcentagem / 100
salario_liq = ir  salario
print(f"O seu salario liquido é: {salario_liq}")