"""
1 - Faça um programa que calcule o maior palíndromo resultado do produto de dois números de 3 dígitos.

- Políndromo são números que lendo da esquerda para a direita resulta no mesmo número se lido da direita para a esquerda
Ex: 52625
Ex: O maior políndromo resultado do produto de dois números é 91 * 99 = 9009

#Usando for
maior = 0
maiord = 0
maiore = 0
for esquerda in range(100,999):
    for direita in range(100,999):
        numero = str(esquerda * direita)
        if numero == numero[::-1] and int(numero) > maior:
            maior = int(numero)
            maiore = esquerda
            maiord = direita

print(maior)
print(maiore)
print(maiord)

"""
num1 = 999
resultado = 0

while num1 >= 100:
    num2 = num1
    while num2 >= 100:
        numero = str(num1 * num2)
        if numero == numero[::-1]:
            if resultado < int(numero):
                resultado = int(numero)
                num2 -= 1
            else:
                num2 -= 1
        else:
            num2 -= 1
    else:
        num1 -= 1

print(resultado)
