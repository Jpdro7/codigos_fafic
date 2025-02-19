print ('Olá Jp')

n1 = int (float(input('Digite o primeiro número a ser calculado')))
n2 = int (float(input('Digite o segundo número a ser calculado')))
n3 = int (float(input('Digite o terceiro número a ser calculado')))
n4 = int (float(input('Digite o quarto número a ser calculado')))

media = (n1+n2+n3+n4)/4

print('A sua media foi {}'.format(media))

pi = 3.1416
R = float(input('Digite o valor do raio a ser calculado'))

P = 2 * pi * R

print('o valor final é{}',format(P))

B = int(input('Digite o valor do seu cateto'))
C = int(input('Digite o valor do seu cateto'))

B2 = B**2
C2 = C**2

A = (B2 + C2)**(1/2)

print('o valor da hipotenusa é{}'.format(A))

x = float(input('Digite o valor de X'))

fx = -2 * (x**2) - (4 * x) + 3

print('o valor final é{}'.format(fx))

aresta = int(input('Digite o valor da Aresta'))
cubo_aresta = aresta**3
print('o valor do volume é:{}'.format(cubo_aresta))

dist = float(input('Digite a distancia'))
temp = float(input('digite o tempo'))

vm = dist / temp

print('avelocidade média é{}'.format(vm))