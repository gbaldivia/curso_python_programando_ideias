"""
Loop While
"""
"""
Como declarar?
while condição: #Enquanto a condição for verdadeira, faça:
    #Processo

A palavra break finaliza o loop

Exemplos:
a)
x = True

while x:
    print('Estou rodando')
    x = False

b)
pedido = ''

while pedido != 'quero sair':
    pedido = input('você não vai sair: ').lower()

c)
contador = 0

while contador <9:
    print(contador, end='')
    contador +=1
    if contador == 5:
        break

d)
while contador < 9:
    if contador == 5:
        contador += 1
        continue
    print(contador, end = ' ')
    contador +=1

Dicas: 
1 - Podemos escrever o loop while na mesma linha caso a codificação seja simples
2 - Palavra continue (prosseguir)
"""
