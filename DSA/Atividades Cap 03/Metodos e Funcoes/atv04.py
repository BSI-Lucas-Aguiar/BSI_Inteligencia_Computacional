# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos
def printnum(arg1, *lista):
    print(arg1)
    for i in lista:
        print(i)
    return


printnum(100)
printnum('A', 'B', 'C')
