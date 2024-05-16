"""Os exercícios a seguir vão conter uma sequência de erros, sua função será alterar os erros e comentar no código o que foi colocado/corrigido.
Lembre-se, não é por que o código funciona, que ele está correto, preste atenção nisso """


'''
'Questão 1'
# Calcule as horas, minutos e segundos e posteriormente, printe os valores na tela.
n = int(input("Quantos segundos? "))

hour = n // 3600
n %= 3600
minutes = n // 60
n %= 60

print(f"{hour}:{minutes}:{n}")'''
#alterado para fstring

'''
'Questão 2'
# Faça um programa que calcule a tabuada
n = int(input('Digite um número: '))

for  i in range(1,11):
    print('{} x {} = {}'.format(n, i, n*i))'''
#correção do comando print (pint -> print) e adicionado os valores no .format

'''
'Questão 3'
# Faça um programa que calcule a média ponderada  de três notas, sabendo que cada nota possui seu peso
a = int(input("Digite nota de peso 2: "))
b = int(input("Digite nota de peso 3: "))
c = int(input("Digite nota de peso 5: "))

media = ((a*2) + (b*3) + (c*5))/10

print('MEDIA = {:.1f}'.format(media))'''
#criado as variaveis "a", "b", "c"

'''
'Questão 4'
# Calcule o salário  do trabalhador.
hours = int(input("Quantidade de horas: "))
value = float(input("Valor das horas: "))

salary = hours * value

print('Salario = U$ {:.2f}'.format(salary))'''
#corrigido o nome da variavel no calculo (vaIue -> value)

'''
'Questão 5'
# Calcule o volume da esfera
radius = float(input())
pi = 3.14159

volume = (4/3) * pi * radius**3

print('VOLUME = {:.3f}'.format(volume))'''
#alterado o nome das variaveis variaveis (radiu -> radius, voIume -> volume)

'''
'Questão 6'
# Dica: o único erro desta questão está no "if clause".
a, b, c = map(int, input().split(','))

if a > b:
    maior = a
elif b > a:
    maior = b
if c > maior:
    maior = c
    
# Printing the result
print(maior, "É o maior")'''
#if alterado

'''
'Questão 7'
"""Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100])
este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

O símbolo ( representa "maior que". Por exemplo:
[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000"""

a = float(input())

if a < 0 or a > 100:
    print('Fora de intervalo')

elif a > 75 and a <= 100:
    print('Intervalo (75,100]')

elif a > 50 and a <= 75:
    print('Intervalo [50,75]')

elif a > 25 and a <= 50:
    print('Intervalo (25,50]')

elif a >= 0 and  a <= 25:
    print('Intervalo [0,25]')
'''
#nada foi alterado alem de organizar os ifs e trocados para elif

'''
'Questão 8'
# Faça um programa que, verifica os números digitados em uma quantidade de vezes definida pelo usuário.
# A verificação vai dizer se ele é par, ímpar, positivo, negativo ou Nulo
n = int(input())
for i in range (0,n):
    i = int(input())
    if i > 0:
        if i%2 == 0:
            print('Par Positivo')
        else:
            print('Ímpar Positivo')
    elif i < 0:
        if i%2 == 0:
            print('Par Negativo')
        else:
            print('Ímpar Negativo')
    else:
        print('NULL')
'''
#adicionado o segundo = nos ifs

'''
'Questão 9'
# Calcule o produto de  dois números inteiros fornecidos pelo usuário.
a = int(input())
b = int(input())

prod = a + b

print('Produto =',prod)
'''
#alterado float para int

'''
'Questão 10'
# Calcule a diferença entre A * B e C * D
a = int(input())
b = int(input())
c = int(input())
d = int(input())

diff = (a*b)-(c*d)

if diff<0:
    diff *= -1

print('Diferença =', diff)'''
#criado a variave diff e tornando ela sempre positiva
