#Calculadora Python
x = 1

def operacao(opcao, numero1, numero2):
    if opcao == 1:
        print('O resultado da Soma é: ' + str(numero1 + numero2))
    elif opcao == 2:
        print('O resultado da Subtracao é: ' + str(numero1 - numero2))
    elif opcao == 3:
        print('O resultado da Multiplicacao é: ' + str(numero1 * numero2))
    elif opcao == 4:
        print('O resultado da Divisao é: ' + str(numero1 / numero2))

while x != 0:
    print('1 - Soma')
    print('2 - Subtracao')
    print('3 - Multiplicacao')
    print('4 - Divisao')
    print('0 - Sair')
    x = int(input('Informe uma opcao'))

    if x == 1:
        print('Informe os valores da Soma')
        numero1 = int(input('Informe o primeiro numero:'))
        numero2 = int(input('Informe o segundo numero:'))
        operacao(x, numero1, numero2)
    elif x == 2:
        print('Informe os valores da Subtracao')
        numero1 = int(input('Informe o primeiro numero:'))
        numero2 = int(input('Informe o segundo numero:'))
        operacao(x, numero1, numero2)
    elif x == 3:
        print('Informe os valores da Multiplicacao')
        numero1 = int(input('Informe o primeiro numero:'))
        numero2 = int(input('Informe o segundo numero:'))
        operacao(x, numero1, numero2)
    elif x == 4:
        print('Informe os valores da Divisao')
        numero1 = int(input('Informe o primeiro numero:'))
        numero2 = int(input('Informe o segundo numero:'))
        operacao(x, numero1, numero2)
    elif x == 0:
        print('\nObrigado por utilizar a calculadora')
