"""
1 - Fazer uma calculadora de 4 operações (soma, multiplicação, divisão inteira, potência).
Peça a operação desejada e depois os dois números ao usuário.
"""

operacao = int(input('1 - soma \n'
                     '2 - multiplicação \n'
                     '3 - divisão inteira \n'
                     '4 - potência \n'
                     'Digite um número de 1 a 4 para realizar a operação desejada: '))

if 1 <= operacao <= 4:
    print('Vamos realizar a operação!')
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    if operacao == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == 2:
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operacao == 3:
        print(f'{num1} // {num2} = {num1 // num2}')
    else:
        print(f'{num1} ** {num2} = {num1 ** num2}')
else:
    print('Operação inexistente. Digite um número de 1 a 4.')
