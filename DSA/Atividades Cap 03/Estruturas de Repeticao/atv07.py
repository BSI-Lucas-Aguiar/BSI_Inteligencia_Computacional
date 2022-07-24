# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20,
# adicione à lista, apenas os valores pares e imprima a lista
lista = []
valor = 4

while valor <= 20:
    if (valor % 2) == 0:
        lista.append(valor)
    valor += 1

print(lista)
