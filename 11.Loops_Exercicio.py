"""
1 - Calcule a média dos 5 primeiros números primos da Sequência de Fibonacci
"""
"""
O que é Fibonacci?
Soma é o resultado dos 2 números anteriores
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

Número primo:
Número maior do que 1, divisível apenas por 1 e por ele mesmo
"""
anterior = 0
proximo = 1
parada = 1
soma = 0
while parada <= 5:
    proximo = proximo + anterior
    anterior = proximo - anterior
    divisor = 1
    numero_divisores_inteiros = 0
    while divisor <= proximo:
        if proximo % divisor == 0:
            numero_divisores_inteiros += 1
        divisor += 1
    if numero_divisores_inteiros == 2:
        print(proximo)
        soma += proximo
        parada += 1

print(f'A média dos 5 primeiros números primos da sequencia de Fibonacci é {soma/5}')
