"""
Para todos os números de 1 a 99, use Dict Comprehension para encontrar o digito único mais alto em que qualquer um dos
números é divisível.
Ex: 64 tem o maior divisor de dígito único de 8, pois 9 não é divisor de 64.

"""
resultado = {}
for number in range(1, 100):
    list = []
    for divisor in range(1, 10):
        if number % divisor == 0:
            list.append(divisor)
    resultado[number] = max(list)

print(resultado)

resultado = {number: max([divisor for divisor in range(1, 10) if number % divisor == 0]) for number in range(1, 100)}
print(resultado)
