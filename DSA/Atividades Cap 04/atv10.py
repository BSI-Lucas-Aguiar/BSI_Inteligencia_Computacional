# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for indice, valor in enumerate(lista):
    if indice <= 5:
        continue
    else:
        print (valor)