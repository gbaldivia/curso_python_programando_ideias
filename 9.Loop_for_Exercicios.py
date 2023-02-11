"""
1 - Faça um programa que calcule a soma dos divisores de um número inteiro definido pelo usuário.
Ex. Se o usuário escolheu 10, temos 1 + 2 + 5 + 10 = 18

2 - Faça um programa que imprima os n primeiros múltiplos de 5, sendo n definido pelo usuário.
Ex. Se o usuário escolheu n = 3, será impresso 5, 10, 15.
"""
print('Exercício 1 ---------------------------------------------------------')
num = int(input('Escolha um número inteiro real positivo: '))
numeros = range(1, num+1)
total = 0

for numero in numeros:
    if num % numero == 0.00:
        total += numero

print(total)

print('Exercício 2 ---------------------------------------------------------')
multiplo = int(input('Digite quantos múltiplos de 5 você quer ver: '))
for numero in range(0, multiplo+1):
    print(numero * 5)
