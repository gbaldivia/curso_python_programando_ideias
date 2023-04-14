"""
Sami e Dudu vão fazer uma competição de quem visita mais estados no Brasil em um período de 6 meses, até então Dudu já
visitou o Espírito Santo e São Paulo, enquanto Sami visitou Rio de Janeiro e Bahia.
Crie dois conjuntos diferentes para simbolizar os estados que cada um foi.
Após 6 meses Dudu visitou Bahía, Acre, Santa Catarina e Sergipe, enquanto que Sami visitou Bahía, Minas Gerais, Amazonas
e Paraná.
Utilize um dos conjuntos com os novos Estados. Responda:
- Quais estados Dudu visitou que Sami não foi?
- Quais estados ambos foram?
- Sendo 27 estados no Brasil ao todo, qual porcentagem o vencedor visitou?
"""
dudu = {'Espírito Santo', 'São Paulo'}
sami = {'Rio de Janeiro', 'Bahía'}

sair = ''

while sair != 'não':
    sami.add(input('Qual estado Sami visitou? '))
    sair = input('Tem mais estados a adicionar? sim ou não: ')

sair = ''

while sair != 'não':
    dudu.add(input('Qual estado Dudu visitou? '))
    sair = input('Tem mais estados para adicionar? sim ou não: ')

apenas_dudu = dudu.difference(sami)
print(f'Estados visitadoa apenas por Dudu: {apenas_dudu}')

ambos = dudu & sami
print(f'Ambos foram nos seguintes estados: {ambos}')

if len(dudu) > len(sami):
    print(f'O Dudu visitou {round((27/len(dudu)), 2)} % dos estados brasileiros.')
else:
    print(f'A Sami visitou {round((27 /len(sami)), 2)} % dos estados brasileiros.')
