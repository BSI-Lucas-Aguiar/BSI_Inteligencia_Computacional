frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."

contador = 0

for letra in frase:
    if letra == 'r':
        contador +=1

print("Aparece %s vezes" %contador)
