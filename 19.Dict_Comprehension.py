"""
- Representados por chaves {}
- Possuem a relação chave -> dado

Como declarar?
pessoas_idade = {'Ana': 22, 'Matheus': 17, 'Lucas': 24}
pessoas_meia_idade = {chave: dado // 2 for chave, dado in pessoas_idade.items()}
print(pessoas_meia_idade)

# É o mesmo que:
for chave, dado in pessoas_idade.items():
    pessoas_meia_idade[chave] = dado // 2

print(pessoas_meia_idade)

# Pegando apenas maiores de idade
pessoas_idade = {'Ana': 22, 'Matheus': 17, 'Lucas': 24}
maiores_idade = {chave: dado for chave, dado in pessoas_idade.items() if dado >= 18}
print(maiores_idade)

# Tratando os que não são maiores de idade
pessoas_idade = {'Ana': 22, 'Matheus': 17, 'Lucas': 24}
maiores_idade = {chave:(dado if dado >= 18 else 'Não pode entrar') for chave, dado in pessoas_idade.items()}
print(maiores_idade)

"""
pessoas_idade = {'Ana': 22, 'Matheus': 17, 'Lucas': 24}
maiores_idade = {chave: (dado if dado >= 18 else 'Não pode entrar') for chave, dado in pessoas_idade.items()}
print(maiores_idade)
