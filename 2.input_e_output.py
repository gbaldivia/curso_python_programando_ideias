"""
Input e Output

Output - print(): Apresenta dados para o usuário

Input - input(): Recebe dados do usuário

Obs: Todos os dados recebidos são do tipo String.
"""

#print('Digite uma cor:')
#cor = input()

#Versões 2.x
#print('Você escolheu a cor %s' %cor)

#Versão 3.x até 3.7
#print('Você escolheu a cor {0}'.format(cor))

#Versões a partir de 3.7
#print(f'Você escolheu a cor {cor}')

cor = input('Digite uma cor: ')

num = input('Digite um número: ')

#Versão 2.x
#print('Você escolheu a cor %s e o número %s' % (cor, num))

#Versão 3.x até 3.7
#print('Você escolheu a cor {0} e o número {1}'.format(cor, num))

#Versão a partir 3.7
#print(f'Você escolheu a cor {cor} e o número {num}')

#print sem pular linha
#print('tomate')
#print('tomate')
#print('tomate')

#print('tomate', end ='$')
#print('tomate', end ='#')
#print('tomate', end ='%')

###########################################Realizando operações de saída###############################################
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

print(f'A soma é: {int(num1) + int(num2)}')